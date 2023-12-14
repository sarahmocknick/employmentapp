#this is the complex_routes.py


from flask import Blueprint, request, render_template, flash, jsonify, redirect

from app.complex import complex_job_search

complex_routes = Blueprint("complex_routes", __name__)

@complex_routes.route("/complex/dashboard", methods=["GET", "POST"])
def complex_dashboard():
    if request.method == "POST":
        what = request.form.get("what")
        salary_pref = request.form.get("salary_pref").lower()  # Ensure it's in lowercase for easier comparison
        # Check the salary_pref string to determine the minimum salary
        if salary_pref == "yes":
            try:
                salary_min = int(request.form.get("salary_min"))  # Convert salary_min to integer
            except (ValueError, TypeError):
                salary_min = 0
        else:
            salary_min = 0
        result = complex_job_search(what, salary_min=salary_min)

        if not result:
            flash_redirect("Error in retrieving job data. Please check your input and try again.", "danger", what)
            return redirect("/complex/dashboard")

        if is_successful_result(result):
            jobs = result.get('results', [])
            format_jobs(jobs)

            # Filter jobs based on salary_min
            filtered_jobs = [job for job in jobs if (job.get('salary_min', 0) >= salary_min) or (job.get('salary_max', 0) >= salary_min)]

            return render_template("complex_dashboard.html", jobs=filtered_jobs)

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