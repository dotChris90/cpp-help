import os
import shutil

ALLOWED_FOLDERS = [
    "bin",
    "include",
    "lib",
    "licenses",
    "res"
]

class Deploy(object):

    def __init__(self,package_name : str , profile : str = "default") -> None:
        super().__init__()
        if not ("@" in package_name):
            raise NameError("package name must be full e.g. ABC/1.2.3@_/_")
        self._package_name = package_name
        self._profile = profile
        self._dst = os.path.join(os.getcwd(),"deploy")
        self._cwd = os.getcwd()

    def set_param(self,destination):
        self._dst = os.path.join(destination,"deploy")

    def generate(self):
        cmd = "/home/kac2st/.local/bin/conan install -pr {0} -g deploy {1}".format(self._profile,self._package_name)
        os.system("rm -rf {0}".format(self._dst))
        os.system("mkdir -p {0}".format(self._dst))
        os.chdir(self._dst)
        os.system(cmd)
    
    def restructure(self):
        os.chdir(self._dst)
        packages = os.listdir(self._dst)
        packages.remove("deploy_manifest.txt")
        for package in packages:
            package_pkg_folders = os.listdir(os.path.join(self._dst,package))
            for pkg in package_pkg_folders:
                if os.path.isdir(os.path.join(self._dst,package,pkg)):
                    for root, subdirs, files in os.walk(os.path.join(self._dst,package,pkg)):
                        for file in files:
                            shutil.move(
                                os.path.join(root,file),
                                os.path.join(self._dst,pkg)
                            )

            if ("licenses" in package_pkg_folders):
                package_pkg_folders.remove("licenses")
            for package_pkg_folder in package_pkg_folders:
                cmd = "mkdir -p {0}".format(os.path.join(
                    self._dst,
                    package_pkg_folder
                ))
                os.system(cmd)
                pkg_items = os.listdir(os.path.join(self._dst,package,package_pkg_folder))
                for pkg_item in pkg_items:
                    item_abs = os.path.join(self._dst,package,package_pkg_folder,pkg_item)
                    if os.path.isdir(item_abs):
                        os.system("cp -r {0} {1}".format(item_abs,os.path.join(self._dst,package_pkg_folder)))
                    else:
                        shutil.copyfile(
                            item_abs,
                            os.path.join(self._dst,package_pkg_folder,pkg_item)
                        )
            shutil.rmtree(os.path.join(self._dst,package))