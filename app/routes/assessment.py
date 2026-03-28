from flask import Blueprint, request, jsonify, session
from flask_login import current_user, login_required
from app.services.assessment_service import process_assessment
from app.models.result import Result
from app.core.questions import QUESTIONS

assessment_bp = Blueprint('assessment', __name__)

@assessment_bp.route('/api/current-question', methods=['GET'])
@login_required
def get_current_question():
    current_index = session.get('current_question_index', 0)
    
    if current_index >= len(QUESTIONS):
        return jsonify({"finished": True})
        
    return jsonify({
        "question": QUESTIONS[current_index],
        "current": current_index + 1,
        "total": len(QUESTIONS)
    })

@assessment_bp.route('/api/next-question', methods=['POST'])
@login_required
def next_question():
    data = request.json
    answer = data.get('answer')
    
    if 'answers' not in session:
        session['answers'] = []
    
    current_index = session.get('current_question_index', 0)
    
    # Store or update the answer
    answers = session['answers']
    if current_index < len(answers):
        answers[current_index] = answer
    else:
        answers.append(answer)
    session['answers'] = answers
    
    # Increment index
    session['current_question_index'] = current_index + 1
    
    finished = session['current_question_index'] >= len(QUESTIONS)
    
    return jsonify({
        "success": True,
        "finished": finished
    })

@assessment_bp.route('/api/previous-question', methods=['POST'])
@login_required
def previous_question():
    current_index = session.get('current_question_index', 0)
    
    if current_index > 0:
        session['current_question_index'] = current_index - 1
        return jsonify({"success": True})
    
    return jsonify({"error": "Already at the first question"}), 400

@assessment_bp.route('/api/submit', methods=['POST'])
@login_required
def submit():
    answers = session.get('answers', [])
    
    if not answers:
        return jsonify({"error": "No answers provided"}), 400

    # Convert session list to dict for processing
    answers_dict = {str(i): ans for i, ans in enumerate(answers)}
    
    result = process_assessment(current_user.id, answers_dict)
    
    # Clear session after submission
    session.pop('current_question_index', None)
    session.pop('answers', None)

    return jsonify({
        "career": result.career,
        "score": result.score,
        "skills": result.skills,
        "gaps": result.gaps
    })

@assessment_bp.route('/api/result', methods=['GET'])
@login_required
def get_result():
    # Get the latest result for the current user
    result = Result.query.filter_by(user_id=current_user.id).order_by(Result.id.desc()).first()
    
    if not result:
        return jsonify({"error": "No result found"}), 404
        
    return jsonify({
        "career": result.career,
        "score": result.score,
        "skills": result.skills,
        "gaps": result.gaps
    })