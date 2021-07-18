from cleo import Command
from cpphelper.ConanDeploy import Deploy

class DependencyCommand(Command):
    """
    Get Dependencies 

    depend
        {pkg? : what package you want deploy? }
        {--p|profile=default : compile for what profile? }
        {--o|output=. : location where to deploy }
    """

    def handle(self):
        pkg = self.argument('pkg')
        pr  = self.option('profile')
        self.line("Taking package {0} with profile {1}".format(pkg,pr))
        
        deploy = Deploy(pkg,pr)
        if self.option('output') != ".":
            deploy.set_param(self.option('output'))
        else:
            pass 
        deploy.generate()
        deploy.restructure()
    