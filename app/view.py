

from flask import Blueprint, redirect, render_template, url_for

from app.models.User import User

mod_home = Blueprint('home', __name__, url_prefix='/')

@mod_home.get("/")
def home():
    return redirect(url_for("admin.admin_dashboard"))

@mod_home.get("/<username>")
def userInfo(username):

    existing_user = User.query.filter_by(
            username=username
        ).first()
    
    if not existing_user:
        return "404"
    print(existing_user.links)

    return render_template("admin.html", links=existing_user.links)
