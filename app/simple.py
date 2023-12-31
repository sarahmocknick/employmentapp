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
#test for error with request using HTTPError instead of 202 - used ChatGPT to fix this!
def simple_job_search(what="Software Developer"):
    base_url = "http://api.adzuna.com/v1/api/jobs/gb/search/1"

    params = {
        'app_id': APP_ID,
        'app_key': APP_KEY,
        'results_per_page': 20,
        'what': what,
        'content-type': 'application/json'
    }

    try:
        r = requests.get(base_url, params=params)
        r.raise_for_status()  # Raise an HTTPError for bad responses
        data = r.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":

    what = input("What kind of job are you looking for?")
    print(what)
    result = simple_job_search(what)
    #if result and 'results' in result:
            #print(result)
    if result and any(result["results"]):
    #print(result)
        for job in result.get('results'):
            capitalized_title = job.get('title').title()

            print("Job Title:", capitalized_title)
            print("Company:", job["company"]["display_name"])
            print("Location:", job["location"]["display_name"])
            print("Description:", job.get('description'))
            print("-" * 20)
    else:
            print("No results found for the specified job query.")
else:
        print("Error in retrieving job data. Please check your input and try again.")



