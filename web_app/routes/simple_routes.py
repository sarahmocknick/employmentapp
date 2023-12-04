from flask import Blueprint, request, render_template, redirect, flash

from app.simple import fetch_data

simple_routes = Blueprint("simple_routes", __name__)


@simple_routes.route("/simple/dashboard")
def simple_dashboard():
    print("Simple Job Search DASHBOARD...")





@simple_routes.route("/api/simple.json")
def simple_api():
    print("Simple Job Search DATA (API)...")