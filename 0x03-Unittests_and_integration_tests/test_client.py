#!/usr/bin/env python3
"""Parameterize a unit test"""
import unittest
import requests
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch


class TestGithubOrgClient(unittest.TestCase):
    """Tests org function"""
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, param, mock):
        """Tests org's output"""
        client = GithubOrgClient(param)
        client.org()
        mock.called_with_once(client.ORG_URL.format(org=param))

    @patch('client.GithubOrgClient.org',
           new_callable=unittest.mock.PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Tests _public_repos_url method's output"""
        mock_payload = {
            "repos_url": "https://api.github.com/orgs/google/repos"
        }
        mock_org.return_value = mock_payload
        client = GithubOrgClient("google")
        result = client._public_repos_url
        self.assertEqual(result, mock_payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Tests public_repos method's output"""
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]
        with patch('client.GithubOrgClient._public_repos_url', new_callable=unittest.mock.PropertyMock) as mock_repos_url:
            mock_repos_url.return_value = "https://api.github.com/orgs/google/repos"
            client = GithubOrgClient("google")
            result = client.public_repos()
            self.assertEqual(result, ["repo1", "repo2", "repo3"])
            mock_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with("https://api.github.com/orgs/google/repos")

