from app.models.assessment import Assessment
from app.models.result import Result
from app.core.extensions import db
from app.services.ai_service import generate_result

def process_assessment(user_id, answers):
    result_data = generate_result(answers)

    result = Result()
    result.user_id = user_id
    result.career = result_data['career']
    result.score = result_data['score']
    result.skills = result_data['skills']
    result.gaps = result_data['gaps']

    db.session.add(result)
    db.session.commit()

    return result