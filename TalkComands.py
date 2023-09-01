def firstWord(hour):
    if 0 <= hour < 12:
        return "What a wonderful morning"
    elif 12 <= hour < 18:
        return "Good Afternoon!"
    else:
        return "Today is very nice eveningе"


def lastWords( hour):
    if 0 <= hour < 12:
        return "Have a nice day, Sir"

    elif 12 <= hour < 18:
        return "Good luck, Sir"

    else:
        return "Good night, sir"


def Talk(comand):
    if 'hello' in comand:
        return 'Nice to meet you, Sir'
    elif 'how are you' in comand:
        return ' Good,what about you, Sir?'
    elif 'i have very bad day' in comand:
        return 'Don`t worry Sir, you will succeed'
    elif 'i`m fine' in comand:
        return 'Glad to hear it, Sir'
    else:
        return ' '



