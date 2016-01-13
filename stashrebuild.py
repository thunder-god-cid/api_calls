# This script will delete devel branches for all repositories
# in a project and then recreate them from the master branch.
# the name of the script is a WIP.

import stashy
from secrets import *

stash = stashy.connect("https://repo.advisory.com", user, password)

PROJECT = 'ETPUPD'

REPO = 'foo'
BRANCH = 'devel'

branch_delete = stash.projects[PROJECT].repos[REPO].branches(BRANCH)

# this currently is not correct but is a placeholder for reference
stash.delete(branch_delete)
