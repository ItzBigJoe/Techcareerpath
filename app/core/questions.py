# 25 Multiple Choice Questions across 5 categories with correct answers
QUESTIONS = [
    # 1-5: Soft Skills
    {"id": 1, "category": "Soft Skills", "text": "How do you typically handle a disagreement with a team member?", "options": ["Avoid the conflict", "Insist on my approach", "Seek a compromise through discussion", "Report to the manager immediately"], "answer": "Seek a compromise through discussion"},
    {"id": 2, "category": "Soft Skills", "text": "What is most important when presenting technical information to non-technical stakeholders?", "options": ["Using industry jargon", "Providing deep code details", "Simplifying concepts and focusing on value", "Focusing on speed of delivery"], "answer": "Simplifying concepts and focusing on value"},
    {"id": 3, "category": "Soft Skills", "text": "How do you manage your tasks when facing multiple tight deadlines?", "options": ["Work on whatever is easiest", "Prioritize based on urgency and impact", "Multitask on everything at once", "Wait for instructions from others"], "answer": "Prioritize based on urgency and impact"},
    {"id": 4, "category": "Soft Skills", "text": "What is the best way to handle receiving constructive criticism on your work?", "options": ["Take it personally", "Defend my decisions immediately", "Listen, reflect, and look for improvements", "Ignore the feedback"], "answer": "Listen, reflect, and look for improvements"},
    {"id": 5, "category": "Soft Skills", "text": "In a team setting, what does 'effective collaboration' primarily mean to you?", "options": ["Doing all the work yourself", "Open communication and shared goals", "Strictly following individual tasks only", "Competitive behavior between members"], "answer": "Open communication and shared goals"},

    # 6-10: Frontend Development
    {"id": 6, "category": "Frontend", "text": "Which CSS property is used to create a flexbox container?", "options": ["display: block", "display: flex", "display: grid", "float: left"], "answer": "display: flex"},
    {"id": 7, "category": "Frontend", "text": "What is the primary purpose of React Hooks?", "options": ["To manipulate the DOM directly", "To use state and lifecycle in functional components", "To speed up page loading", "To replace CSS styling"], "answer": "To use state and lifecycle in functional components"},
    {"id": 8, "category": "Frontend", "text": "Which HTML tag is correctly used for the largest heading?", "options": ["<heading>", "<h6>", "<h1>", "<head>"], "answer": "<h1>"},
    {"id": 9, "category": "Frontend", "text": "What does 'Responsive Web Design' refer to?", "options": ["Websites that load very fast", "Websites that adapt to different screen sizes", "Websites with lots of animations", "Websites that use specific fonts"], "answer": "Websites that adapt to different screen sizes"},
    {"id": 10, "category": "Frontend", "text": "In JavaScript, which method is used to add an element to the end of an array?", "options": ["pop()", "shift()", "push()", "unshift()"], "answer": "push()"},

    # 11-15: Backend Development
    {"id": 11, "category": "Backend", "text": "What is the main role of a RESTful API?", "options": ["To style the user interface", "To provide a standard way for systems to communicate", "To store data in the browser", "To handle CSS animations"], "answer": "To provide a standard way for systems to communicate"},
    {"id": 12, "category": "Backend", "text": "Which SQL command is used to retrieve data from a database?", "options": ["INSERT", "UPDATE", "DELETE", "SELECT"], "answer": "SELECT"},
    {"id": 13, "category": "Backend", "text": "What is 'Middleware' in a web framework like Flask or Express?", "options": ["A type of database", "Functions that run during the request-response cycle", "A CSS framework", "A frontend routing library"], "answer": "Functions that run during the request-response cycle"},
    {"id": 14, "category": "Backend", "text": "What does 'Hashing' a password primarily achieve?", "options": ["Compressing the password size", "Encrypting it so it can be reversed", "One-way conversion for secure storage", "Formatting it for the UI"], "answer": "One-way conversion for secure storage"},
    {"id": 15, "category": "Backend", "text": "Which HTTP status code represents a 'Not Found' error?", "options": ["200", "404", "500", "403"], "answer": "404"},

    # 16-20: AI and Data Science
    {"id": 16, "category": "AI/Data Science", "text": "What is the primary goal of Supervised Learning?", "options": ["Learning from unlabeled data", "Learning from labeled data with targets", "Clustering data into groups", "Reducing data dimensionality"], "answer": "Learning from labeled data with targets"},
    {"id": 17, "category": "AI/Data Science", "text": "In Data Science, what is 'Overfitting'?", "options": ["The model is too simple for the data", "The model performs perfectly on new data", "The model learns noise and performs poorly on new data", "The model takes too long to train"], "answer": "The model learns noise and performs poorly on new data"},
    {"id": 18, "category": "AI/Data Science", "text": "Which Python library is most commonly used for numerical computations?", "options": ["NumPy", "Flask", "BeautifulSoup", "Pygame"], "answer": "NumPy"},
    {"id": 19, "category": "AI/Data Science", "text": "What does 'NLP' stand for in AI?", "options": ["Next Level Programming", "Natural Language Processing", "Network Layer Protocol", "Neural Logic Path"], "answer": "Natural Language Processing"},
    {"id": 20, "category": "AI/Data Science", "text": "What is a 'Confusion Matrix' used for?", "options": ["Generating new images", "Evaluating classification model performance", "Cleaning raw data", "Visualizing 3D data"], "answer": "Evaluating classification model performance"},

    # 21-25: Data Structure and Algorithm
    {"id": 21, "category": "DSA", "text": "What is the average time complexity of searching in a Hash Table?", "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"], "answer": "O(1)"},
    {"id": 22, "category": "DSA", "text": "Which data structure follows the 'First In, First Out' (FIFO) principle?", "options": ["Stack", "Queue", "Binary Tree", "Linked List"], "answer": "Queue"},
    {"id": 23, "category": "DSA", "text": "What is the main advantage of a Binary Search over a Linear Search?", "options": ["It works on unsorted arrays", "It is easier to implement", "It is much faster for large sorted datasets", "It uses less memory"], "answer": "It is much faster for large sorted datasets"},
    {"id": 24, "category": "DSA", "text": "Which algorithm is commonly used to find the shortest path in a graph?", "options": ["Binary Search", "Dijkstra's Algorithm", "Merge Sort", "Depth First Search"], "answer": "Dijkstra's Algorithm"},
    {"id": 25, "category": "DSA", "text": "In a linked list, what does a 'node' typically contain?", "options": ["Only data", "Only a pointer", "Data and a pointer to the next node", "An index and a value"], "answer": "Data and a pointer to the next node"}
]
