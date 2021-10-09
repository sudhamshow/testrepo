def my_cap(text):
    return text[0].upper() + text[1:]

def my_title(text):
    res = ""
    for t in text.split():
        res = res + " " + my_cap(t)
    return res
