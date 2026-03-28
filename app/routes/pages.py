from flask import Blueprint, render_template, redirect, url_for

pages_bp = Blueprint('pages', __name__)

@pages_bp.route('/')
def home():
    return redirect(url_for('pages.profile'))

@pages_bp.route('/profile')
def profile():
    return render_template('profile.html')

@pages_bp.route('/assessment')
def assessment():
    return render_template('assessment.html')

@pages_bp.route('/analyzing')
def analyzing():
    return render_template('analyzing.html')

@pages_bp.route('/career')
def career():
    return render_template('career.html')

@pages_bp.route('/learning')
def learning():
    return render_template('learning.html')