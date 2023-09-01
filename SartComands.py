import webbrowser
import subprocess
import os

webbrowser.register('Y', None,webbrowser.BackgroundBrowser('C:\Program Files (x86)\Yandex\YandexBrowser\Application\Browser'))


def openComands(comand):
    if 'open youtube' in comand:
        webbrowser.get('Y').open("https://www.youtube.com")

    elif 'open browser' in comand:
        subprocess.call("C:\Program Files (x86)\Yandex\YandexBrowser\Application\Browser.exe")

    elif 'open messenger' in comand:
        webbrowser.get('Y').open("https://vk.com/im")

    elif 'open email' in comand:
        webbrowser.get('Y').open("https://e.mail.ru/inbox/?back=1")

    elif 'i want to play something' in comand:
        subprocess.call('C:\Program Files (x86)\Steam\Steam.exe')


def notepad():
    os.system("start "+"plan.txt")


def messenger(txt):
    if 'alex' in txt:
        webbrowser.open('https://vk.com/im?sel=215051398')
    if 'friend' in txt:
        webbrowser.open('https://vk.com/im?sel=188690738')
    if 'me' in txt:
        webbrowser.open('https://vk.com/im?sel=504941621')
    if 'my girlfriend' in txt:
        webbrowser.open('https://vk.com/im?sel=359314720')


def search(newCommand):
    webbrowser.get('Y').open('https://yandex.ru/search/?text=' + newCommand + '&clid=2271258&win=506&lr=197')

