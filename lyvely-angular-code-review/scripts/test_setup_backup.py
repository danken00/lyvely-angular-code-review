# This file helps set up a PR for review. Effectively, it helps empty the list of files to be reviewed and then
#  recreating them so we can create a PR with those files.
#
# 1. In the `main` branch, back up the files so we can empty them and recreate them later:
#     `python3 test_setup_backup.py backup`
# 2. Commit the emptied files. The backup files should still be there and Git should ignore them
# 3. Create a new branch from `main`, and switch to it e.g. `release/v1.0.0`. Make sure you "bring" the `.BAK` files
#     with you to the new branch
# 4. Now restore the backup files: `python3 test_setup_backup.py setup`
# 5. Commit those files to the release branch. Now you should have `main` with those files emptied, and your new branch
#     with the original files
# 6. Now, when someone forks the repo, they should be able to create a PR from the release branch to main and leave
#     comments and what not

import shutil
import sys
import os

files_to_back_up = [
  '../src/app/app.component.html',
  '../src/app/app.component.ts',
  '../assets/images/moon.png',
  '../assets/images/sun.png',
  '../assets/images/white-logo-lyvely.svg',
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
