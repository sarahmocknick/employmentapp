# employmentapp


## Setup

Create and activate a virtual environment:

```sh
conda create -n employmentapp python=3.10

conda activate employmentapp


Install packages:

'''sh
pip install -r requirements.txt
'''


##Usage

Register for an app_key and an app_id on adzuna: https://developer.adzuna.com/

#app_key = "2f9346990e80efa58db891b2ed825637"
#app_id = "651392a1"

Run the simple job search:

'''sh
python app/simple-job-search.py
'''



##glitch I found - have to type in a space before typing in the job


Run the complex job search:

'''sh
python app/complex-job-search.py
'''



