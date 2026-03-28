# Comprehensive Career Matching Algorithm Data and Logic
# Based on files 1.py, 2.py, 3.ipynb, 4.py, and 5.py

# Task 7-12: Unified Data Structure
# Format: { Career: [ (Skill, Domain, Weight, Threshold, Level, [Resources], [Tags]) ] }
CAREER_SKILLS_ADVANCED = {
    "Data Engineer": [
        ("REST Concepts", "APIs & Integration", 0.021739, 60, "Intermediate", 
         ["YouTube: Beginner tutorial series", "Documentation: Official docs + examples", "Practice: Build a mini-project task"], ["ETL", "Warehouse", "Streaming"]),
        ("Unit Testing", "Quality & Testing", 0.021739, 40, "Beginner", 
         ["YouTube: Beginner tutorial series", "Documentation: Official docs + examples", "Practice: Build a mini-project task"], ["ETL", "Warehouse", "Streaming"]),
        ("Data Modeling", "Foundations", 0.021739, 65, "Intermediate", 
         ["SQL Basics", "Normalization Guide", "Practice: Schema Design"], ["Database", "SQL"]),
        ("Python Scripting", "Programming", 0.021739, 60, "Intermediate", 
         ["Python Docs", "Automation Basics", "Practice: ETL Script"], ["Python", "Automation"]),
        ("CI/CD Basics", "Delivery & Ops", 0.021739, 40, "Beginner", 
         ["GitHub Actions Guide", "Docker Basics", "Practice: CI Pipeline"], ["DevOps", "CI/CD"])
    ],
    "AI Engineer": [
        ("Debugging Basics", "Foundations", 0.021739, 60, "Intermediate", 
         ["YouTube: Beginner tutorial series", "Documentation: Official docs + examples", "Practice: Build a mini-project task"], ["AI", "Model", "Inference"]),
        ("Machine Learning", "AI & ML", 0.021739, 75, "Advanced", 
         ["Andrew Ng Course", "Scikit-Learn Docs", "Practice: Train a Model"], ["AI", "ML", "Python"]),
        ("Neural Networks", "Deep Learning", 0.021739, 80, "Advanced", 
         ["Deep Learning Specialization", "PyTorch Docs", "Practice: Build a CNN"], ["AI", "Deep Learning"]),
        ("NLP", "AI & ML", 0.021739, 60, "Intermediate", 
         ["NLTK Tutorial", "HuggingFace Course", "Practice: Sentiment Analysis"], ["AI", "NLP"]),
        ("NumPy", "Foundations", 0.021739, 50, "Intermediate", 
         ["NumPy Quickstart", "Math for ML", "Practice: Matrix Ops"], ["AI", "Math"])
    ],
    "Frontend Developer": [
        ("HTML", "Web Core", 0.021739, 40, "Beginner", 
         ["MDN HTML Guide", "W3Schools HTML", "Practice: Static Page"], ["Web", "UI"]),
        ("CSS", "Web Core", 0.021739, 40, "Beginner", 
         ["CSS Tricks Flexbox", "Grid Guide", "Practice: Responsive Page"], ["Web", "UI", "CSS"]),
        ("JavaScript", "Web Core", 0.021739, 60, "Intermediate", 
         ["Eloquent JavaScript", "JS Info", "Practice: Interactive DOM"], ["Web", "JS"]),
        ("React Hooks", "Frameworks", 0.021739, 60, "Intermediate", 
         ["React Official Tutorial", "Hooks Docs", "Practice: Custom Hook"], ["Web", "React"]),
        ("Responsive Design", "Product & UX", 0.021739, 50, "Intermediate", 
         ["Mobile First Guide", "Media Queries Tutorial", "Practice: Multi-device Layout"], ["Web", "UX"])
    ],
    "Backend Developer": [
        ("RESTful API", "APIs & Integration", 0.021739, 60, "Intermediate", 
         ["Postman Learning Center", "RestfulAPI.net", "Practice: Build CRUD API"], ["Web", "API"]),
        ("SQL", "Foundations", 0.021739, 60, "Intermediate", 
         ["SQLZoo", "PostgreSQL Tutorial", "Practice: Complex Joins"], ["Web", "Database"]),
        ("Middleware", "Web Core", 0.021739, 50, "Intermediate", 
         ["Flask Middleware Guide", "Express Docs", "Practice: Auth Middleware"], ["Web", "Security"]),
        ("Hashing", "Security", 0.021739, 50, "Intermediate", 
         ["OWASP Top 10", "Argon2 Tutorial", "Practice: Secure Login"], ["Web", "Security"]),
        ("HTTP Status Codes", "APIs & Integration", 0.021739, 40, "Beginner", 
         ["MDN HTTP Codes", "HTTP Cats", "Practice: API Error Handling"], ["Web", "API"])
    ],
    "UI/UX Designer": [
        ("Wireframes & Prototypes (Figma)", "Product & UX", 0.021739, 60, "Intermediate", 
         ["Figma Learn", "Prototyping Basics", "Practice: Mobile App Wireframe"], ["UX", "UI", "Design"]),
        ("User Research & Problem Framing", "Product & UX", 0.021739, 60, "Intermediate", 
         ["Interaction Design Foundation", "UX Research Guide", "Practice: User Interviews"], ["UX", "Research"]),
        ("Key Libraries (Storytelling)", "Foundations", 0.021739, 50, "Intermediate", 
         ["Storytelling for Designers", "UX Copywriting", "Practice: Case Study"], ["UX", "Content"]),
        ("Color Theory", "Web Core", 0.021739, 40, "Beginner", 
         ["Adobe Color Guide", "Typography Basics", "Practice: Brand Palette"], ["UI", "Visual"]),
        ("Interaction Design", "Product & UX", 0.021739, 60, "Intermediate", 
         ["Nielsen Norman Group", "Micro-interactions Guide", "Practice: Animated Component"], ["UX", "UI"])
    ]
}

