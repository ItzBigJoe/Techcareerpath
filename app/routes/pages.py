from flask import Blueprint, render_template
from flask_login import login_required

pages_bp = Blueprint('pages', __name__)

@pages_bp.route('/')
def home():
    return render_template('index.html')

@pages_bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@pages_bp.route('/assessment')
@login_required
def assessment():
    return render_template('assessment.html')

@pages_bp.route('/analyzing')
@login_required
def analyzing():
    return render_template('analyzing.html')

@pages_bp.route('/career')
@login_required
def career():
    return render_template('career.html')

@pages_bp.route('/learning')
@login_required
def learning():
    return render_template('learning.html')