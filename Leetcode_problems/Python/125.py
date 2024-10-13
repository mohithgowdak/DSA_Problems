from collections import defaultdict

def chooseFlask(requirements, flaskTypes, markings):
    min_waste = float('inf')
    best_flask = -1
    
    flask_markings = defaultdict(list)
    for f_id, mark in markings:
        flask_markings[f_id].append(mark)
    
    for flask_id in range(flaskTypes):
        waste = 0
        valid = True
        
        suitable_markings = sorted(flask_markings[flask_id])
        
        for req in requirements:
            idx = next((i for i, mark in enumerate(suitable_markings) if mark >= req), None)
            if idx is None:
                valid = False
                break
            waste += suitable_markings[idx] - req
        
        if valid and waste <= min_waste: # Changed < to <= to return the first flask with minimum waste
            min_waste = waste
            best_flask = flask_id
            if waste == min_waste: # Added condition to return the first flask with minimum waste
                break
    
    return best_flask
requirements = [5, 10, 15]
flaskTypes = 3
markings = [
        (0, 3), (0, 8), (0, 12),
        (1, 4), (1, 9), (1, 14),
        (2, 2), (2, 7), (2, 11)
    ]
    
result = chooseFlask(requirements, flaskTypes, markings)
print(result)
