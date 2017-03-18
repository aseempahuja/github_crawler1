#from repo_twitter_copy import *
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

def listAssignees(user_name,repos,headers):
	

	data=[]

	page_n=100
	j=1

	while page_n == 100:
		#a = random.uniform(1,2)
		time.sleep(0.1)

		file_name="http://api.github.com/repos/"+user_name+"%s/assignees?per_page=100&page=%d" %(repos,j)
		repo_assignees = requests.get(file_name, headers=headers)
		#print repo_assignees, j#if success(200)
		##print repo_comments
		raw_data=json.loads(repo_assignees.text)
		page_n=len(raw_data)
		for k in range(page_n):
			data.append(raw_data[k])

		j = j+1


	return data

def writeAssigneesToCSV(repo,assignees):#write to csv
	f = csv.writer(open(repo+"/"+repo+"ReposAssignees.csv", "wb+"))
	item_keys    = []
	item_values = []

	for i in range (len(assignees)):	
		singleassignees=assignees[i]
		if i == 0:
			write_header = True
		else: write_header = False

		item_values = []

		for k , v in singleassignees.iteritems():

		 	
		 	if type(v) is not  types.DictType:#if it is not a dict
		 		##print k,v
		 		if write_header:
		 			item_keys.append(k)
		 		item_values.append(v)
		 	else:#it is a dict

		 		##print k,v
		 		for innerkey, innervalue in v.iteritems():
		 			if type(innervalue) is not types.DictType:
		 				if write_header:
		 					rowName=k+"/"+innerkey
		 					item_keys.append(rowName)	
		 				item_values.append(innervalue)
		 			else:
		 				for innerinnerkey, innerinnervalue in innervalue.iteritems():#invervalue is dict
							if type(innerinnervalue) is not types.DictType:
		 						if write_header:
		 							rowName=k+"/"+innerkey+"/"+innerinnerkey
		 							item_keys.append(rowName)	
		 						item_values.append(innerinnervalue)
		 					else:
		 						for innerinnerinnerkey, innerinnerinnervalue in innerinnervalue.iteritems():
		 							if write_header:
		 								rowName=k+"/"+innerkey+"/"+innerinnerkey+"/"+innerinnerinnerkey
		 								item_keys.append(rowName)
		 							item_values.append(innerinnerinnervalue)




							

		if write_header:
			f.writerow(item_keys)
		f.writerow(item_values)

def listCommentsForRepos(user_name,repos,headers):


	data=[]

	page_n=100
	j=1

	while page_n == 100:

		#a = random.uniform(1,2)
		time.sleep(0.1)



		file_name="http://api.github.com/repos/"+user_name+"%s/issues/comments?per_page=100&page=%d" %(repos,j)
		repo_ReposComments = requests.get(file_name, headers=headers)
		
		#print repo_ReposComments, j#if success(200)
		##print repo_comments
		raw_data=json.loads(repo_ReposComments.text)
		page_n=len(raw_data)
		for k in range(page_n):
			data.append(raw_data[k])

		j = j+1
		

	return data

def writeReposCommentsToCSV(repo,reposcomments):#write to csv
	f = csv.writer(open(repo+"/"+repo+"ReposCommentsForRepos.csv", "wb+"))
	item_keys    = []
	item_values = []

	for i in range (len(reposcomments)):	
		singlereposcomments=reposcomments[i]
		if i == 0:
			write_header = True
		else: write_header = False
		#write_header = False

		item_values = []

		for k , v in singlereposcomments.iteritems():
		 	
		 	if type(v) is not  types.DictType:#if it is not a dict
		 		##print k,v
		 		if write_header:
		 			item_keys.append(k)
		 		item_values.append(v)
		 	else:#it is a dict

		 		##print k,v
		 		for innerkey, innervalue in v.iteritems():
		 			if type(innervalue) is not types.DictType:
		 				if write_header:
		 					rowName=k+"/"+innerkey
		 					item_keys.append(rowName)	
		 				item_values.append(innervalue)
		 			else:
		 				for innerinnerkey, innerinnervalue in innervalue.iteritems():#invervalue is dict
							if type(innerinnervalue) is not types.DictType:
		 						if write_header:
		 							rowName=k+"/"+innerkey+"/"+innerinnerkey
		 							item_keys.append(rowName)	
		 						item_values.append(innerinnervalue)
		 					else:
		 						for innerinnerinnerkey, innerinnerinnervalue in innerinnervalue.iteritems():
		 							if write_header:
		 								rowName=k+"/"+innerkey+"/"+innerinnerkey+"/"+innerinnerinnerkey
		 								item_keys.append(rowName)
		 							item_values.append(innerinnerinnervalue)




							

		if write_header:
			f.writerow(item_keys)
		f.writerow(item_values)



