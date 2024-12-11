 # mood_responses.py
def mood_response(mood):
# Implement your response logic here
    mood = mood.lower()

    if mood == 'sad':
        return "It's okay to feel down, allow yourself to feel it and let it go!"
    elif mood == 'stressed':
        return "Don't let the stress take over, step away and come back to it later."
    elif mood == 'excited':
        return "Anticipation and excitement can uplift your entire day!"
    elif mood == 'happy':
        return "It's great to feel good!"
    else:
        return ""
