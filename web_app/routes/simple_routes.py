from flask import Blueprint, render_template, flash

from app.simple import fetch_data  # Adjust the import path based on your file structure

simple_routes = Blueprint("simple_routes", __name__)


@simple_routes.route("/simple/dashboard")
def simple_dashboard():
    print("SIMPLE JOB SEARCH DASHBOARD...")
    # Fetch job data using the provided function
    results = fetch_data()
    if results:
        return render_template("results.html", results=results)
    else:
        flash("Error fetching job data", "error")
        return render_template("error.html")


@simple_routes.route("/api/simple.json")
def simple_api():
    print("SIMPLE JOB SEARCH DATA (API)...")
    # Similar logic to fetch job data, can return JSON if needed
    results = fetch_data()
    if results:
        return {"results": results}
    else:
        return {"error": "Error fetching job data"}