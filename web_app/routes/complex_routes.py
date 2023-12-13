from flask import Blueprint, request, render_template, flash, jsonify, redirect
from app.complex import complex_job_search

complex_routes = Blueprint("complex_routes", __name__)

@complex_routes.route("/complex/dashboard", methods=["GET", "POST"])
def complex_dashboard():
    if request.method == "POST":
        what = request.form.get("what")
        result = complex_job_search(what)

        if result is None:
            flash_redirect("Error in retrieving job data. Please check your input and try again.", "danger", what)

        if isinstance(result, dict) and 'results' in result:
            jobs = result['results']
            if jobs:
                for job in jobs:
                    if job.get('contract_time') == 'full_time':
                        job['contract_time'] = 'Full Time'
                return render_template("complex_dashboard.html", jobs=jobs)

            flash("No results found for the specified job query.", "warning")
            print(f"API returned empty results for query: {what}")  # Debugging
        else:
            flash_error(result, what)

        return redirect("/complex/dashboard")  # Redirect to the form

    return render_template("complex_form.html")  # Display the form initially

def flash_redirect(message, category, what):
    flash(message, category)
    return redirect("/complex/dashboard")

def flash_error(result, what):
    flash("Error in retrieving job data. Please check your input and try again.", "danger")
    print(f"Error retrieving data for query: {what}")  # Debugging
    if isinstance(result, dict) and 'error' in result:
        print(f"API Error Message: {result['error']}") 

@complex_routes.route("/api/complex.json")
def complex_api():
    try:
        data = complex_job_search()
        if data is not None:
            return jsonify(data)
        return {"message": "No data found."}, 404
    except Exception as err:
        print('OOPS', err)
        return {"message": "Complex Job Search Data Error. Please try again."}, 404