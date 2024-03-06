from django.test import TestCase
from unittest.mock import patch, Mock
import requests
from webportfolio.views import make_github_request


class TestGithubRequest(TestCase):
    @patch("webportfolio.views.requests.get")
    @patch("webportfolio.views.logger.error")
    @patch("webportfolio.views.check_cache")
    def test_make_github_request_error(
        self, mock_check_cache, mock_logger_error, mock_requests_get
    ):
        """
        Test case for make_github_request function when it encounters an error.

        This test checks:
        - If make_github_request encounters an error (simulated by causing requests.get to raise a RequestException), it should log an error and call check_cache with forced=True.
        - The result of make_github_request should be the result of check_cache when an error occurs.

        Mocks:
        - requests.get: Simulates an error by raising a RequestException.
        - logger.error: Captures error logging for assertion.
        - check_cache: Returns a predefined result and captures the arguments it was called with for assertion.
        """
        # Arrange
        mock_requests_get.side_effect = requests.exceptions.RequestException
        mock_check_cache.return_value = {"forced": "cache"}

        # Act
        result = make_github_request("users/jakeyjakeyy/repos", "public")

        # Assert
        mock_logger_error.assert_called_once()
        mock_check_cache.assert_called_once_with("public", forced=True)
        self.assertEqual(result, {"forced": "cache"})
