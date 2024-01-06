from flask import Blueprint, render_template, request, redirect, url_for
from .model import Passwords
from . import db

views = Blueprint("views", __name__)

@views.route("/")
def index():
    return render_template("index.html")

@views.route("/dataView/")
def viewAll():
    password = Passwords.query.all()
    return render_template("view.html", password=password)

@views.route("/dataMng/")
def mngData():
    return render_template("manage.html")

@views.route("/dataMng/add", methods = ["POST"])
def addPass():
    website = request.form.get("website")
    email = request.form.get("email")
    password = request.form.get("password")
    addData = Passwords(website=website, email=email, password=password)
    db.session.add(addData)
    db.session.commit()
    print("Data successfully added to database.")
    return redirect(url_for("views.mngData"))

@views.route("/dataMng/search", methods=["POST"])
def search():
    err = None
    website = request.form.get("search")
    if not website:
        err = "Search bar is empty."
    else:
        results = Passwords.query.filter(Passwords.website.ilike(f"%{website}")).all()
        if not results:
            err = f"{website} does not exist."
        else:
            return render_template("manage.html", results=results)
    return render_template("manage.html", err=err)

@views.route("/dataMng/update", methods = ["GET", "POST"])
def updatePass():
    id = Passwords.query.filter_by(id = request.form.get("id")).first()
    website = request.form.get("website")
    email = request.form.get("email")
    password = request.form.get("password")

    id.website = website
    id.email = email
    id.password = password
    db.session.commit()
    print("Data update successful.")
    return redirect(url_for("views.mngData"))

@views.route("/dataMng/delete/<id>")
def deletePass(id):
    pword = Passwords.query.get(id)
    db.session.delete(pword)
    db.session.commit()
    print("Data deletion successful.")
    return redirect(url_for("views.viewAll"))