def listIssuesEvents(user_name,repos,headers):


	data=[]

	page_n=100
	j=1

	while page_n == 100:
		#a = random.uniform(1,2)
		time.sleep(0.1)


		file_name="http://api.github.com/repos/"+user_name+"%s/issues/events?per_page=100&page=%d" %(repos,j)
		repo_issuesEvents = requests.get(file_name, headers=headers)
		#print repo_issuesEvents, j#if success(200)
		##print repo_comments
		raw_data=json.loads(repo_issuesEvents.text)
		page_n=len(raw_data)
		for k in range(page_n):
			data.append(raw_data[k])

		j = j+1
		

	return data

def writeIssuesEventsToCSV(repo,issuesEvents):#write to csv
	f = csv.writer(open(repo+"/"+repo+"ReposIssuesEvents.csv", "wb+"))
	item_keys    = []
	item_values = []

	for i in range (len(issuesEvents)):	
		singleissuesEvents=issuesEvents[i]
		if i == 0:
			write_header = True
		else: write_header = False
		#write_header = False

		item_values = []

		for k , v in singleissuesEvents.iteritems():

		 	
		 	if type(v) is not  types.DictType:#if it is not a dict
		 		##print k,v
		 		if write_header:
		 			item_keys.append(k)
		 		item_values.append(v)
		 	else:#it is a dict

		 		##print k,v
		 		for innerkey, innervalue in v.iteritems():
		 			if type(innervalue) is not types.DictType:
		 				if write_header:
		 					rowName=k+"/"+innerkey
		 					item_keys.append(rowName)	
		 				item_values.append(innervalue)
		 			else:
		 				for innerinnerkey, innerinnervalue in innervalue.iteritems():#invervalue is dict
							if type(innerinnervalue) is not types.DictType:
		 						if write_header:
		 							rowName=k+"/"+innerkey+"/"+innerinnerkey
		 							item_keys.append(rowName)	
		 						item_values.append(innerinnervalue)
		 					else:
		 						for innerinnerinnerkey, innerinnerinnervalue in innerinnervalue.iteritems():
		 							if write_header:
		 								rowName=k+"/"+innerkey+"/"+innerinnerkey+"/"+innerinnerinnerkey
		 								item_keys.append(rowName)
		 							item_values.append(innerinnerinnervalue)




							

		if write_header:
			f.writerow(item_keys)
		f.writerow(item_values)


def listIssuesMilestones(user_name,repos,headers):


	data=[]

	page_n=100
	j=1

	while page_n == 100:
		#a = random.uniform(1,2)
		time.sleep(0.1)

		file_name="http://api.github.com/repos/"+user_name+"%s/milestones?per_page=100&page=%d" %(repos,j)
		repo_issuesmilestones = requests.get(file_name, headers=headers)
		#print repo_issuesmilestones, j#if success(200)
		##print repo_comments
		raw_data=json.loads(repo_issuesmilestones.text)
		page_n=len(raw_data)
		for k in range(page_n):
			data.append(raw_data[k])

		j = j+1


	return data

