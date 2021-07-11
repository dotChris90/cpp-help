import os
import shutil

class Deploy(object):

    def __init__(self,package_name : str , profile : str = "default") -> None:
        super().__init__()
        if not ("@" in package_name):
            raise NameError("package name must be full e.g. ABC/1.2.3@_/_")
        if not (len(package_name.split("/")) == 3):
            raise NameError("package name must be valid...")    
        self._package_name = package_name
        self._profile = profile
        self._dst = os.path.join(os.getcwd(),"deploy")
        self._cwd = os.getcwd()

    def set_param(self,destination):
        self._dst = os.path.join(destination,"deploy")

    def generate(self):
        cmd = "conan install -pr {0} -g deploy {1}".format(self._profile,self._package_name)
        if os.path.isdir(self._dst):
            shutil.rmtree(self._dst)
        else:
            pass
        os.makedirs(self._dst,exist_ok=True)
        os.chdir(self._dst)
        os.system(cmd)
    
    def restructure(self):
        os.chdir(self._dst)
        packages = os.listdir(self._dst)
        packages.remove("deploy_manifest.txt")
        for package in packages:
            package_pkg_folders = os.listdir(os.path.join(self._dst,package))
            for pkg in package_pkg_folders:
                prefix = package + "_" if pkg == "licenses" else "" 
                if os.path.isdir(os.path.join(self._dst,package,pkg)):
                    for root, subdirs, files in os.walk(os.path.join(self._dst,package,pkg)):
                        for file in files:
                            os.makedirs(os.path.join(self._dst,pkg),exist_ok=True)
                            shutil.move(
                                os.path.join(root,file),
                                os.path.join(self._dst,pkg,prefix + file)
                            )
            shutil.rmtree(os.path.join(self._dst,package))

