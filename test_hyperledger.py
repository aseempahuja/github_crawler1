import time
import random
import os
import sys
from imp import reload
import csv

from totalReposForTwitter import listInformationForRepos


def main():

        reload(sys)

        user_name = "hyperledger/"

        headers = {'User-Agent': '99992838f540e39d741c', 'Authorization': '3a09aed5aadfccd24b1cedf77fb22198af92a8da'}
    #does this work

        with open('repos_names2.csv', newline='') as f:
            reader = csv.reader(f, delimiter=' ', quotechar='|')
            count = 1
            for row in reader:
                count = count + 1
                repo = row[0]
                print(count,repo)


                isExists = os.path.exists(repo)
                if not isExists:
                    os.makedirs(repo)
                     listInformationForRepos(user_name, repo, headers)
                     # a = random.uniform(1,2)
                    time.sleep(0.1)

        f.close()

if __name__ == "__main__":
    main()