# This file helps set up a PR for review. Effectively, it helps empty the list of files to be reviewed and then
#  recreating them so we can create a PR with those files.
#
# To use,

import shutil
import sys
import os

files_to_back_up = [
    '../src/app/app.component.html'
]

step_backup = 'backup'
step_setup = 'setup'

if len(sys.argv) <= 1:
    print('Needs an argument, either "backup" or "setup"')
    sys.exit()

step = sys.argv[1]

if step not in [step_setup, step_backup]:
    print('Needs an argument, either "backup" or "setup"')
    sys.exit()

if step == step_backup:
    for file_to_back_up in files_to_back_up:
        # Back it up
        shutil.copyfile(file_to_back_up, file_to_back_up + '.BAK')

        # Overwrite the original
        open(file_to_back_up, 'w').close()

if step == step_setup:
    for file_to_back_up in files_to_back_up:
        # Copy the original file back
        shutil.copyfile(file_to_back_up + '.BAK', file_to_back_up)

        # And delete the backup
        os.remove(file_to_back_up + '.BAK')
