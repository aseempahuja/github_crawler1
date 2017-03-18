from repo_twitter_copy import *
from repo_twitter2_copy import *
from repo_twitter3_copy import *
from repo_twitter4_copy import *
from repo_twitter5_copy import *


import time
import random
import os

def listInformationForRepos(user_name,repo, headers):

        print "Hello"
        contributors = listContributors(user_name,repo, headers)
	print contributors
	writeContributorsToCSV(repo, contributors)

	tags = listTags(user_name, repo, headers)
	#print "tags number is %d" % len(tags)#15
	##print "one tag has atrribute number is %d" % len(tags[1])
	writeTagsToCSV(repo,tags)

	pulls = listPulls(user_name, repo,headers)
	#print "pulls number is %d" % len(pulls)#84 
	##print "one pull has atrribute number is %d" % len(pulls[1])#28
	writePullsToCSV(repo,pulls)

	branches = listBranches(user_name, repo, headers)
	#print "branches number is %d" % len(branches)#3 
	##print "one branches has atrribute number is %d" % len(branches[1])#2
	writeBranchesToCSV(repo,branches)

	comments = listComments(user_name, repo, headers)
	#print "comments number is %d" % len(comments)#33 
	##print "one comments has atrribute number is %d" % len(comments[1])#11
	writeCommentsToCSV(repo,comments)
	commits = listCommits(user_name, repo, headers)
	#print "commits number is %d" % len(commits)#594 
	##print "one commits has atrribute number is %d" % len(commits[1])#8
	writeCommitsToCSV(repo,commits)
	contents = listContents(user_name, repo, headers)
	#print "contents number is %d" % len(contents)#12 
	##print "one contents has atrribute number is %d" % len(contents[1])#8
	writeContentsToCSV(repo,contents)

	###########################2############################################




	deployKeys = listDeployKeys(user_name, repo, headers)
	#print "deployKeys number is %d" % len(deployKeys)#2
	writeDeployKeysToCSV(repo,deployKeys)

	deployments = listDeployment(user_name, repo, headers)
	#print "deployments number is %d" % len(deployments)#0
	##print "one deployments has atrribute number is %d" % len(deployments[1])#2
	writeDeploymentsToCSV(repo,deployments)

	forks = listForks(user_name, repo, headers)
	#print "forks number is %d" % len(forks)#2419
	##print "one forks has atrribute number is %d" % len(forks[1])#68
	writeForksToCSV(repo,forks)

#################################3#############################################


	
	statsWeek = listStatsWeek(user_name, repo, headers)
	#print "statsWeek number is %d" % len(statsWeek)#52
	writeStatsWeekToCSV(repo,statsWeek)####excute two times with response 202

	stats = listStats(user_name, repo, headers)
	#print "stats number is %d" % len(stats)#70
	##print "one stats has atrribute number is %d" % len(stats[1])#3
	writeStatsToCSV(repo,stats)

	releases = listReleases(user_name, repo, headers)
	#print "releases number is %d" % len(releases)#0
	##print "one releases has atrribute number is %d" % len(releases[1])#68
	writeReleasesToCSV(repo,releases)

	weekAddDel = listWeekAddDel(user_name, repo, headers)
	#print "weekAddDel number is %d" % len(weekAddDel)#177
	writeWeekAddDelToCSV(repo,weekAddDel)

	weekAllOwner = listWeekAllOwner(user_name, repo, headers)
	#print "weekAllOwner attribute number is %d" % len(weekAllOwner)#2
	writeWeekAllOwnerToCSV(repo,weekAllOwner)

	hourDayCommits = listHourDayCommits(user_name, repo, headers)
	#print "hourDayCommits  number is %d" % len(hourDayCommits)#168
	writeHourDayCommitToCSV(repo,hourDayCommits)
################################### 4 ###########################################

	issues = listIssures(user_name, repo, headers)
	#print "issues number is %d" % len(issues)#337
	##print "one issues has atrribute number is %d" % len(issues[1])#21

	writeIssuesToCSV(repo,issues)

################################## 5 #############################################

	assignees = listAssignees(user_name, repo, headers)
	#print "assignees number is %d" % len(assignees)#186
	##print "one assignees has atrribute number is %d" % len(assignees[1])#17
	writeAssigneesToCSV(repo,assignees)

	reposcomments = listCommentsForRepos(user_name, repo, headers)
	#print "reposcomments number is %d" % len(reposcomments)#4710
	writeReposCommentsToCSV(repo,reposcomments)

	issuesEvents = listIssuesEvents(user_name, repo, headers)
	#print "issuesEvents number is %d" % len(issuesEvents)#4433
	##print "one issuesEvents has atrribute number is %d" % len(issuesEvents[1])#9
	writeIssuesEventsToCSV(repo,issuesEvents)
	
	issuesmilestones = listIssuesMilestones(user_name, repo, headers)
	#print "issuesmilestones number is %d" % len(issuesmilestones)#2
	##print "one issuesmilestones has atrribute number is %d" % len(issuesmilestones[1])#15
	writeIssuesMilestonesToCSV(repo,issuesmilestones)

	issuesLabels = listIssuesLabels(user_name, repo, headers)
	#print "issuesLabels number is %d" % len(issuesLabels)#11
	##print "one issuesLabels has atrribute number is %d" % len(issuesLabels[1])#3
	writeIssuesLabelsToCSV(repo,issuesLabels)

	downloads = listDownloads(user_name, repo, headers)
	#print "downloads number is %d" % len(downloads)#11
	# #print "one issuesLabels has atrribute number is %d" % len(issuesLabels[1])#3
	writeDownloadsToCSV(repo,downloads)

def main():

	
	reload(sys)
	sys.setdefaultencoding("utf-8")

	

	
	user_name = "hyperledger/"
	
	headers={'User-Agent':'99992838f540e39d741c','Authorization': '3a09aed5aadfccd24b1cedf77fb22198af92a8da'}
	


	f = file("repos_names2.csv", 'rb')
	reader = csv.reader(f)

	count = 1
	for row in reader:
		count = count +1
		repo=row[0]
		print repo, count

		isExists=os.path.exists(repo)
		if not isExists:
			os.makedirs(repo)
			listInformationForRepos(user_name, repo, headers)
			#a = random.uniform(1,2)
			time.sleep(0.1)

			
	f.close() 
	

	

if __name__=="__main__":
	main()	

