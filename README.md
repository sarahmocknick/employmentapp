# Employment App


## Setup

Create and activate a virtual environment:

```sh
conda create -n employmentapp python=3.10

conda activate employmentapp
```
Obtain an [API Key from Alphavantage](https://www.alphavantage.co/support/#api-key) or from the prof (`ALPHAVANTAGE_API_KEY`).

Create a ".env" file and paste in the following contents:
```sh
# this is the ".env" file...
You must first follow the [setup instructions](https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/sendgrid.md) to create an account, verify your account, setup a single sender, and obtain an API Key.

ALPHAVANTAGE_API_KEY="_______"
```
SENDGRID_ID="________"

## Usage

### Web App

Run the web app (then view in the browser at https://localhost:5000/):

```sh

#Mac OS:

FLASK_APP=web_app flask run

#Windows OS:

export FLASK_APP=web_app
flask run
```

Install packages:
```sh

pip install -r requirements.txt
```

Run the simple job search:

```sh
python -m app.simple
```
##glitch I found - have to type in a space before typing in the job

Run the complex job search:

```sh
python -m app.complex
```
## Testing
```sh
pytest
```







