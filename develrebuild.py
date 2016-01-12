# This script is run on the puppet masters and used
# to rebuild the test environment modules and hiera
# data. It will delete all modules and hiera data
# and then issue git clones for the new devel branch.
# The new devel branch is recreated from the master
# branch prior to this script being run.

import stashy
import os
import shutil
from subprocess import call
from secrets import *

stash = stashy.connect("https://repo.advisory.com", user, password)

PROJECT = 'ETPUPD'
MODULE_PATH = '/etc/puppet/environments/test/modules/'
DATA_PATH = '/etc/puppet/environments/test/'

repo_data = stash.projects[PROJECT].repos.list()

modules = []

for _, repo in enumerate(repo_data):
	for _, links in enumerate(repo['links']['clone']):
		if links['name'] == 'ssh':
			modules.append({ 'name': repo['name'], 'url': links['href'] })

for _, module in enumerate(modules):
	repository_path = MODULE_PATH + module['name']
	hiera_path = DATA_PATH + module['name']
	if os.path.exists(repository_path) and module['name'] != 'hieradata':
                shutil.rmtree(repository_path)
		call(['git', 'clone', '-b', 'devel', module['url'], repository_path])
	elif os.path.exists(hiera_path) and module['name'] == 'hieradata':
		shutil.rmtree(hiera_path)
		call(['git', 'clone', '-b', 'devel', module['url'], hiera_path])
	else:
		print "we have unknown issues"
