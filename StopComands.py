import re


def whatTime(comand):
    p = re.findall(r'\d+', comand)
    answer = int(p[0])
    if 'minutes' in comand:
        answer *= 60
        return answer
    else:
        return answer
