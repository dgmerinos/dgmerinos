import interfaces.AWSSecretParameterClient as secrets

#Abstract class instancing, if the class doesn't fully implement all abstract methods, this will fail because interpreter cannot instantiate the abstract class.
mysecretClient = secrets.AWSSecretParameterClient()

print(mysecretClient.GetSecretValueAsync('/gbm/clearing/elfelix/rds'))