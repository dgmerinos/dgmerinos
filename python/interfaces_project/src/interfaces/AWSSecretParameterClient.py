from .IAWSSecretParameterClient import IAWSSecretParameterClient
import botocore 
import botocore.session 
from aws_secretsmanager_caching import SecretCache, SecretCacheConfig 

#Abstract class implementation.
class AWSSecretParameterClient(IAWSSecretParameterClient):
    def GetSecretValueAsync(self, secretId: str) -> str :
        client = botocore.session.get_session().create_client('secretsmanager')
        cache_config = SecretCacheConfig()
        cache = SecretCache( config = cache_config, client = client)
        return cache.get_secret_string(secretId)
        

