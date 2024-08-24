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
