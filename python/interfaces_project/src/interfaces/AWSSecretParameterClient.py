from .IAWSSecretParameterClient import IAWSSecretParameterClient

class AWSSecretParameterClient(IAWSSecretParameterClient):
    def GetSecretValueAsync(self, secretId: str) -> str :
        pass 
        

