from app.models.assessment import Assessment
from app.models.result import Result
from app.core.extensions import db
from app.core.questions import QUESTIONS
from app.services.career_algorithm import match_career_v2

def process_assessment(user_id, answers_dict):
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
    total_questions = len(QUESTIONS)
    user_skills_dict = {} # Task 12: Dictionary for advanced metrics

    # Map question keywords to dataset skills
    skill_mapping = {
        "flexbox": "CSS",
        "React Hooks": "React Hooks",
        "Largest heading": "HTML",
        "Responsive Web Design": "Responsive Design",
        "element to the end": "JavaScript",
        "RESTful API": "RESTful API",
        "SELECT": "SQL",
        "Middleware": "Middleware",
        "Hashing": "Hashing",
        "404": "HTTP Status Codes",
        "Supervised Learning": "Machine Learning", # Updated mapping
        "Overfitting": "Machine Learning",
        "NumPy": "NumPy",
        "NLP": "NLP",
        "Confusion Matrix": "Machine Learning",
        "Hash Table": "Linked List", # Best fit mapping
        "FIFO": "Linked List",
        "Binary Search": "Python Scripting",
        "shortest path": "Python Scripting",
        "linked list": "Linked List"
    }

    for i, q in enumerate(QUESTIONS):
        user_answer = answers_dict.get(str(i)) or answers_dict.get(i)
        is_correct = user_answer == q['answer']
        
        category = q['category']
        if is_correct:
            correct_total += 1
            category_scores[category]["correct"] += 1
            
            # Map correct answer to dataset skill
            for keyword, skill in skill_mapping.items():
                if keyword.lower() in q['text'].lower():
                    # Set proficiency based on correctness
                    # If correct, give 100% for that sub-skill for scoring purposes
                    user_skills_dict[skill] = 100
        else:
            missed_categories.append(category)

    # Readiness Score (Overall)
    readiness_score = int((correct_total / total_questions) * 100) if total_questions > 0 else 0
    
    # Category percentages
    calculated_skills = {}
    for cat, stats in category_scores.items():
        calculated_skills[cat] = int((stats["correct"] / stats["total"]) * 100)

    # Task 12: ALGORITHM-BASED COMPREHENSIVE MATCHING
    rankings = match_career_v2(user_skills_dict)
    top_career, rank_score, metrics = rankings[0]

    result = Result()
    result.user_id = user_id
    result.career = top_career
    result.score = readiness_score
    
    # Store all detailed scores and metrics
    result.skills = {
        "Readiness": readiness_score,
        "Domain Fit": metrics["domain_fit"],
        "Tag Similarity": metrics["tag_similarity"],
        **calculated_skills
    }
    
    # Store structured gaps and resources
    result.gaps = {
        "missing": metrics["missing_skills"],
        "weak": metrics["weak_skills"],
        "resources": metrics["resources"]
    }

    db.session.add(result)
    db.session.commit()
    
    return result