LEVEL_MAP = {
    "Beginner": 1,
    "Intermediate": 2,
    "Advanced": 3
}

def calculate_advanced_metrics(user_skills_dict, target_career):
    """
    Implements Tasks 7, 8, 9, 10, 11
    user_skills_dict: { skill_name: proficiency_0_100 }
    """
    career_reqs = CAREER_SKILLS_ADVANCED.get(target_career, [])
    if not career_reqs:
        return None

    # Task 9: Threshold-Weighted Readiness Score
    total_weighted_score = 0
    max_possible_weight = sum(row[2] for row in career_reqs)
    
    # Task 7 & 11: Domain & Tag Matching
    domains_required = set()
    domains_matched = set()
    tags_matched = 0
    total_tags = 0
    
    # Task 8 & 10: Advanced Gaps & Resources
    missing_skills = []
    weak_skills = []
    resources_for_gaps = {}

    user_level_avg = sum(user_skills_dict.values()) / len(user_skills_dict) if user_skills_dict else 0
    user_level_label = "Beginner" if user_level_avg < 40 else "Intermediate" if user_level_avg < 75 else "Advanced"
    user_level_val = LEVEL_MAP[user_level_label]

    for skill, domain, weight, threshold, level, resources, tags in career_reqs:
        domains_required.add(domain)
        total_tags += len(tags)
        
        user_proficiency = user_skills_dict.get(skill, 0)
        
        # Readiness Math (Task 9)
        actual_score = min(user_proficiency / threshold, 1.0) * weight if threshold > 0 else 0
        total_weighted_score += actual_score
        
        # Domain Fit (Task 7)
        if user_proficiency >= threshold:
            domains_matched.add(domain)
            
        # Tag Similarity (Task 11)
        # In a real app, we'd compare user interests. Here we assume proficiency matches tag interest.
        if user_proficiency > 0:
            tags_matched += len(tags) # Simplified tag matching

        # Advanced Gap Analysis (Task 8)
        if user_proficiency == 0:
            missing_skills.append(skill)
            resources_for_gaps[skill] = resources # Task 10
        elif user_proficiency < threshold or user_level_val < LEVEL_MAP[level]:
            weak_skills.append(skill)
            resources_for_gaps[skill] = resources # Task 10

    # Task 9 Result
    readiness_score = (total_weighted_score / max_possible_weight) * 100 if max_possible_weight > 0 else 0
    
    # Task 7 Result
    domain_fit = (len(domains_matched) / len(domains_required)) * 100 if domains_required else 0
    
    # Task 11 Result
    tag_similarity = (tags_matched / total_tags) * 100 if total_tags else 0

    return {
        "career": target_career,
        "readiness": round(readiness_score, 2),
        "domain_fit": round(domain_fit, 2),
        "tag_similarity": round(tag_similarity, 2),
        "missing_skills": missing_skills,
        "weak_skills": weak_skills,
        "resources": resources_for_gaps
    }

def match_career_v2(user_skills_dict):
    """
    Ranks all careers using the advanced weighted algorithm.
    """
    rankings = []
    for career in CAREER_SKILLS_ADVANCED:
        metrics = calculate_advanced_metrics(user_skills_dict, career)
        if metrics is None:
            continue
        # Final rank score is a combination of readiness and domain fit
        rank_score = (metrics["readiness"] * 0.7) + (metrics["domain_fit"] * 0.3)
        rankings.append((career, rank_score, metrics))
    
    return sorted(rankings, key=lambda x: x[1], reverse=True)
