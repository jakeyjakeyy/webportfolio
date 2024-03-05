from rest_framework.views import APIView
from rest_framework.response import Response
from webportfolio import models
import os
from dotenv import load_dotenv
import requests
import logging
import datetime

load_dotenv()
logger = logging.getLogger(__name__)

# Create your views here.

GITHUB_KEY = os.getenv("GITHUB_KEY")


class GithubInfo(APIView):
    def get(self, request, repo, format=None):
        serverTime = datetime.datetime.now()
        logger.info(f"{serverTime} - GithubInfo View: Getting info for {repo}")
        if repo == "public":
            # Get all public repos
            pub_repos = requests.get(
                "https://api.github.com/users/jakeyjakeyy/repos",
                headers={"Authorization": f"Bearer {GITHUB_KEY}"},
            )
            pub_repos = pub_repos.json()

            languages = {}
            for repo in pub_repos:
                # Get languages for each repo
                repo_languages = requests.get(
                    f"https://api.github.com/repos/jakeyjakeyy/{repo['name']}/languages",
                    headers={"Authorization": f"Bearer {GITHUB_KEY}"},
                )
                repo_languages = repo_languages.json()
                for language in repo_languages:
                    # Tally up the languages
                    if language in languages:
                        languages[language] += repo_languages[language]
                    else:
                        languages[language] = repo_languages[language]

            for language in languages:
                # Average the languages
                languages[language] = round(languages[language] / len(pub_repos))

            # Get last activity
            activity = requests.get(
                "https://api.github.com/users/jakeyjakeyy/events",
                headers={"Authorization": f"Bearer {GITHUB_KEY}"},
            )
            activity = activity.json()
            last_active = activity[0]["created_at"]

            return Response(
                {"languagePercentages": languages, "lastActive": last_active},
                status=200,
            )

        else:
            repos = ["cityplanner", "dfchronicles", "webportfolio"]
            if repo not in repos:
                return Response({"message": "This repo is not available"}, status=404)
            # We are getting the languages for a specific repo
            repo_languages = requests.get(
                f"https://api.github.com/repos/jakeyjakeyy/{repo}/languages",
                headers={"Authorization": f"Bearer {GITHUB_KEY}"},
            )
            repo_languages = repo_languages.json()

            return Response({"languagePercentages": repo_languages}, status=200)
