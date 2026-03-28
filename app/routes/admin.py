from flask import Blueprint, render_template
from app.models.user import User
from app.models.result import Result

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin')
def admin():
    users = User.query.all()
    results = Result.query.all()

    return render_template("admin.html", users=users, results=results)