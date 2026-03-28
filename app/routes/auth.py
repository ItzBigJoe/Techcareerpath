from flask import Blueprint, request, redirect, render_template, session, flash, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user import User
from app.core.extensions import db
from flask_login import login_user, logout_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        if password != confirm_password:
            flash('Passwords do not match.', 'danger')
            return redirect(url_for('auth.register'))
            
        existing_user = User.query.filter_by(email=email).first()
        
        if existing_user:
            flash('Email already registered.', 'danger')
            return redirect(url_for('auth.register'))
            
        user = User()
        user.name = name
        user.email = email
        user.password = generate_password_hash(password)
        
        db.session.add(user)
        db.session.commit()
        
        # Log the user in immediately after successful registration
        login_user(user)
        
        flash('Registration successful! Welcome to JobReady.', 'success')
        return redirect(url_for('pages.profile'))
        
    return render_template('register.html')


@auth_bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()

        if user and check_password_hash(user.password, request.form['password']):
            login_user(user)
            # Reset assessment progress on login
            session.pop('current_question_index', None)
            session.pop('answers', None)
            return redirect(url_for('pages.assessment'))
        else:
            flash('Invalid email or password.', 'danger')

    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    logout_user()
    flash('Logged out successfully.', 'info')
    return redirect(url_for('pages.home'))