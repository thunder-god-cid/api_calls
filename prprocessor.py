# This script will parse through a project and return
# information on all open pull requests. You will need to
# create a secrets.py file for this script to read your
# username and password information from.
#
# Example file:
#
#  user = foo
#  password = bar
#
# A future release might include additional PR information
# as well as writing the output to a file so a daily report
# could be generated.

import stashy
import os
from subprocess import call
from secrets import *

stash = stashy.connect("https://repo.advisory.com", user, password)

PROJECT = 'ETPUPD'

repo_data = stash.projects[PROJECT].repos.list()

print "Open Pull Requests in", PROJECT, "\n"

for _, repo in enumerate(repo_data):
	REPO = repo['name']
        pull_requests = stash.projects[PROJECT].repos[REPO].pull_requests.list()
	if pull_requests != []:
		print "Repo:", repo['name']
	for _, pr in enumerate(pull_requests):
		if pr['title'] != []:
			print "Pull Request:", pr['title']
		else:
		        print "No title available"
		print "Author:", pr['author']['user']['displayName']
		print "Source Branch:", pr['fromRef']['displayId']
		print "Target Branch:", pr['toRef']['displayId']
		if 'description' in pr:
			print "Description:", pr['description']
		else:
		        print "No description available"
		if pr['reviewers'] != []:
			for _, reviewers in enumerate(pr['reviewers']):
				print "Reviewers:", reviewers['user']['displayName']
				print "Approved:", reviewers['approved']
		else:
			print "No reviewers assigned"
		print "\n"
