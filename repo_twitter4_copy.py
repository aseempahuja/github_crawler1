# from repo_twitter_copy import *
import requests
import json
import csv
import collections
import types
import unicodedata
import sys

import time
import random
import os


def listIssures(user_name, repos, headers):
    data = []

    page_n = 100
    j = 1

    while page_n == 100:
        # a = random.uniform(1,2)
        time.sleep(0.1)

        file_name = "http://api.github.com/repos/" + user_name + "%s/issues?per_page=100&page=%d" % (repos, j)
        repo_issues = requests.get(file_name, headers=headers)
        # print repo_issues, j#if success(200)
        raw_data = json.loads(repo_issues.text)
        page_n = len(raw_data)
        for k in range(page_n):
            data.append(raw_data[k])

        j = j + 1

    return data


def writeIssuesToCSV(repo, issues):  # write to csv
    # f = csv.writer(open(repo+"/"+repo+"mostStarReposIssues.csv", "wb+"))
    item_keys = []
    item_values = []
    count = 0
    count1 = 0

    for i in range(len(issues)):
        singleIssue = issues[i]

        item_values = []

        if singleIssue.keys()[0] == "body":
            count1 = count1 + 1
            writeIssuesToCSV2(repo, singleIssue, count1, 1, 1)


        else:
            count = count + 1
            writeIssuesToCSV2(repo, singleIssue, count, 2, 1)  # use record 72 as title
        # print count, count1


def writeIssuesToCSV2(repo, singleIssue, count, j, title):
    # #print count
    # #print len(singleIssue)
    f1 = csv.writer(open(repo + "/" + repo + "ReposIssues%d.csv" % j, "a+"))
    item_keys = []
    item_values = []

    if count == title:
        write_header = True
    else:
        write_header = False

    for k, v in singleIssue.iteritems():

        if type(v) is not types.DictType:  # if it is not a dict
            ##print k,v
            if write_header:
                item_keys.append(k)
            item_values.append(v)
        else:  # it is a dict

            ##print k,v
            for innerkey, innervalue in v.iteritems():
                if type(innervalue) is not types.DictType:
                    if write_header:
                        rowName = k + "/" + innerkey
                        item_keys.append(rowName)
                    item_values.append(innervalue)
                else:
                    for innerinnerkey, innerinnervalue in innervalue.iteritems():  # invervalue is dict
                        if type(innerinnervalue) is not types.DictType:
                            if write_header:
                                rowName = k + "/" + innerkey + "/" + innerinnerkey
                                item_keys.append(rowName)
                            item_values.append(innerinnervalue)
                        else:
                            for innerinnerinnerkey, innerinnerinnervalue in innerinnervalue.iteritems():
                                if write_header:
                                    rowName = k + "/" + innerkey + "/" + innerinnerkey + "/" + innerinnerinnerkey
                                    item_keys.append(rowName)
                                item_values.append(innerinnerinnervalue)

    if write_header:
        f1.writerow(item_keys)
    f1.writerow(item_values)

# def main():
# 	reload(sys)
# 	sys.setdefaultencoding("utf-8")
# 	user_name='twitter/'
# 	repos="typeahead.js"
# 	#data=Get_data(user_name)

# 	#mostStarRepos=mostStar_repos(data)
# 	# #print(mostStarRepos.get("name"))##print the most star repository name
# 	# #print "mostStarRepos atrribute number is %d" % len(mostStarRepos)#69

# 	#issues = listIssures(user_name, mostStarRepos.get("name"))
# 	issues = listIssures(user_name, repos)
# 	#print "issues number is %d" % len(issues)#337
# 	#print "one issues has atrribute number is %d" % len(issues[1])#21


# 	writeIssuesToCSV(repo,issues)



# if __name__=="__main__":
# 	main()
