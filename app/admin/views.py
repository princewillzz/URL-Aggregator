

from flask import Blueprint, redirect, render_template, session, url_for
from flask_login import current_user, login_required
from app.forms.LinkAddForm import LinkAddForm
from app.forms.UserDetailsForm import UserDetailsForm
from app.models.Link import Link
from app import db
from app.models.User import User

from app.auth.views import bcrypt

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


@mod_admin.get("/settings")
@login_required
def settings_view():

    error = session.get('error')
    if error:
        session.pop('error')

    userDetailsForm = UserDetailsForm()


    return render_template(
        "settings.html",
        userForm=userDetailsForm,
        error=error
    )

@mod_admin.post("/details")
@login_required
def update_user_details():

    

    userDetailsForm = UserDetailsForm()

    if userDetailsForm.validate_on_submit():
        user = User.query.get(current_user.id)

        user.bio = userDetailsForm.bio.data
        user.username = userDetailsForm.username.data
        if userDetailsForm.password.data and not (userDetailsForm.password.data == current_user.password):
            hashed_password = bcrypt.generate_password_hash(userDetailsForm.password.data)
            user.password = hashed_password

        db.session.commit()

        
        return redirect(url_for('admin.settings_view'))

    # If errors exist 
    if len(userDetailsForm.username.errors) > 0:
        session['error'] = userDetailsForm.username.errors[0]


    return redirect(
        url_for('admin.settings_view', error=session.get('error')),
    )
