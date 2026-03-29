from flask import Blueprint, render_template, redirect, url_for, session, jsonify, request

pages_bp = Blueprint('pages', __name__)

@pages_bp.route('/')
def home():
    return render_template('index.html')

@pages_bp.route('/profile')
def profile():
    return render_template('profile.html')

@pages_bp.route('/assessment')
def assessment():
    # Check server-side session for profile
    if not session.get('profile_completed'):
        return redirect(url_for('pages.profile'))
    return render_template('assessment.html')

@pages_bp.route('/api/save-profile', methods=['POST'])
def save_profile():
    try:
        profile_data = request.json
        if profile_data and profile_data.get('profileCompleted'):
            session['profile_completed'] = True
            session['user_profile'] = profile_data
            return jsonify({'success': True})
        return jsonify({'success': False, 'error': 'Invalid profile data'}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@pages_bp.route('/analyzing')
def analyzing():
    return render_template('analyzing.html')

@pages_bp.route('/career')
def career():
    return render_template('career.html')

@pages_bp.route('/learning')
def learning():
    return render_template('learning.html')