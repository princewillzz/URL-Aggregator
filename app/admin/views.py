

from crypt import methods
from flask import Blueprint, render_template
from flask_login import login_required


mod_admin = Blueprint('admin', __name__, url_prefix='/admin')

@mod_admin.get('/')
@login_required
def admin_dashboard():

    return render_template("admin.html")