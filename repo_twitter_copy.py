import urllib.request
import json
import csv
import collections
import types
import unicodedata
import sys

import time
import random
import os
import imp


def convert(data):  # unicode to dict
    if isinstance(data, str):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(list(map(convert, iter(list(data.items())))))
    elif isinstance(data, collections.Iterable):
        return type(data)(list(map(convert, data)))
    else:
        return data


def listAllReposNames(user_name):  # get all repository about twitter
    data = []
    dataName = []

    page_n = 100
    j = 1

    while page_n == 100:
        # a = random.uniform(1,2)
        time.sleep(1)

        file_name = "http://api.github.com/orgs/" + user_name + "repos?per_page=100&page=%d" % (j)

        repo_twitter = requests.get(file_name)
        # print repo_twitter#if success(200)
        raw_data = json.loads(repo_twitter.text)  # raw_data has 100 repos
        page_n = len(raw_data)
        for k in range(page_n):
            data.append(raw_data[k])
            dataName.append(raw_data[k].get("name"))

        j = j + 1

    # print len(data)##print the number of repository
    return data, dataName  # data is the list of all the repository


def writeNamesToCSV(repos_names):  # write to csv

    f = csv.writer(open("repos_names2.csv", "wb+"))

    f.writerow(repos_names)


def writeRepoBasicInfoToCSV(repos):  # write to csv
    f = csv.writer(open("ReposBasicInfo.csv", "wb+"))

    item_keys = []
    item_values = []

    for i in range(len(repos)):
        singleRepo = repos[i]
        if i == 0:
            write_header = True
        else:
            write_header = False

        item_values = []

        for j in range(len(list(singleRepo.keys()))):

            if write_header:
                item_keys.append(list(singleRepo.keys())[j])
            value = singleRepo.get(list(singleRepo.keys())[j])
            item_values.append(value)

        if write_header:
            ##print item_values
            f.writerow(item_keys)
        ##print item_values
        f.writerow(item_values)


def listContributors(user_name, repos, headers):
    print("in list contributors")
    data = []

    page_n = 100
    j = 1

    while page_n == 100:
        # a = random.uniform(1,2)
        time.sleep(1)
#made changes here on march 20
        #file_name = "http://api.github.com/repos/" + user_name + "/contributors" % (repos, j)
        file_name = "https://api.github.com/repos/hyperledger/fabric/contributors"
        webURL=urllib.request.urlopen(file_name)
        r_data=webURL.read()
        encoding = webURL.info().get_content_charset('utf-8')


        #repo_contributors = requests.get("https://api.github.com/repos/hyperledger/fabric/contributors", headers=headers)
        # print repo_contributors, j#if success(200)
        raw_data = json.loads(r_data.decode(encoding))
        print(raw_data)
        page_n = len(raw_data)
        for k in range(page_n):
            data.append(raw_data[k])

        j = j + 1

    ##print len(data)##print the number of repository
    return data


def writeContributorsToCSV(repo, contributors):  # write to csv
# wb+ - Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists.
# If the file does not exist, creates a new file for reading and writing. rb - read binary
    f = csv.writer(open(repo + "/" + repo + "ReposContributors.csv", "wb+"))
    # write_header = True
    item_keys = []
    item_values = []

    for i in range(len(contributors)):
        singleContributor = contributors[i]
        if i == 0:
            write_header = True
        else:
            write_header = False

        item_values = []

        for j in range(len(list(singleContributor.keys()))):

            if write_header:
                item_keys.append(list(singleContributor.keys())[j])
            value = singleContributor.get(list(singleContributor.keys())[j])
            item_values.append(value)

        if write_header:
            ##print item_values
            f.writerow(item_keys)
        ##print item_values
        f.writerow(item_values)


def listTags(user_name, repos, headers):
    data = []

    page_n = 100
    j = 1

    while page_n == 100:
        # a = random.uniform(1,2)
        time.sleep(1)

        file_name = "http://api.github.com/repos/" + user_name + "%s/tags?per_page=100&page=%d" % (repos, j)
        repo_tags = requests.get(file_name, headers=headers)
        # print repo_tags,j#if success(200)
        raw_data = json.loads(repo_tags.text)
        page_n = len(raw_data)
        for k in range(page_n):
            data.append(raw_data[k])

        j = j + 1

    return data


