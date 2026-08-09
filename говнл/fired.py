text = 'im fucking ask you to do what i want and if you little shit dont understand me im fire you fucking bastard its last warning'
def count_curses(text):
    curses = ["fuck", "bastard", "shit", "damn", "asshole"]
    count = 0
    for curse in curses:
        count += text.lower().count(curse)
    return count
print(count_curses(text))

def fire_or_not(text):
    cs = count_curses(text)
    if cs >= 10:
        return "You are fired!"
    if cs < 10:
        return "You are not fired."
print(fire_or_not(text))