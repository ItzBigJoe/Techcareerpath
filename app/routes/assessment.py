from flask import Blueprint, request, jsonify, session, send_file
from app.services.assessment_service import process_assessment
from app.models.result import Result
from app.core.questions import QUESTIONS
import io

assessment_bp = Blueprint('assessment', __name__)

def get_pdf_class():
    """Lazily import FPDF to avoid startup errors if the library is missing."""
    try:
        from fpdf import FPDF # type: ignore
        return FPDF
    except ImportError:
        return None

@assessment_bp.route('/api/download-report', methods=['GET'])
def download_report():
    # Get the latest result
    result = Result.query.order_by(Result.id.desc()).first()
    
    if not result:
        return jsonify({"error": "No assessment result found. Please complete an assessment first."}), 404
        
    # Generate PDF
    FPDF_Class = get_pdf_class()
    if not FPDF_Class:
        return jsonify({"error": "PDF generation library (fpdf2) is not installed on the server."}), 500
        
    pdf = FPDF_Class()
    pdf.add_page()
    
    # Title
    pdf.set_font("Helvetica", 'B', 24)
    pdf.set_text_color(45, 75, 143) # #2d4b8f
    pdf.cell(0, 20, "JobReady Career Report", border=0, ln=1, align='C')
    pdf.ln(10)
    
    # Career Recommendation
    pdf.set_draw_color(221, 221, 221)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(10)
    
    pdf.set_font("Helvetica", 'B', 18)
    pdf.cell(0, 10, "Recommended Career Path", border=0, ln=1)
    pdf.set_font("Helvetica", 'B', 20)
    pdf.set_text_color(61, 180, 255) # #3db4ff
    pdf.cell(0, 15, result.career, border=0, ln=1)
    pdf.ln(5)
    
    # Readiness Score
    pdf.set_font("Helvetica", 'B', 16)
    pdf.set_text_color(51, 51, 51)
    pdf.cell(0, 10, f"Overall Readiness Score: {result.score}%", border=0, ln=1)
    
    # Advanced Metrics (Task 7 & 11)
    domain_fit = result.skills.get("Domain Fit", 0)
    tag_similarity = result.skills.get("Tag Similarity", 0)
    
    pdf.set_font("Helvetica", '', 12)
    pdf.cell(100, 10, f"Domain Fit: {domain_fit}%", border=0, ln=0)
    pdf.cell(0, 10, f"Tag Similarity: {tag_similarity}%", border=0, ln=1)
    pdf.ln(10)
    
    # Skill Breakdown
    pdf.set_font("Helvetica", 'B', 18)
    pdf.cell(0, 10, "Skill Breakdown", border=0, ln=1)
    pdf.ln(5)
    
    pdf.set_font("Helvetica", '', 14)
    # Filter out metrics from breakdown
    metric_keys = ["Readiness", "Domain Fit", "Tag Similarity", "Technical", "Soft Skills"]
    for skill, value in result.skills.items():
        if skill in metric_keys: continue
        pdf.cell(100, 10, f"{skill}:", border=0, ln=0)
        pdf.cell(0, 10, f"{value}%", border=0, ln=1)
        
    pdf.ln(10)
    
    # Advanced Skill Gaps (Task 8 & 10)
    if isinstance(result.gaps, dict):
        missing = result.gaps.get("missing", [])
        weak = result.gaps.get("weak", [])
        resources = result.gaps.get("resources", {})
        
        if missing or weak:
            pdf.set_font("Helvetica", 'B', 18)
            pdf.cell(0, 10, "Skill Gaps & Actionable Learning Path", border=0, ln=1)
            pdf.ln(5)
            
            if missing:
                pdf.set_font("Helvetica", 'B', 14)
                pdf.set_text_color(198, 40, 40) # Red
                pdf.cell(0, 10, "Critical Missing Skills:", border=0, ln=1)
                pdf.set_font("Helvetica", '', 11)
                pdf.set_text_color(51, 51, 51)
                for skill in missing:
                    pdf.multi_cell(0, 8, f"- {skill}", border=0, align='L')
                    if skill in resources:
                        pdf.set_font("Helvetica", 'I', 10)
                        pdf.set_text_color(100, 100, 100)
                        pdf.multi_cell(0, 6, f"  Resources: {', '.join(resources[skill])}", border=0, align='L')
                        pdf.set_font("Helvetica", '', 11)
                        pdf.set_text_color(51, 51, 51)
                pdf.ln(5)
                
            if weak:
                pdf.set_font("Helvetica", 'B', 14)
                pdf.set_text_color(249, 168, 37) # Yellow
                pdf.cell(0, 10, "Skills to Improve:", border=0, ln=1)
                pdf.set_font("Helvetica", '', 11)
                pdf.set_text_color(51, 51, 51)
                for skill in weak:
                    pdf.multi_cell(0, 8, f"- {skill}", border=0, align='L')
                    if skill in resources:
                        pdf.set_font("Helvetica", 'I', 10)
                        pdf.set_text_color(100, 100, 100)
                        pdf.multi_cell(0, 6, f"  Resources: {', '.join(resources[skill])}", border=0, align='L')
                        pdf.set_font("Helvetica", '', 11)
                        pdf.set_text_color(51, 51, 51)
    else:
        # Legacy gaps fallback
        if result.gaps:
            pdf.set_font("Helvetica", 'B', 18)
            pdf.cell(0, 10, "Skill Gaps & Areas for Improvement", border=0, ln=1)
            pdf.ln(5)
            pdf.set_font("Helvetica", '', 12)
            for gap in result.gaps:
                pdf.multi_cell(0, 10, f"- {gap}", border=0, align='L')
            
    pdf.ln(20)
    pdf.set_font("Helvetica", 'I', 10)
    pdf.set_text_color(136, 136, 136)
    pdf.cell(0, 10, "Generated by JobReady AI Career Assessment Platform", border=0, ln=1, align='C')
    
    # Output PDF to memory
    output = io.BytesIO()
    pdf_content = pdf.output(dest='S')
    output.write(pdf_content)
    output.seek(0)
    
    return send_file(
        output,
        mimetype='application/pdf',
        as_attachment=True,
        download_name="JobReady_Career_Report.pdf"
    )

