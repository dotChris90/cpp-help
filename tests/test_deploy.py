from cleo import Application
from cleo import CommandTester

import pytest
import os
import tempfile
from cpphelper.DependencyCmd import DependencyCommand

def test_execute():

    with tempfile.TemporaryDirectory() as tempdir:
        application = Application()
        application.add(DependencyCommand())
        
        command = application.find('depend')
        command_tester = CommandTester(command)
        command_tester.execute("--output {0} fast-dds/2.3.2@_/_".format(tempdir))

        assert os.path.isdir(os.path.join(tempdir,"deploy")) == True
        assert ["bin","lib","include"] in os.listdir(os.path.join(tempdir,"deploy"))

        os.rmdir(tempdir)