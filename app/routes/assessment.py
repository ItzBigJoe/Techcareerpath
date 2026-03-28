from flask import Blueprint, request, jsonify, session
from flask_login import current_user, login_required
from app.services.assessment_service import process_assessment
from app.models.result import Result

assessment_bp = Blueprint('assessment', __name__)

# Dummy questions for demonstration
QUESTIONS = [
    {"id": 1, "text": "How much experience do you have with programming? (Beginner, Intermediate, Advanced)"},
    {"id": 2, "text": "Which programming languages are you most comfortable with?"},
    {"id": 3, "text": "Have you ever worked with any web frameworks like Flask or Django?"},
    {"id": 4, "text": "What is your level of understanding of database management systems?"},
    {"id": 5, "text": "How comfortable are you with using Git for version control?"},
    {"id": 6, "text": "Do you have any experience with cloud platforms like AWS or Azure?"},
    {"id": 7, "text": "How would you rate your problem-solving and algorithmic skills?"},
    {"id": 8, "text": "What kind of projects have you worked on in the past?"},
    {"id": 9, "text": "Which tech career path interests you the most and why?"},
    {"id": 10, "text": "How many hours per week can you dedicate to learning new skills?"}
]

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

    result = process_assessment(current_user.id, answers)
    
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