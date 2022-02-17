

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
    

    errorMsg = None
    links = []
    userinfo = None

    if not existing_user:
        errorMsg = "User Not Found!!"
    else:
        links = existing_user.links
        userinfo = {
            'email': existing_user.email,
            'username': existing_user.username
        }

    return render_template("profile.html", links=links, userinfo=userinfo, errorMsg=errorMsg)
