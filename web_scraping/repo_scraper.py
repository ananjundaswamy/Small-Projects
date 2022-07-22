#Importing requests package
import pip._vendor.requests

#Importing BeautifulSoup package
from bs4 import BeautifulSoup

#Importing the git.repo.base's Repo module
from git.repo.base import Repo

#Importing git module
import git

#Importing OS module
import os

#Repositories main page
source_url = 'https://github.com/orgs/r-lib/repositories'

#Empty list to store the source URLs that we need to find the repos we want to scrape the files from
source_urls_list = []

#Empty list to store the repository links from which we need to scrape the files from
complete_repo_urls = []

#For-loop to iterate through pages 1-5 of the required repository links and append the appropriate webpage to the source_urls_list
for i in range(1, 6):
    #Temporary string created to store the repository links
    temp_string = source_url + "?page=" + str(i)
    
    #source_urls_list appended with the temporary strings
    source_urls_list.append(temp_string)
    
    #HTTP requests received from the respective links
    request_getter = pip._vendor.requests.get(temp_string)
    
    # soup alias for BeautifulSoup object instantiated
    soup = BeautifulSoup(request_getter.text, 'html.parser')
    
    #Finds all div tags with the 'owns' that contain the a-tags and hrefs of each individual repositories' link
    task = soup.find_all('div', itemprop='owns')
    
    #Base URL for Github repos
    basic_url = "https://github.com/"
    
    #Enumerates and appends the final URLs to the complete_repo_urls list 
    for _,i in enumerate(task):
        #Finds all a tags
        for a_tag in i.find_all('a', href=True):
            #Creation of a final_url variable that stores the URL of every repository to download files from using the href property from HTML
            final_url = basic_url + a_tag['href']

            #If-statement to filter out specific URLs within repositories and 43 is the length of the longest repo name (checked using the len() method)
            if len(final_url) > 43 or final_url.endswith("/issues") or final_url.endswith("/pulls") or final_url.endswith("/stargazers") or "MangoTheCat" in final_url:
                continue
            #Else-condition to append the correct URLs to the complete_repo_urls list
            else: 
                complete_repo_urls.append(final_url)

#Prompts user for input of a valid file path
#Try-except
valid_input_path = False

while (valid_input_path == False):
    #File path requested from user
    file_path = input("Please enter a valid file location to download and store the required github files to: ")
    if (os.path.isdir(file_path) == False):
        valid_input_path = False
        print("Invalid filepath: " + file_path + "Please enter a valid file path to clone the GitHub repo to.")
    else:
        print("Downloading to directory: " + file_path)
        valid_input_path = True

#Git cloning to clone the repositories from the complete_repo_urls list
for link in complete_repo_urls:
    #Link split using the '/' delimiter 
    split_link_list = link.split("/")
    
    #Repository names extracted using indexing on the split_link_list
    repo_final_name = split_link_list[len(split_link_list) - 1]
    
    print ("Downloading module: " + repo_final_name)
    #Repo's clone_from method used here to take in user input as file_path and appended to the repo_final_name string 
    #The above is done to create respective directories for each cloned repository
    #Try-except to see if the repository can be downloaded 
    try:
        Repo.clone_from(link, file_path + "/" + repo_final_name)
    except git.GitCommandError:
        print("GitCommandError raised. Could not download the files from the repository at: " + link)
        #Continues in case of the repository not being able to be downloaded/partially downloaded due to file extension errors
        continue
    except:
        print("Unidentified exception raised. Could not download the files from the repository at: " + link)
        continue