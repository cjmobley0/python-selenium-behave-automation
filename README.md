README
==================



##Execute using Behave through Command Line

behave -m /Users/Chris/Coding/git/python-selenium-behave-automation/tests/features --tags @asdf --no-skipped


##Execute using PyCharm through automation_runner.py

-> Run -> Edit Configurations...

Script: /path/to/python-selenium-behave-automation/tests/automation_runner.py
Script Parameter: -m --tags @asdf --no-skipped
Working directory: /path/to/python-selenium-behave-automation/tests/features/steps

For more behave script parameters, check out their documentation:
https://pythonhosted.org/behave/behave.html