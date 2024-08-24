""" testing unit for client module """
from client import GithubOrgClient
from unittest.mock import Mock, patch, PropertyMock
import unittest
from parameterized import parameterized


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


if __name__ == '__main__':
    unittest.main()
