#COMPLEX JOB QUERY THAT TAKES MORE INFORMATION
##IMPORTS
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

 

def complex_job_search(what="Software Developer", where="london", salary_min=0, full_time=1, permanent=1):
    base_url = "http://api.adzuna.com/v1/api/jobs/gb/search/1"

    params = {
        'app_id': APP_ID,
        'app_key': APP_KEY,
        'results_per_page': 20,
        'what': what,
        'where': where,
        'sort_by': 'salary',
        'salary_min': salary_min,
        'full_time': full_time,
        'permanent': permanent,
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
    salary_pref = input("Do you have a preference for a salary minumum? Please type yes or no: ").lower()

    if(salary_pref == "yes"):
        salary_min = int(input("What is your preferred salary minimum in euros?: "))
    else:
        salary_min = 0

    full_time_query = input("Do you want a full time job? Please type yes or no: ").lower()
    permanent_query = input("Do you want a permanent job? Please type yes or no: ").lower()


    if full_time_query == "yes":
        full_time = 1
    else:
        full_time = "Part Time"

    if(permanent_query == 0):
        permanent = 1
    else:
        permanent = 0
        print(what)
    result = complex_job_search()
    if result and any(result["results"]):
        #print(result)
        for job in result.get('results'):
            print("Job Title:", job.get('title'))
            print("Company:", job["company"]["display_name"])
            print("Location:", job["location"]["display_name"])
            print("Salary:", job.get('salary_min'))
            availability = job.get('contract_time')
            availability = availability.replace("_", " ")
            print("Availability:", availability)
            print("Description:", job.get('description'))
            print("-" * 20)
    else:
        print("Oops! We couldn't find any jobs that met your specifications. Try again!")
