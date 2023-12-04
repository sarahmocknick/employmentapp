from flask import Blueprint, request, render_template, redirect, flash

from app.simple import simple_job_search

simple_routes = Blueprint("simple_routes", __name__)


@simple_routes.route("/simple/dashboard")
def simple_dashboard():
    print("Simple Job Search DASHBOARD...")
    try:
        data = simple_job_search()
        flash("Fetched Simple Job Search Data!", "success")
        return render_template("simple_dashboard.html",
        )
    except Exception as err:
        print('OOPS', err)

        flash("Job Search Data Error. Please try again!", "danger")
        return redirect("/")



@simple_routes.route("/api/simple.json")
def simple_api():
    print("Simple Job Search DATA (API)...")
    try:
        data = simple_job_search()
        return data
    except Exception as err:
        print('OOPS', err)
        return {"message":"Simple Job Search Data Error. Please try again."}, 404

    # We need a route to render the job form function. 
    #form action poihnts to dashboard route 
    #action = "/simple/dashboard" to trigger the dashboard route
    #dashboard route needs to import the fetching function
    #use form inputs passed from the form
    #look at request.form within the route
    #invoke fetching function to get some jobs back
    #pass those jobs to the dashboard page