#!/usr/bin/env python3
""" testing unit for client module """
from client import GithubOrgClient
from unittest.mock import Mock, patch, PropertyMock
import unittest
from parameterized import parameterized
from typing import Dict, Any


class TestGithubOrgClient(unittest.TestCase):
    """ test class for githuborgclient """
    @parameterized.expand([
            ('google'),
            ('abc'),
        ])
    @patch('client.get_json', return_value={'payload': True})
    def test_org(self, org_name: str, mock_get: Mock) -> None:
        """ test organizations method for githuborgclient """
        github_cli = GithubOrgClient(org_name)
        self.assertEqual(github_cli.org, {'payload': True})
        url = "https://api.github.com/orgs/{}".format(org_name)
        mock_get.assert_called_once_with(url)

    def test_public_repos_url(self) -> None:
        """ test method for GithubOrgClient._public_repos_url """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as new_mock:
            payload = {"repos_url": "https://api.github.com/orgs/abc/repos"}
            new_mock.return_value = payload
            github_cli = GithubOrgClient("abc")
            self.assertEqual(github_cli._public_repos_url,
                             payload["repos_url"])

    @patch('client.get_json', return_value=[{'name': 'git_repo'}])
    def test_public_repos(self, mock_json) -> None:
        """ test for public repos """
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mocked:
            mocked.return_value = ("https://api.github.com/orgs/aws/repos")
            git_cli = GithubOrgClient("aws")
            self.assertEqual(git_cli.public_repos(), ["git_repo"])
            mock_json.assert_called_once()
            mocked.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo: Dict,
                         license_key: str, result) -> None:
        """ testing the presence of license """
        github_cli = GithubOrgClient("microsoft")
        self.assertEqual(github_cli.has_license(repo,license_key), result)


if __name__ == '__main__':
    unittest.main()
