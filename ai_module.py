def sayai(file):
    if file == "Hi":
        words = "How are you?"
    elif file == "How are you?":
        words = "I am good! thank you."
    elif file == "Hello!":
        words = "How are you?"
    elif file == "I am good! thank you.":
        words = "Ok."
    return words

__version__ = "0.1"
