from flask import Blueprint, request, render_template, redirect, flash

from app.complex import fetch_data

complex_routes = Blueprint("complex_routes", __name__)


@complex_routes.route("/complex/dashboard")
def complex_dashboard():
    print("Complex Job Search DASHBOARD...")





@complex_routes.route("/api/complex.json")
def simple_api():
    print("Complex Job Search DATA (API)...")