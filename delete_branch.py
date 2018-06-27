# -- coding: utf-8 --

# https://github.com/jmoiron/python-github
# https://github.com/PyGithub/PyGithub
#https://github.com/copitux/python-github3

import os
import requests
from github import Github

from variables import USER_NAME, PRIVATE_TOKEN_REPO, REPOSITORY_NAME

# list all repositories
'''
url_list_repositories = "{}?access_token={}".format(
	'https://api.github.com/users/'+USER_NAME+'/repos', 
	PRIVATE_TOKEN_REPO
)
'''

# list all branch protected
'''
url_branch_protected = "{}?access_token={}".format(
	'https://api.github.com/repos/'+USER_NAME+'/'+REPOSITORY_NAME+'/branches/master/protection/required_status_checks', 
	PRIVATE_TOKEN_REPO
)
'''

# list all branches 
url_list_branches = "{}?access_token={}".format(
	'https://api.github.com/repos/'+USER_NAME+'/'+REPOSITORY_NAME+'/branches', 
	PRIVATE_TOKEN_REPO
)

datos_ramas = requests.get(url_list_branches).json()
ramas = []

for rama in datos_ramas:
	ramas.append(rama['name'])

url3 = "{}?access_token={}".format(
	'https://api.github.com/repos/'+USER_NAME+'/'+REPOSITORY_NAME+'/git/refs/heads/', 
	PRIVATE_TOKEN_REPO
)

datos_ramas2 = requests.get(url3).json()

f = open('prueba.txt', 'w')

get_dates_branch = []
get_date_last_commit_branch = []
for rama in datos_ramas2:
	f.writelines('name branch: '+rama['ref']+'\nurl last commit: '+rama['object']['url']+'\n\n')
