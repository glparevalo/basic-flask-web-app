# =========== IMPORTS ===========  

from flask import render_template
from flask_login import login_required, current_user
from . import main

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)