@assessment_bp.route('/api/current-question', methods=['GET'])
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
def next_question():
    data = request.json
    answer = data.get('answer')
    
    if 'answers' not in session:
        session['answers'] = []
    
    current_index = session.get('current_question_index', 0)
    
    # Store or update the answer
    answers = list(session['answers']) # Ensure it's a list
    if current_index < len(answers):
        answers[current_index] = answer
    else:
        # Pad with None if somehow the index jumped
        while len(answers) < current_index:
            answers.append(None)
        answers.append(answer)
    session['answers'] = answers
    
    # Increment index
    session['current_question_index'] = current_index + 1
    
    finished = session['current_question_index'] >= len(QUESTIONS)
    
    # Proactively process assessment if finished to avoid race conditions
    if finished:
        answers_dict = {str(i): ans for i, ans in enumerate(answers)}
        process_assessment("anonymous", answers_dict) # Using "anonymous" as session_id
        # Clear session after submission
        session.pop('current_question_index', None)
        session.pop('answers', None)
    
    return jsonify({
        "success": True,
        "finished": finished
    })

@assessment_bp.route('/api/previous-question', methods=['POST'])
def previous_question():
    current_index = session.get('current_question_index', 0)
    
    if current_index > 0:
        session['current_question_index'] = current_index - 1
        return jsonify({"success": True})
    
    return jsonify({"error": "Already at the first question"}), 400

@assessment_bp.route('/api/submit', methods=['POST'])
def submit():
    # This is now a backup or manual trigger, primary submission happens in next_question
    answers = session.get('answers', [])
    
    if not answers:
        # Check if we already have a result from the pro-active submission
        result = Result.query.order_by(Result.id.desc()).first()
        if result:
            return jsonify({
                "career": result.career,
                "score": result.score,
                "skills": result.skills,
                "gaps": result.gaps
            })
        return jsonify({"error": "No answers provided"}), 400

    # Convert session list to dict for processing
    answers_dict = {str(i): ans for i, ans in enumerate(answers)}
    
    result = process_assessment(1, answers_dict) # Using anonymous user ID 1
    
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
def get_result():
    # Get the latest result
    result = Result.query.order_by(Result.id.desc()).first()
    
    if not result:
        return jsonify({"error": "No assessment result found"}), 404
        
    return jsonify({
        "career": result.career,
        "score": result.score,
        "skills": result.skills,
        "gaps": result.gaps
    })