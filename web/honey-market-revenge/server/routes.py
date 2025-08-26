from app import app, Users, Products, db
from flask import render_template
from flask import request
from flask import redirect, abort
from flask import session, jsonify
from flask import make_response, send_from_directory
from sqlalchemy import text
from marshmallow import ValidationError
from settings import *
from validator import *
from bot import visit_website
from sqlalchemy.exc import OperationalError
import uuid
import secrets
import traceback

# Handling errors
@app.errorhandler(404)
def not_found_error(error):
    return render_template('error.html', code="404 - Not Found", err=error), 404
@app.errorhandler(401)
def internal_error(error):
    return render_template('error.html', code="401 - Unauthorized", err=error), 401
@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html', code="500 - Internal Server Error", err=f"Traceback: ...{traceback.format_exc()[-500:]}"), 500


@app.route("/", methods=["GET"])
def index_page():
    
    all = Products.query.filter_by(bestFame=True).all()
    
    return render_template("index.html", products=all)

def sanitize(payload):

    lpayload = payload.strip()
    REPLACEMENT = ["{{", "}}", "'", '"', "`", ";", "+"]
    BLACK_LIST = [ "constructor", "alert", "fetch" ]

    for i in REPLACEMENT:
        if i in lpayload:
            lpayload = lpayload.replace(i, "")

    for i in BLACK_LIST:
        if i in lpayload:
            return None

    return lpayload


@app.route("/products", methods=["GET", "POST"])
def products_page():
    try:
        # Load and validate form data using Marshmallow
        form_data = search_scheme.load(request.args)
    except ValidationError as e:
        return f"Error: {e.messages}", 400

    search = sanitize(form_data['search']) if "search" in form_data else None

    if search:
        ret = Products.query.filter(Products.title.like(f'%{search.strip()}%')).all()
    else:
        ret = Products.query.all()
    
    return render_template("product.html", searchTerm=search if search else '' , products=ret, length=len(ret))

@app.route("/products/<uuid:productID>", methods=["GET"])
def item_page(productID):
    
    prod = Products.query.filter_by(id=productID).first()
    if not prod:
        abort(404)
    
    return render_template("item.html", prod=prod)

@app.route("/admin/login", methods=["GET"])
def admin_login():
    
    if "user" in session:
        return redirect("/admin/profile")
    
    return render_template("login.html")

@app.route("/admin/login", methods=["POST"])
def admin_login_post():

    try:
        form_data = login_scheme.load(request.form.to_dict())
    except ValidationError as e:
        return f"Error: {e.messages}", 400

    username = form_data['username']
    password = form_data['password']
    
    # Extracting the first matched record
    user = Users.query.filter_by(name=username).first()
        
    if user and user.checkPassword(password):
        
        session['user'] = user.name
        session['id'] = user.id

        return redirect('/admin/profile')
    
    return render_template("login.html", is_error=True)

@app.route("/contact/submit", methods=["POST"])
def contact():
    try:
        form_data = submit_scheme.load(request.form.to_dict())
    except ValidationError as e:
        return f"Error: {e.messages}", 400

    url = form_data["url"]

    visit_website(url=url)

    redirect_to = f"{request.headers.get('Referer')}?T=SENT"

    return redirect(redirect_to)

@app.route('/logout', methods=["GET", "POST"])
def logout():
    session.clear()
    return redirect('/')

@app.route("/v1/api/profile/get", methods=["GET", "POST"])
def get_profile():
    
    # returning the profile picture for the admin
    
    if "id" not in session:
        return redirect("/admin/login")
    
    user = Users.query.filter_by(id=session['id']).first()    
    if not user:
        return redirect("/admin/login")

    return send_from_directory(PROFILE_IMAGE_DIR, user.profile_pic)

@app.route("/admin/profile", methods=["GET"])
def admin_profile():
    
    if "id" not in session:
        return redirect("/admin/login")
    
    user = Users.query.filter_by(id=session['id']).first()    
    if not user:
        return redirect("/admin/login")

    return render_template("profile.html", user=user)
