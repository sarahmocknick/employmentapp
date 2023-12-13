from flask import Blueprint, request, render_template, flash, jsonify, redirect
from app.complex import complex_job_search

complex_routes = Blueprint("complex_routes", __name__)

@complex_routes.route("/complex/dashboard", methods=["GET", "POST"])
def complex_dashboard():
    if request.method == "POST":
        what = request.form.get("what")
        result = complex_job_search(what)

        if not result:
            flash_redirect("Error in retrieving job data. Please check your input and try again.", "danger", what)
            return redirect("/complex/dashboard")

        if is_successful_result(result):
            jobs = result.get('results', [])
            format_jobs(jobs)
            return render_template("complex_dashboard.html", jobs=jobs)

        flash_error(result, what)
        return redirect("/complex/dashboard")

    return render_template("complex_form.html")

def is_successful_result(result):
    return isinstance(result, dict) and 'results' in result

def format_jobs(jobs):
    for job in jobs:
        if job.get('contract_time') == 'full_time':
            job['contract_time'] = 'Full Time'

def flash_redirect(message, category, what):
    flash(message, category)

def flash_error(result, what):
    flash("Error in retrieving job data. Please check your input and try again.", "danger")
    print(f"Error retrieving data for query: {what}")  # Debugging
    if isinstance(result, dict) and 'error' in result:
        print(f"API Error Message: {result['error']}") 

@complex_routes.route("/api/complex.json")
def complex_api():
    try:
        data = complex_job_search()
        return jsonify(data) if data else {"message": "No data found."}, 404
    except Exception as err:
        print('OOPS', err)
        return {"message": "Complex Job Search Data Error. Please try again."}, 404