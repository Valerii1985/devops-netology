#!/usr/bin/env python3

import os
import sys

git_path = os.getcwd()

if len(sys.argv) >= 2:
    git_path = sys.argv[1]

bash_command = ["cd "+ git_path, "git status 2>&1"]
result_os = os.popen(' && '.join(bash_command)).read()
for result in result_os.split('\n'):
    if result.find('fatal:') != -1:
        print("Git репозиторий в " + git_path + " не обнаружен :(")    
    if result.find('изменено') != -1:
        prepare_result = result.replace('\tизменено: ', '') 
        print(git_path + prepare_result)
