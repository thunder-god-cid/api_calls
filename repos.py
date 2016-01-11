# This script will connect to Stash and enumerate a list
# of repositories in a project you specify. It will then
# run a git clone for any repository you do not have
# locally. Currently it is tailored for Puppet Development
# with a specific directory structure based off of a
# Vagrant setup from the Vagrant repository in the ETPUPD
# project.
#
# Future functionality might be changing your branches
# to master and issuing a git pull/fetch/rebase.

import stashy
import os
from subprocess import call
from secrets import *

PROJECT = 'ETPUPD'
MODULE_PATH = '/opt/testing/modules/'
DATA_PATH = '/opt/testing/'

stash = stashy.connect("https://repo.advisory.com", user, password)

repo_data = stash.projects[PROJECT].repos.list()

modules = []

for _, repo in enumerate(repo_data):
	for _, links in enumerate(repo['links']['clone']):
		if links['name'] == 'ssh':
			modules.append({ 'name': repo['name'], 'url': links['href'] })

for _, module in enumerate(modules):
	repository_path = MODULE_PATH + module['name']
        hiera_path = DATA_PATH + module['name']
	if not os.path.exists(repository_path) and module['name'] != 'hieradata':
		call(['git', 'clone', module['url'], repository_path])
        elif not os.path.exists(hiera_path) and module['name'] == 'hieradata':
		call(['git', 'clone', module['url'], hiera_path])
	else:
		print "Skip Cloning:", module['name']

