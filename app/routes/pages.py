from flask import Blueprint, render_template

pages_bp = Blueprint('pages', __name__)

@pages_bp.route('/')
def home():
    return render_template('index.html')

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

@pages_bp.route('/login')
def login():
    return render_template('login.html')

@pages_bp.route('/admin')
def admin():
    return render_template('admin.html')

@pages_bp.route('/register')
def register():
    return render_template('register.html')