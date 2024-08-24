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
