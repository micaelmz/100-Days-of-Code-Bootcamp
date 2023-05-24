def bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper

def emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper

def underline(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper