from app.models.assessment import Assessment
from app.models.result import Result
from app.core.extensions import db
from app.services.ai_service import generate_result
from app.routes.assessment import QUESTIONS

def process_assessment(user_id, answers_dict):
    # answers_dict is { "0": "User Answer", "1": "User Answer", ... }
    
    # Track scores per category
    category_scores = {
        "Soft Skills": {"correct": 0, "total": 5},
        "Frontend": {"correct": 0, "total": 5},
        "Backend": {"correct": 0, "total": 5},
        "AI/Data Science": {"correct": 0, "total": 5},
        "DSA": {"correct": 0, "total": 5}
    }
    
    correct_total = 0
    missed_categories = []

    for i, q in enumerate(QUESTIONS):
        user_answer = answers_dict.get(str(i)) or answers_dict.get(i)
        is_correct = user_answer == q['answer']
        
        category = q['category']
        if is_correct:
            correct_total += 1
            category_scores[category]["correct"] += 1
        else:
            missed_categories.append(category)

    # Calculate percentages
    readiness_score = int((correct_total / total_questions) * 100)
    
    # Detailed category percentages
    calculated_skills = {}
    for cat, stats in category_scores.items():
        calculated_skills[cat] = int((stats["correct"] / stats["total"]) * 100)

    # Legacy keys for backward compatibility with existing UI if needed
    soft_skills_score = calculated_skills["Soft Skills"]
    tech_correct = sum(category_scores[c]["correct"] for c in category_scores if c != "Soft Skills")
    technical_skills_score = int((tech_correct / 20) * 100)

    # Prepare data for AI analysis
    ai_input = {
        "overall_score": readiness_score,
        "category_scores": calculated_skills,
        "missed_topics": list(set(missed_categories)),
        "user_answers": answers_dict
    }
    
    try:
        ai_result = generate_result(ai_input)
    except Exception:
        ai_result = {
            "career": "Software Engineer",
            "gaps": [f"Improve knowledge in: {', '.join(list(set(missed_categories))[:3])}"]
        }

    result = Result()
    result.user_id = user_id
    result.career = ai_result.get('career', 'Software Engineer')
    result.score = readiness_score
    
    # Store all detailed scores in the skills dictionary
    result.skills = {
        "Readiness": readiness_score,
        "Soft Skills": soft_skills_score,
        "Technical": technical_skills_score,
        **calculated_skills
    }
    result.gaps = ai_result.get('gaps', [])

    db.session.add(result)
    db.session.commit()
    
    return result

    return result