#!/usr/bin/env python
# app.py

from cleo import Application
from DependencyCmd import DependencyCommand
from ConBuildCmd import ConanBuildCommand

application = Application()
application.add(DependencyCommand())
application.add(ConanBuildCommand())

def run():
    application.run()

if __name__ == '__main__':
    run()