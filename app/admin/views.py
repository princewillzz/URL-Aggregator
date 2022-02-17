

from crypt import methods
from distutils.log import error
from os import link
from turtle import title
from flask import Blueprint, redirect, render_template, request, session, url_for
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


    session['error'] = form.link.errors and form.link.errors[0]

    return redirect(url_for('admin.admin_dashboard', error=session['error']))


@mod_admin.delete("/link/<int:linkId>")
@login_required
def delete_link(linkId):

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
    error = session.get('error')
    
    if error: 
        session.pop('error')

    form = LinkAddForm()

    links = Link.query.all()

    return render_template("admin.html", links=links, form=form, errorMsg=error)

