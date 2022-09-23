import abc


class IAWSSecretParameterClient(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'GetSecretValueAsync') and
                callable(subclass.GetSecretValueAsync))

    @abc.abstractmethod 
    def GetSecretValueAsync(self, secretId: str):
        """Get secret from Secret Manager """
        raise NotImplementedError 

