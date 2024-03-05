from rest_framework.views import APIView
from rest_framework.response import Response
from webportfolio import models
import os
from dotenv import load_dotenv
import requests
import logging
from datetime import datetime, timezone

load_dotenv()
logger = logging.getLogger(__name__)

# Create your views here.

GITHUB_KEY = os.getenv("GITHUB_KEY")


def check_cache(repo_name):
    cache = models.GithubInfoCache.objects.filter(repo=repo_name).first()
    if cache:
        if (datetime.now(timezone.utc) - cache.cache_time).seconds < 3600:
            logger.info(
                f"{datetime.now(timezone.utc)} - Sending cached data for {repo_name}"
            )
            return cache
    return None


class GithubInfo(APIView):

    def get(self, request, repo, format=None):
        serverTime = datetime.now(timezone.utc)
        logger.info(f"{serverTime} - GithubInfo View: Getting info for {repo}")
        if repo == "public":
            # We are getting the languages for all public repos, and my latest activity
            # First check our cache
            cache = check_cache("public")
            if cache:
                return Response(
                    {
                        "languagePercentages": cache.language_percentages,
                        "lastActive": cache.last_active,
                    },
                    status=200,
                )
                # else continue and update the cache

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

            save_cache = models.GithubInfoCache.objects.create(
                repo="public",
                language_percentages=languages,
                last_active=last_active,
            )
            save_cache.save()

            return Response(
                {"languagePercentages": languages, "lastActive": last_active},
                status=200,
            )

        else:
            # We are getting the languages for a specific repo
            repos = ["cityplanner", "dfchronicles", "webportfolio"]
            if repo not in repos:
                return Response({"message": "This repo is not available"}, status=404)
            cache = check_cache(repo)
            if cache:
                return Response(
                    {"languagePercentages": cache.language_percentages}, status=200
                )
            repo_languages = requests.get(
                f"https://api.github.com/repos/jakeyjakeyy/{repo}/languages",
                headers={"Authorization": f"Bearer {GITHUB_KEY}"},
            )
            repo_languages = repo_languages.json()

            repo_cache = models.GithubInfoCache.objects.create(
                repo=repo, language_percentages=repo_languages
            )
            repo_cache.save()

            return Response({"languagePercentages": repo_languages}, status=200)
