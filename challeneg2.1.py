def solutions(data):
    c_right = 0
    c_interactions = 0
    for char in data:
        if char == '>':
            c_right+=1
        elif char == '<':
            c_interactions+=c_right
    return c_interactions*2