#COMPLEX JOB QUERY THAT TAKES MORE INFORMATION

import os
app_id = os.getenv("APP_ID")


import requests
import json
from getpass import getpass

app_id = getpass("Please input your app id: ")
app_key = getpass("Please input your app key: ")

#app_key = "2f9346990e80efa58db891b2ed825637"
#app_id = "651392a1"

what = input("What kind of job are you looking for?: ")
salary_pref = input("Do you have a preference for a salary minumum? Please type yes or no: ").lower()

if(salary_pref == "yes"):
    salary_min = int(input("What is your preferred salary minimum in euros?: "))
else:
    salary_min = 0

full_time_query = input("Do you want a full time job? Please type yes or no: ").lower()
permanent_query = input("Do you want a permanent job? Please type yes or no: ").lower()


if(full_time_query == "yes"):
    full_time = 1;
else:
    full_time = 0;

if(permanent_query == 0):
    permanent = 1
else:
    permanent = 0

#should ask for salary requirement? and availability?

def complex_job_search(where=None, what_exclude=None):
    base_url = "http://api.adzuna.com/v1/api/jobs/gb/search/1"

    params = {
        'app_id': app_id,
        'app_key': app_key,
        'results_per_page': 20,
        'what': what,
        'where': 'london',
        'sort_by': 'salary',
        'salary_min': salary_min,
        'full_time': full_time,
        'permanent': permanent,
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

result = complex_job_search()
if result and any(result["results"]):
    #print(result)
    for job in result.get('results'):
    #what if there is a case where there are no results/errors?
    #we need to account for this in the code here
        print("Job Title:", job.get('title'))
        print("Company:", job["company"]["display_name"])
        print("Location:", job["location"]["display_name"])
        print("Salary:", job.get('salary_min'))
        print("Availability:", job.get('contract_time'))
        print("Description:", job.get('description'))
        print("-" * 20)
else:
    print("Oops! We couldn't find any jobs that met your specifications. Try again!")