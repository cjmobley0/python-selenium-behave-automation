# This file is created in order to be able to execute through PyCharm.
# Right click then click "Save 'automation_runner' then fill out parameters
# Consult the Readme for more information

from behave.__main__ import main as behave_main

behave_main('--tags @Done --no-skipped --no-capture')
