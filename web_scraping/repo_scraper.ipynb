{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "GitCommandError raised. Could not download the files from the repository at: https://github.com//softprops/turnstyle\n"
     ]
    }
   ],
   "source": [
    "#Importing requests package\n",
    "import requests\n",
    "\n",
    "#Importing BeautifulSoup package\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "#Importing the git.repo.base's Repo module\n",
    "from git.repo.base import Repo\n",
    "\n",
    "#Importing git module\n",
    "import git\n",
    "\n",
    "#Repositories main page\n",
    "source_url = 'https://github.com/orgs/r-lib/repositories'\n",
    "\n",
    "#Empty list to store the source URLs that we need to find the repos we want to scrape the files from\n",
    "source_urls_list = []\n",
    "\n",
    "#Empty list to store the repository links from which we need to scrape the files from\n",
    "complete_repo_urls = []\n",
    "\n",
    "#For-loop to iterate through pages 1-5 of the required repository links and append the appropriate webpage to the source_urls_list\n",
    "for i in range(1, 6):\n",
    "    #Temporary string created to store the repository links\n",
    "    temp_string = source_url + \"?page=\" + str(i)\n",
    "    \n",
    "    #source_urls_list appended with the temporary strings\n",
    "    source_urls_list.append(temp_string)\n",
    "    \n",
    "    #HTTP requests received from the respective links\n",
    "    request_getter = requests.get(temp_string)\n",
    "    \n",
    "    # soup alias for BeautifulSoup object instantiated\n",
    "    soup = BeautifulSoup(request_getter.text, 'html.parser')\n",
    "    \n",
    "    #Finds all div tags with the 'owns' that contain the a-tags and hrefs of each individual repositories' link\n",
    "    task = soup.find_all('div', itemprop='owns')\n",
    "    \n",
    "    #Base URL for Github repos\n",
    "    basic_url = \"https://github.com/\"\n",
    "    \n",
    "    #Enumerates and appends the final URLs to the complete_repo_urls list \n",
    "    for _,i in enumerate(task):\n",
    "        #Finds all a tags\n",
    "        for a_tag in i.find_all('a', href=True):\n",
    "            #Creation of a final_url variable that stores the URL of every repository to download files from using the href property from HTML\n",
    "            final_url = basic_url + a_tag['href']\n",
    "\n",
    "            #If-statement to filter out specific URLs within repositories and 43 is the length of the longest repo name (checked using the len() method)\n",
    "            if len(final_url) > 43 or final_url.endswith(\"/issues\") or final_url.endswith(\"/pulls\") or final_url.endswith(\"/stargazers\") or \"MangoTheCat\" in final_url:\n",
    "                continue\n",
    "            #Else-condition to append the correct URLs to the complete_repo_urls list\n",
    "            else: \n",
    "                complete_repo_urls.append(final_url)\n",
    "\n",
    "#Prompts user for input of a valid file path\n",
    "#Try-except\n",
    "try:\n",
    "    #File path requested from user\n",
    "    file_path = input(\"Please enter a valid file location to download and store the required github files to: \")\n",
    "except:\n",
    "    #Exception message printed\n",
    "    print(\"Invalid filepath. Please enter a valid file path to clone the GitHub repo to.\")\n",
    "\n",
    "#Git cloning to clone the repositories from the complete_repo_urls list\n",
    "for link in complete_repo_urls:\n",
    "    #Link split using the '/' delimiter \n",
    "    split_link_list = link.split(\"/\")\n",
    "    \n",
    "    #Repository names extracted using indexing on the split_link_list\n",
    "    repo_final_name = split_link_list[len(split_link_list) - 1]\n",
    "    \n",
    "    #Repo's clone_from method used here to take in user input as file_path and appended to the repo_final_name string \n",
    "    #The above is done to create respective directories for each cloned repository\n",
    "    #Try-except to see if the repository can be downloaded \n",
    "    try:\n",
    "        Repo.clone_from(link, file_path + \"/\" + repo_final_name)\n",
    "    except git.GitCommandError:\n",
    "        print(\"GitCommandError raised. Could not download the files from the repository at: \" + link)\n",
    "        #Continues in case of the repository not being able to be downloaded/partially downloaded due to file extension errors\n",
    "        continue\n",
    "    except:\n",
    "        print(\"Unidentified exception raised. Could not download the files from the repository at: \" + link)\n",
    "        continue"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.8.3 64-bit",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "aee8b7b246df8f9039afb4144a1f6fd8d2ca17a180786b69acc140d282b71a49"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
