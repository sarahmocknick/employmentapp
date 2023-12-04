#SIMPLE JOB QUERY THAT ONLY TAKES ONE INPUT FROM USER
#IMPORTS

import os
from dotenv import load_dotenv
import requests
import json
from getpass import getpass

#ENVIRONMENT VARIABLES AND CONSTANTS

load_dotenv()

user_app_id = os.getenv("APP_ID")
user_app_key = os.getenv("APP_KEY")

#breakpoint()

#quit()


#FUNCTIONS

app_id = getpass("Please input your app id: ")
app_key = getpass("Please input your app key: ")
what = input("What kind of job are you looking for?")

def simple_job_search():
    base_url = "http://api.adzuna.com/v1/api/jobs/gb/search/1"

    params = {
        'app_id': app_id,
        'app_key': app_key,
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

result = simple_job_search()
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



def generate_html_output(results):
    html_output = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Job Search Results</title>
    </head>
    <body>
        <h1>Job Search Results</h1>
        <div>
    '''

    if results and 'results' in results:
        if results['results']:
            html_output += '''
            <table border="1">
                <tr>
                    <th>Job Title</th>
                    <th>Company</th>
                    <th>Location</th>
                    <th>Description</th>
                </tr>
            '''

            for job in results.get('results'):
                html_output += f'''
                <tr>
                    <td>{job.get('title')}</td>
                    <td>{job.get('display_name')}</td>
                    <td>{job.get('area')}</td>
                    <td>{job.get('description')}</td>
                </tr>
                '''

            html_output += '''
            </table>
            '''
        else:
            html_output += '''
            <p>No results found for the specified job query.</p>
            '''

    else:
        html_output += '''
        <p>Error in retrieving job data. Please check your input and try again.</p>
        '''

    html_output += '''
        </div>
    </body>
    </html>
    '''
    return html_output

result = simple_job_search()
html_content = generate_html_output(result)

with open('simple_dashboard.html', 'w') as file:
    file.write(html_content)




