# from repo_twitter_copy import *

import json
import csv
import collections
import types
import unicodedata
import sys

import time
import random
import os


def listDeployKeys(user_name, repos, headers):
    # a = random.uniform(1,2)
    time.sleep(0.1)

    file_name = "http://api.github.com/repos/" + user_name + "%s/keys?per_page=100" % repos
    repo_DeployKeys = requests.get(file_name, headers=headers)
    # print repo_DeployKeys
    raw_data = json.loads(repo_DeployKeys.text)

    return raw_data


def writeDeployKeysToCSV(repo, deployKeys):  # write to csv
    f = csv.writer(open(repo + "/" + repo + "ReposDeployKeys.csv", "wb+"))
    item_keys = []
    item_values = []

    write_header = True

    for k, v in list(deployKeys.items()):

        # if isinstance(v,basestring) == True:
        ##print v
        # v = unicodedata.normalize('NFKD',v).encode('ascii', 'ignore')
        # v=convert(v)#convert unicode to str and dict

        if type(v) is not dict:  # if it is not a dict
            ##print k,v
            if write_header:
                item_keys.append(k)
            item_values.append(v)
        else:  # it is a dict
#C:\Program Files (x86)\Python36-32\Tools\scripts
            ##print k,v
            for innerkey, innervalue in list(v.items()):
                if write_header:
                    rowName = k + "/" + innerkey
                    item_keys.append(rowName)
                item_values.append(innervalue)

    if write_header:
        f.writerow(item_keys)
    f.writerow(item_values)


def listDeployment(user_name, repos, headers):
    # request = requests.get("https://api.github.com/repos/twitter/typeahead.js/contributors?per_page=100")
    # data=json.loads(request.text)
    # len(data)

    data = []

    page_n = 100
    j = 1

    while page_n == 100:
        # a = random.uniform(1,2)
        time.sleep(0.1)
        file_name = "http://api.github.com/repos/" + user_name + "%s/deployments?per_page=100&page=%d" % (repos, j)
        repo_deployments = requests.get(file_name, headers=headers)
        # print repo_deployments, j#if success(200)
        raw_data = json.loads(repo_deployments.text)
        page_n = len(raw_data)
        for k in range(page_n):
            data.append(raw_data[k])

        j = j + 1

    return data


def writeDeploymentsToCSV(repo, deployments):  # write to csv
    f = csv.writer(open(repo + "/" + repo + "ReposDeployments.csv", "wb+"))
    item_keys = []
    item_values = []

    for i in range(len(deployments)):
        singleDeployment = deployments[i]
        if i == 0:
            write_header = True
        else:
            write_header = False

        item_values = []

        for k, v in list(singleDeployment.items()):
            v=convert(v)#convert unicode to str and dict

            if type(v) == type(""):#if it is not a dict
            	##print v
            	if write_header:
            		item_keys.append(k)
            	item_values.append(v)
            else:#it is a dict

            	##print type(v)
            	for innerkey, innervalue in v.items():
            		innervalue=convert(innervalue)
            		if write_header:
            			rowName=k+"/"+innerkey
            			item_keys.append(rowName)
            		item_values.append(innervalue)

            if write_header:
                item_keys.append(k)
            item_values.append(v)

        if write_header:
            f.writerow(item_keys)
        f.writerow(item_values)


def listForks(user_name, repos, headers):
    # request = requests.get("https://api.github.com/repos/twitter/typeahead.js/contributors?per_page=100")
    # data=json.loads(request.text)
    # len(data)

    data = []

    page_n = 100
    j = 1

    while page_n == 100:

        # a = random.uniform(1,2)
        time.sleep(0.1)

        file_name = "http://api.github.com/repos/" + user_name + "%s/forks?per_page=100&page=%d" % (repos, j)
        repo_forks = requests.get(file_name, headers=headers)
        # print repo_forks, j#if success(200)
        ##print repo_comments
        raw_data = json.loads(repo_forks.text)
        page_n = len(raw_data)
        for k in range(page_n):
            data.append(raw_data[k])

        j = j + 1

    return data


def writeForksToCSV(repo, forks):  # write to csv
    f = csv.writer(open(repo + "/" + repo + "ReposForks.csv", "wb+"))
    item_keys = []
    item_values = []

    for i in range(len(forks)):
        singleFork = forks[i]
        if i == 0:
            write_header = True
        else:
            write_header = False

        item_values = []

        for k, v in list(singleFork.items()):
            # if isinstance(v,basestring) == True:
            ##print v
            # v = unicodedata.normalize('NFKD',v).encode('ascii', 'ignore')
            # v=convert(v)#convert unicode to str and dict

            if type(v) is not dict:  # if it is not a dict
                ##print k,v
                if write_header:
                    item_keys.append(k)
                item_values.append(v)
            else:  # it is a dict

                ##print k,v
                for innerkey, innervalue in list(v.items()):
                    if type(innervalue) is not dict:
                        if write_header:
                            rowName = k + "/" + innerkey
                            item_keys.append(rowName)
                        item_values.append(innervalue)
                    else:
                        for innerinnerkey, innerinnervalue in list(innervalue.items()):  # invervalue is dict
                            if type(innerinnervalue) is not dict:
                                if write_header:
                                    rowName = k + "/" + innerkey + "/" + innerinnerkey
                                    item_keys.append(rowName)
                                item_values.append(innerinnervalue)
                            else:
                                for innerinnerinnerkey, innerinnerinnervalue in list(innerinnervalue.items()):
                                    if write_header:
                                        rowName = k + "/" + innerkey + "/" + innerinnerkey + "/" + innerinnerinnerkey
                                        item_keys.append(rowName)
                                    item_values.append(innerinnerinnervalue)

        if write_header:
            f.writerow(item_keys)
        f.writerow(item_values)

# def main():
# 	reload(sys)
# 	sys.setdefaultencoding("utf-8")
# 	user_name='twitter/'
# 	data=Get_data(user_name)



# 	deployKeys = listDeployKeys(user_name, Repos.get("name"))
# 	#print "deployKeys number is %d" % len(deployKeys)#2


# 	deployments = listDeployment(user_name, Repos.get("name"))
# 	#print "deployments number is %d" % len(deployments)#0
# 	##print "one deployments has atrribute number is %d" % len(deployments[1])#2

# 	forks = listForks(user_name, Repos.get("name"))
# 	#print "forks number is %d" % len(forks)#2419
# 	#print "one forks has atrribute number is %d" % len(forks[1])#68

# 	writeDeployKeysToCSV(repo,deployKeys)
# 	writeDeploymentsToCSV(repo,deployments)
# 	writeForksToCSV(repo,forks)



# if __name__=="__main__":
# 	main()
