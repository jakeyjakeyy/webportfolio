from rest_framework.views import APIView
from rest_framework.response import Response
from webportfolio import models
import os
from dotenv import load_dotenv
import requests
import logging
from datetime import datetime, timezone
import json

load_dotenv()
logger = logging.getLogger(__name__)

# Create your views here.

GITHUB_KEY = os.getenv("GITHUB_KEY")


def check_cache(repo_name, forced=False):
    """
    Check the cache for a specific repo.

    Args:
        repo_name (str): Name of the repo.
        force (bool): If True, ignore the time limit and return the cache regardless.

    Returns:
        GithubInfoCache: Cached data for the repo, or None if the cache is expired.
    """
    cache = models.GithubInfoCache.objects.filter(repo=repo_name).last()
    if cache:
        if (datetime.now(timezone.utc) - cache.cache_time).seconds < 3600:
            logger.info(
                f"{datetime.now(timezone.utc)} - check_cache: Sending cached data for {repo_name}"
            )
            return cache
        elif forced:
            logger.info(
                f"{datetime.now(timezone.utc)} - check_cache: Sending forced cached data for {repo_name}"
            )
            return cache
    return None


def make_github_request(endpoint, repo_name=None):
    """
    Make a request to the GitHub API.

    Args:
        endpoint (str): The API endpoint.
        repo_name (str): The name of the repo to force the cache in case of error.

    Returns:
        dict: JSON response from the API.
    """
    url = f"https://api.github.com/{endpoint}"
    headers = {"Authorization": f"Bearer {GITHUB_KEY}"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for non-2xx responses
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(
            f"{datetime.now(timezone.utc)} - make_github_request: Error making request to {url}: {e}\n Forcing cache for {repo_name}"
        )
        if repo_name:
            return check_cache(repo_name, forced=True)


def average_languages(languages):
    """
    Average the languages in a dictionary.

    Args:
        languages (dict): A dictionary of languages and their byte counts.

    Returns:
        dict: A dictionary of languages and their percentages.
    """
    total = sum(languages.values())
    for language in languages:
        languages[language] = round((languages[language] / total) * 100)
    # purge any languages that are <= 1%
    languages = {k: v for k, v in languages.items() if v > 1}

    return languages


class GithubInfo(APIView):

    def get(self, request, repo):
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
                    },
                    status=200,
                )
                # else continue and update the cache

            # Get all public repos
            pub_repos = make_github_request("user/repos", "public")
            # logger.info(json.dumps(pub_repos))
            languages = {}
            for repo in pub_repos:
                rname = repo["name"]
                if "jakeyjakeyy" != repo["owner"]["login"]:
                    continue
                if repo["fork"] == True:
                    continue
                # Get languages for each repo
                repo_languages = make_github_request(
                    f"repos/jakeyjakeyy/{rname}/languages", rname
                )
                for language in repo_languages:
                    # Tally up the languages
                    if language in languages:
                        languages[language] += repo_languages[language]
                    else:
                        languages[language] = repo_languages[language]

            languages = average_languages(languages)


            save_cache = models.GithubInfoCache.objects.create(
                repo="public",
                language_percentages=languages,
            )
            save_cache.save()

            return Response(
                {"languagePercentages": languages},
                status=200,
            )

        else:
            # We are getting the languages for a specific repo
            repos = ["cityplanner", "password_manager", "social"]
            if repo not in repos:
                return Response({"message": "This repo is not available"}, status=404)
            cache = check_cache(repo)
            if cache:
                return Response(
                    {"languagePercentages": cache.language_percentages}, status=200
                )
            repo_languages = make_github_request(
                f"repos/jakeyjakeyy/{repo}/languages", repo
            )

            repo_languages = average_languages(repo_languages)

            repo_cache = models.GithubInfoCache.objects.create(
                repo=repo, language_percentages=repo_languages
            )
            repo_cache.save()

            return Response({"languagePercentages": repo_languages}, status=200)
