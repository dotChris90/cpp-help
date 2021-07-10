from cpphelper import __version__
from cpphelper.ConanDeploy import Deploy

def test_version():
    assert __version__ == '0.1.0'

def test_generator():
    deploy = Deploy("fast-dds/2.3.2@_/_")
    deploy.set_param("/tmp/")
    deploy.generate()
    a = 1
    deploy.restructure()
    a = 1

test_generator()
a = 1