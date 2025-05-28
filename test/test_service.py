from os import environ

from apifactory import Service

environ['APIFACTORY_CONTROLLERS_PATH'] = './test/controllers'
environ['APIFACTORY_SPEC_PATH'] = './test/test_spec.yaml'

app = Service()
