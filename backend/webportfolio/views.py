from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from webportfolio import models
import os
from dotenv import load_dotenv
import requests
import logging

load_dotenv()
logger = logging.getLogger(__name__)

# Create your views here.

GITHUB_KEY = os.getenv("GITHUB_KEY")


class GithubInfo(APIView):
    def get(self, request):
        pub_repos = requests.get(
            "https://api.github.com/users/jakeyjakeyy/repos",
            headers={"Authorization": f"Bearer {GITHUB_KEY}"},
        )
        pub_repos = pub_repos.json()

        languages = {}
        for repo in pub_repos:
            repo_languages = requests.get(
                f"https://api.github.com/repos/jakeyjakeyy/{repo['name']}/languages",
                headers={"Authorization": f"Bearer {GITHUB_KEY}"},
            )
            repo_languages = repo_languages.json()
            for language in repo_languages:
                logger.info(language)
                if language in languages:
                    languages[language] += repo_languages[language]
                else:
                    languages[language] = repo_languages[language]

        return Response(languages)
