from flask import Blueprint, request, render_template, flash, jsonify, redirect
from app.simple import simple_job_search

simple_routes = Blueprint("simple_routes", __name__)

@simple_routes.route("/simple/dashboard", methods=["GET", "POST"])
def simple_dashboard():
    if request.method == "POST":
        what = request.form.get("what")
        result = simple_job_search(what)

        if result is None:
            flash_redirect("Error in retrieving job data. Please check your input and try again.", "danger", what)
            return redirect("/simple/dashboard")

        if is_successful_result(result):
            jobs = result['results']
            if jobs:
                return render_template("simple_dashboard.html", jobs=jobs)

            flash_no_results(what)
        else:
            flash_error(result, what)

        return redirect("/simple/dashboard")

    return render_template("simple_form.html")

def is_successful_result(result):
    return isinstance(result, dict) and 'results' in result

def flash_redirect(message, category, what):
    flash(message, category)

def flash_error(result, what):
    flash("Error in retrieving job data. Please check your input and try again.", "danger")
    print(f"Error retrieving data for query: {what}")  # Debugging
    if isinstance(result, dict) and 'error' in result:
        print(f"API Error Message: {result['error']}") 

def flash_no_results(what):
    flash("No results found for the specified job query.", "warning")
    print(f"API returned empty results for query: {what}")  # Debugging

@simple_routes.route("/api/simple.json")
def simple_api():
    try:
        data = simple_job_search()
        if data is not None:
            return jsonify(data)
        return {"message": "No data found."}, 404
    except Exception as err:
        print('OOPS', err)
        return {"message": "Simple Job Search Data Error. Please try again."}, 404

    # We need a route to render the job form function. 
    #form action poihnts to dashboard route 
    #action = "/simple/dashboard" to trigger the dashboard route
    #dashboard route needs to import the fetching function
    #use form inputs passed from the form
    #look at request.form within the route
    #invoke fetching function to get some jobs back
    #pass those jobs to the dashboard page