def writeTagsToCSV(repo, tags):  # write to csv
    f = csv.writer(open(repo + "/" + repo + "ReposTags.csv", "wb+"))
    item_keys = []
    item_values = []

    for i in range(len(tags)):
        singleTag = tags[i]
        if i == 0:
            write_header = True
        else:
            write_header = False

        item_values = []

        for k, v in list(singleTag.items()):
            v = convert(v)  # convert unicode to str and dict

            if type(v) == type(""):  # if it is not a dict
                ##print v
                if write_header:
                    item_keys.append(k)
                item_values.append(v)
            else:  # it is a dict

                ##print type(v)
                for innerkey, innervalue in list(v.items()):
                    if write_header:
                        rowName = k + "/" + innerkey
                        item_keys.append(rowName)
                    item_values.append(innervalue)

        if write_header:
            f.writerow(item_keys)
        f.writerow(item_values)


def listBranches(user_name, repos, headers):
    data = []

    page_n = 100
    j = 1

    while page_n == 100:
        # a = random.uniform(1,2)
        time.sleep(1)

        file_name = "http://api.github.com/repos/" + user_name + "%s/branches?per_page=100&page=%d" % (repos, j)
        repo_branch = requests.get(file_name, headers=headers)
        # print repo_branch, j#if success(200)
        raw_data = json.loads(repo_branch.text)
        page_n = len(raw_data)
        for k in range(page_n):
            data.append(raw_data[k])

        j = j + 1

    return data


def writeBranchesToCSV(repo, branches):  # write to csv
    f = csv.writer(open(repo + "/" + repo + "ReposBranches.csv", "wb+"))
    item_keys = []
    item_values = []

    for i in range(len(branches)):
        singleBranch = branches[i]
        if i == 0:
            write_header = True
        else:
            write_header = False

        item_values = []

        for k, v in list(singleBranch.items()):
            v = convert(v)  # convert unicode to str and dict

            if type(v) == type(""):  # if it is not a dict
                ##print v
                if write_header:
                    item_keys.append(k)
                item_values.append(v)
            else:  # it is a dict

                ##print type(v)
                for innerkey, innervalue in list(v.items()):
                    if write_header:
                        rowName = k + "/" + innerkey
                        item_keys.append(rowName)
                    item_values.append(innervalue)

        if write_header:
            f.writerow(item_keys)
        f.writerow(item_values)


def listPulls(user_name, repos, headers):
    data = []

    page_n = 100
    j = 1

    while page_n == 100:
        # a = random.uniform(1,2)
        time.sleep(0.1)

        file_name = "http://api.github.com/repos/" + user_name + "%s/pulls?per_page=100&page=%d" % (repos, j)
        repo_pulls = requests.get(file_name, headers=headers)
        # print repo_pulls,j#if success(200)
        raw_data = json.loads(repo_pulls.text)
        page_n = len(raw_data)
        for k in range(page_n):
            data.append(raw_data[k])

        j = j + 1

    return data


def writePullsToCSV(repo, pulls):  # write to csv
    f = csv.writer(open(repo + "/" + repo + "ReposPulls.csv", "wb+"))
    item_keys = []
    item_values = []

    for i in range(len(pulls)):
        singlePull = pulls[i]
        if i == 0:
            write_header = True
        else:
            write_header = False

        item_values = []

        for k, v in list(singlePull.items()):
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


def listComments(user_name, repos, headers):
    data = []

    page_n = 100
    j = 1

    while page_n == 100:
        # a = random.uniform(1,2)
        time.sleep(0.1)

        file_name = "http://api.github.com/repos/" + user_name + "%s/comments?per_page=100&page=%d" % (repos, j)
        repo_comments = requests.get(file_name, headers=headers)
        # print repo_comments, j#if success(200)
        ##print repo_comments
        raw_data = json.loads(repo_comments.text)
        page_n = len(raw_data)
        for k in range(page_n):
            data.append(raw_data[k])

        j = j + 1

    return data


