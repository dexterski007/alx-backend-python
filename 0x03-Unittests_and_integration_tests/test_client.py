""" testing unit for client module """
from client import GithubOrgClient
from unittest.mock import Mock, patch
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


if __name__ == '__main__':
    unittest.main()
