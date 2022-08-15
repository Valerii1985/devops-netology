#!/usr/bin/env python3

import os

bash_command = ["cd ~/devops_netology", "pwd", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()

for result in result_os.split('\n'):
    if result.find('/Users') != -1:
        git_path = result
    elif result.find('изменено') != -1:
        prepare_result = result.replace('\tизменено:     ', '')
        print(git_path, prepare_result)
        