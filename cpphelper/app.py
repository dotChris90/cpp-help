#!/usr/bin/env python
# app.py

from cleo import Application
from cpphelper.DependencyCmd import DependencyCommand

application = Application()
application.add(DependencyCommand())

def run():
    application.run()

if __name__ == '__main__':
    run()