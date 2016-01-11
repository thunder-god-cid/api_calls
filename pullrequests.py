import stashy
import os
from subprocess import call
from secrets import *

PROJECT = 'ETPUPD'

stash = stashy.connect("https://repo.advisory.com", user, password)

pull_requests = stash.projects[PROJECT].repos.pull_requests.list()

print pull_requests