def writeCommentsToCSV(repo, comments):  # write to csv
    f = csv.writer(open(repo + "/" + repo + "ReposComments.csv", "wb+"))
    item_keys = []
    item_values = []

    for i in range(len(comments)):
        singleComment = comments[i]
        if i == 0:
            write_header = True
        else:
            write_header = False

        item_values = []

        for k, v in list(singleComment.items()):

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


def listCommits(user_name, repos, headers):
    data = []

    page_n = 100
    j = 1

    while page_n == 100:

        file_name = "http://api.github.com/repos/" + user_name + "%s/commits?per_page=100&page=%d" % (repos, j)
        repo_commits = requests.get(file_name, headers=headers)
        # print repo_commits,j
        raw_data = json.loads(repo_commits.text)
        page_n = len(raw_data)
        for k in range(page_n):
            data.append(raw_data[k])

        j = j + 1
        # a = random.uniform(1,2)
        time.sleep(1)

    return data


def writeCommitsToCSV(repo, commits):  # write to csv
    f = csv.writer(open(repo + "/" + repo + "ReposCommits.csv", "wb+"))
    item_keys = []
    item_values = []

    for i in range(len(commits)):
        singleCommit = commits[i]
        if i == 0:
            write_header = True
        else:
            write_header = False

        item_values = []

        for k, v in list(singleCommit.items()):
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


def listContents(user_name, repos, headers):
    # a = random.uniform(1,2)
    time.sleep(1)
    file_name = "http://api.github.com/repos/" + user_name + "%s/readme?per_page=100" % repos
    repo_contents = requests.get(file_name, headers=headers)
    repo_contents
    ##print "contents is %s" % repo_contents
    raw_data = json.loads(repo_contents.text)

    return raw_data


def writeContentsToCSV(repo, contents):  # write to csv
    f = csv.writer(open(repo + "/" + repo + "ReposContents.csv", "wb+"))
    item_keys = []
    item_values = []

    write_header = True

    for k, v in list(contents.items()):

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
                if write_header:
                    rowName = k + "/" + innerkey
                    item_keys.append(rowName)
                item_values.append(innervalue)

    if write_header:
        f.writerow(item_keys)
    f.writerow(item_values)


def main():
    imp.reload(sys)
    sys.setdefaultencoding("utf-8")
    user_name = 'hyperledger/cello/'
    repos, reposNames = listAllReposNames(user_name)

    # contributors=listContributors(user_name,repos.get("name"))#list contributors
    # #print "contributors number is %d" % len(contributors)#71
    # #print "one contributor has atrribute number is %d" % len(contributors[1])#18

    # tags = listTags(user_name, Repos.get("name"))
    # #print "tags number is %d" % len(tags)#15
    # #print "one tag has atrribute number is %d" % len(tags[1])#4

    # pulls = listPulls(user_name, Repos.get("name"))
    # #print "pulls number is %d" % len(pulls)#84
    # #print "one pull has atrribute number is %d" % len(pulls[1])#28


    # branches = listBranches(user_name, Repos.get("name"))
    # #print "branches number is %d" % len(branches)#3
    # #print "one branches has atrribute number is %d" % len(branches[1])#2

    # comments = listComments(user_name, Repos.get("name"))
    # #print "comments number is %d" % len(comments)#33
    # #print "one comments has atrribute number is %d" % len(comments[1])#11

    # commits = listCommits(user_name, Repos.get("name"))
    # #print "commits number is %d" % len(commits)#594
    # #print "one commits has atrribute number is %d" % len(commits[1])#8

    # contents = listContents(user_name, Repos.get("name"))
    # #print "contents number is %d" % len(contents)#12
    # ##print "one contents has atrribute number is %d" % len(contents[1])#8

    writeNamesToCSV(reposNames)


# writeContributorsToCSV(repo,contributors)
# writeTagsToCSV(repo,tags)
# writePullsToCSV(repo,pulls)
# writeBranchesToCSV(repo,branches)
# writeCommentsToCSV(repo,comments)
# writeCommitsToCSV(repo,commits)
# writeContentsToCSV(repo,contents)


if __name__ == "__main__":
    main()


######collaborator not Authenticate
