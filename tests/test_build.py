from cleo import Application
from cleo import CommandTester

import pytest
import os
import shutil
import tempfile
from cpphelper.ConBuildCmd import ConanBuildCommand

def test_execute():

    with tempfile.TemporaryDirectory() as tempdir:
        
        testfolder = os.path.dirname(__file__)

        conanfile = shutil.copy(
            os.path.join(testfolder,"res","conanfile.py"),
            tempdir
        )

        application = Application()
        application.add(ConanBuildCommand())

        command = application.find('conbuild')
        command_tester = CommandTester(command)
        command_tester.execute("{0}".format(conanfile))

        assert os.path.isdir(os.path.join(tempdir,"build","package")) == True

        os.rmdir(tempdir)