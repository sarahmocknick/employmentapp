#SIMPLE JOB QUERY THAT ONLY TAKES ONE INPUT FROM USER
#IMPORTS

import os
from dotenv import load_dotenv
import requests
import json
from getpass import getpass

#ENVIRONMENT VARIABLES AND CONSTANTS

load_dotenv()

APP_ID = os.getenv("APP_ID")
APP_KEY = os.getenv("APP_KEY")

#breakpoint()

#quit()


#FUNCTIONS

#app_id = getpass("Please input your app id: ")
#app_key = getpass("Please input your app key: ")


def simple_job_search(what="software developer"):
    base_url = "http://api.adzuna.com/v1/api/jobs/gb/search"

    params = {
        'app_id': APP_ID,
        'app_key': APP_KEY,
        'results_per_page': 20,
        'what': what,
        'content-type': 'application/json'
    }

    r = requests.get(base_url, params=params)

    if r.status_code == 200:
        data = json.loads(r.text)
        return data
    else:
        print(f"Error: {r.status_code}")
        print(r.text)
        return None


if __name__ == "__main__":

    what = input("What kind of job are you looking for?")
    print(what)
    result = simple_job_search(what)
    if result and 'results' in result:
        if result['results']:
            print("Example Result:")
            #print(result)
            for job in result.get('results'):
            #what if there is a case where there are no results/errors?
            #we need to account for this in the code here
                print("Job Title:", job.get('title'))
                print("Company:", job.get('display_name'))
                print("Location:", job.get('area'))
                print("Description:", job.get('description'))
                print("-" * 20)
        else:
            print("No results found for the specified job query.")
    else:
        print("Error in retrieving job data. Please check your input and try again.")








