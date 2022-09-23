from IAWSSecretParameterClient import IAWSSecretParameterClient
from unittest import TestCase
from unittest.mock import patch

class SecretClientMock(IAWSSecretParameterClient):
    def GetSecretValueAsync(self, secretId : str):
        return secretId


class TestExample(TestCase):
    def test_returns_1(self):
        secretClient = SecretClientMock()
        self.assertTrue(secretClient.GetSecretValueAsync('mySecret') == 'mySecret')
        