def writeIssuesMilestonesToCSV(repo,issuesmilestones):#write to csv
	f = csv.writer(open(repo+"/"+repo+"ReposIssuesMilestones.csv", "wb+"))
	item_keys    = []
	item_values = []

	for i in range (len(issuesmilestones)):	
		singleissuesMilestones=issuesmilestones[i]
		if i == 0:
			write_header = True
		else: write_header = False

		item_values = []

		for k , v in singleissuesMilestones.iteritems():

		 	
		 	if type(v) is not  types.DictType:#if it is not a dict
		 		##print k,v
		 		if write_header:
		 			item_keys.append(k)
		 		item_values.append(v)
		 	else:#it is a dict

		 		##print k,v
		 		for innerkey, innervalue in v.iteritems():
		 			if type(innervalue) is not types.DictType:
		 				if write_header:
		 					rowName=k+"/"+innerkey
		 					item_keys.append(rowName)	
		 				item_values.append(innervalue)
		 			else:
		 				for innerinnerkey, innerinnervalue in innervalue.iteritems():#invervalue is dict
							if type(innerinnervalue) is not types.DictType:
		 						if write_header:
		 							rowName=k+"/"+innerkey+"/"+innerinnerkey
		 							item_keys.append(rowName)	
		 						item_values.append(innerinnervalue)
		 					else:
		 						for innerinnerinnerkey, innerinnerinnervalue in innerinnervalue.iteritems():
		 							if write_header:
		 								rowName=k+"/"+innerkey+"/"+innerinnerkey+"/"+innerinnerinnerkey
		 								item_keys.append(rowName)
		 							item_values.append(innerinnerinnervalue)




							

		if write_header:
			f.writerow(item_keys)
		f.writerow(item_values)


def listIssuesLabels(user_name,repos,headers):

	data=[]

	page_n=100
	j=1

	while page_n == 100:
		#a = random.uniform(1,2)
		time.sleep(0.1)

		file_name="http://api.github.com/repos/"+user_name+"%s/labels?per_page=100&page=%d" %(repos,j)
		repo_issuesLabels = requests.get(file_name, headers=headers)
		#print repo_issuesLabels, j#if success(200)
		##print repo_comments
		raw_data=json.loads(repo_issuesLabels.text)
		page_n=len(raw_data)
		for k in range(page_n):
			data.append(raw_data[k])

		j = j+1


	return data

def writeIssuesLabelsToCSV(repo,issuesLabels):#write to csv
	f = csv.writer(open(repo+"/"+repo+"ReposIssuesLabels.csv", "wb+"))
	item_keys    = []
	item_values = []

	for i in range (len(issuesLabels)):	
		singleissuesLabels=issuesLabels[i]
		if i == 0:
			write_header = True
		else: write_header = False

		item_values = []

		for k , v in singleissuesLabels.iteritems():

		 	
		 	if type(v) is not  types.DictType:#if it is not a dict
		 		##print k,v
		 		if write_header:
		 			item_keys.append(k)
		 		item_values.append(v)
		 	else:#it is a dict

		 		##print k,v
		 		for innerkey, innervalue in v.iteritems():
		 			if type(innervalue) is not types.DictType:
		 				if write_header:
		 					rowName=k+"/"+innerkey
		 					item_keys.append(rowName)	
		 				item_values.append(innervalue)
		 			else:
		 				for innerinnerkey, innerinnervalue in innervalue.iteritems():#invervalue is dict
							if type(innerinnervalue) is not types.DictType:
		 						if write_header:
		 							rowName=k+"/"+innerkey+"/"+innerinnerkey
		 							item_keys.append(rowName)	
		 						item_values.append(innerinnervalue)
		 					else:
		 						for innerinnerinnerkey, innerinnerinnervalue in innerinnervalue.iteritems():
		 							if write_header:
		 								rowName=k+"/"+innerkey+"/"+innerinnerkey+"/"+innerinnerinnerkey
		 								item_keys.append(rowName)
		 							item_values.append(innerinnerinnervalue)




							

		if write_header:
			f.writerow(item_keys)
		f.writerow(item_values)

def listDownloads(user_name,repos,headers):
	

	data=[]

	page_n=100
	j=1

	while page_n == 100:
		#a = random.uniform(1,2)
		time.sleep(0.1)

		file_name="http://api.github.com/repos/"+user_name+"%s/downloads?per_page=100&page=%d" %(repos,j)
		repo_downloads = requests.get(file_name, headers=headers)
		#print repo_downloads#if success(200)
		##print repo_comments
		raw_data=json.loads(repo_downloads.text)
		page_n=len(raw_data)
		for k in range(page_n):
			data.append(raw_data[k])

		j = j+1


	return data

