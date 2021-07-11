from cleo import Command
import os 

class ConanBuildCommand(Command):
    """
    Do all conan cmds one after one 

    conbuild
        {conanfile? : location of conanfile }
        {--p|profile=default : compile for what profile? }
    """

    def handle(self):
        conanfile_pos = self.argument('conanfile')
        if not conanfile_pos:
            conanfile_pos = os.getcwd()
        else:
            pass 
        conan_dir = conanfile_pos if os.path.isdir(conanfile_pos) else os.path.pardir(conanfile_pos)
        pr = self.option('profile')
        # preapre workspace
        os.chdir(conan_dir)
        print(conan_dir)
        os.makedirs("build",exist_ok=True)
        os.chdir("build")
        # workflow
        os.system("conan source ..")
        os.system("conan install -pr {0} .. --build=missing".format(pr))
        os.system("conan build ..")
        os.system("conan package ..")
