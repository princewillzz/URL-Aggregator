

from crypt import methods
from os import link
from turtle import title
from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from itsdangerous import json
from app.forms.LinkAddForm import LinkAddForm
from app.models.Link import Link
from app import db

mod_admin = Blueprint('admin', __name__, url_prefix='/admin')

@mod_admin.post("/link")
@login_required
def add_link():
    
    form = LinkAddForm()
    
    if form.validate_on_submit():
        new_link = Link(title=form.title.data, link=form.link.data, user_id=current_user.id)
        db.session.add(new_link)
        db.session.commit()

    return redirect(url_for('admin.admin_dashboard'))


@mod_admin.delete("/link/<int:linkId>")
@login_required
def delete_link(linkId):
    print(linkId)

    link = Link.query.get(linkId)
    if link:
        db.session.delete(link)
        db.session.commit()


    return {
        'message': "successfully deleted!!"
    }, 200

    
@mod_admin.get('/')
@login_required
def admin_dashboard():

    form = LinkAddForm()

    links = Link.query.all()

    return render_template("admin.html", links=links, form=form)