def writeDownloadsToCSV(repo,downloads):#write to csv
	f = csv.writer(open(repo+"/"+repo+"ReposDownloads.csv", "wb+"))
	item_keys    = []
	item_values = []

	for i in range (len(downloads)):	
		singledownload=downloads[i]
		if i == 0:
			write_header = True
		else: write_header = False

		item_values = []

		for k , v in singledownload.iteritems():

		 	
		 	if type(v) is not  types.DictType:#if it is not a dict
		 		##print k,v
		 		if write_header:
		 			item_keys.append(k)
		 		item_values.append(v)
		 	else:#it is a dict

		 		##print k,v
		 		for innerkey, innervalue in v.iteritems():
		 			if type(innervalue) is not types.DictType:
		 				if write_header:
		 					rowName=k+"/"+innerkey
		 					item_keys.append(rowName)	
		 				item_values.append(innervalue)
		 			else:
		 				for innerinnerkey, innerinnervalue in innervalue.iteritems():#invervalue is dict
							if type(innerinnervalue) is not types.DictType:
		 						if write_header:
		 							rowName=k+"/"+innerkey+"/"+innerinnerkey
		 							item_keys.append(rowName)	
		 						item_values.append(innerinnervalue)
		 					else:
		 						for innerinnerinnerkey, innerinnerinnervalue in innerinnervalue.iteritems():
		 							if write_header:
		 								rowName=k+"/"+innerkey+"/"+innerinnerkey+"/"+innerinnerinnerkey
		 								item_keys.append(rowName)
		 							item_values.append(innerinnerinnervalue)




							

		if write_header:
			f.writerow(item_keys)
		f.writerow(item_values)



# def main():
# 	reload(sys)
# 	sys.setdefaultencoding("utf-8")
# 	user_name='twitter/'
# 	repos="typeahead.js"
# 	#data=Get_data(user_name)
	
# 	#Repos=_repos(data)
# 	# #print(Repos.get("name"))##print the most star repository name
# 	# #print "Repos atrribute number is %d" % len(Repos)#69

# 	#issues = listIssures(user_name, Repos.get("name"))
# 	#assignees = listAssignees(user_name, repos)
# 	# #print "assignees number is %d" % len(assignees)#186
# 	# #print "one assignees has atrribute number is %d" % len(assignees[1])#17

# 	reposcomments = listCommentsForRepos(user_name, repos)
# 	#print "reposcomments number is %d" % len(reposcomments)#4710


# 	# issuesEvents = listIssuesEvents(user_name, repos)
# 	# #print "issuesEvents number is %d" % len(issuesEvents)#4433
# 	# #print "one issuesEvents has atrribute number is %d" % len(issuesEvents[1])#9

# 	# issuesmilestones = listIssuesMilestones(user_name, repos)
# 	# #print "issuesmilestones number is %d" % len(issuesmilestones)#2
# 	# #print "one issuesmilestones has atrribute number is %d" % len(issuesmilestones[1])#15

# 	# issuesLabels = listIssuesLabels(user_name, repos)
# 	# #print "issuesLabels number is %d" % len(issuesLabels)#11
# 	# #print "one issuesLabels has atrribute number is %d" % len(issuesLabels[1])#3
	
# 	# downloads = listDownloads(user_name, repos)
# 	# #print "downloads number is %d" % len(downloads)#11
# 	# #print "one issuesLabels has atrribute number is %d" % len(issuesLabels[1])#3

# 	writeReposCommentsToCSV(repo,reposcomments)
# 	#writeAssigneesToCSV(repo,assignees)
# 	#writeIssuesEventsToCSV(repo,issuesEvents)
# 	#writeIssuesLabelsToCSV(repo,issuesLabels)
# 	#writeDownloadsToCSV(repo,downloads)




# if __name__=="__main__":
# 	main()	




