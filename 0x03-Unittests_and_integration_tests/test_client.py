#!/usr/bin/env python3
""" testing unit for client module """
from client import GithubOrgClient
from unittest.mock import Mock, patch, PropertyMock
import unittest
from parameterized import parameterized, parameterized_class
from typing import Dict
from fixtures import TEST_PAYLOAD


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
        self.assertEqual(github_cli.has_license(repo, license_key), result)


@parameterized_class(('org_payload', 'repos_payload',
                      'expected_repos', 'apache2_repos'),
                     TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ class for integration test """
    @classmethod
    def setUpClass(cls) -> None:
        """ setup class for building testing"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.side_effect = cls.side_effect_meth

    @classmethod
    def tearDownClass(cls) -> None:
        """ class method for tearing down """
        cls.get_patcher.stop()

    @classmethod
    def side_effect_meth(cls, url: str) -> Mock:
        """ replacing default behaviour of class """
        if url == "https://api.github.com/orgs/google":
            return Mock(json=lambda: cls.org_payload)
        elif url == "https://api.github.com/orgs/google/repos":
            return Mock(json=lambda: cls.repos_payload)
        return Mock(json=lambda: {})

    def test_public_repos(self):
        """ method to test if this class ir working or not """
        github_cli = GithubOrgClient("google")
        self.assertEqual(github_cli.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """ method to test if this can return licenses """
        github_cli = GithubOrgClient("google")
        self.assertEqual(github_cli.public_repos(license="apache-2.0"),
                         self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
