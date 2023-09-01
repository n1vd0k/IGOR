import keyboard

def readPlans():
    file = open('plan.txt', 'r')
    text = file.read()
    file.close()
    return text


def wrightNewPlan(text):
    file = open('plan.txt', 'w+')
    file.seek(0)
    file.write(text)
    file.close()


def writing(txt):
    keyboard.write(txt)
    keyboard.send('enter')
