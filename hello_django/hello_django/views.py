from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    myText1 = 'Это мой первый проект на Django'
    myText2 = 'И пока я мало что понимаю'
    myText3 = 'например как обработать событие нажатия кнопки?'
    return render(request, 'about.html', {'text1': myText1, 'text2': myText2, 'text3': myText3})


def home(request):
    return HttpResponse('This is my new home function')

def action1(request):
    return HttpResponse('A C T I O N № 1')

def main_page(request):
    myText1 = 'Это пробный текст для домашнего задания'
    return render(request, 'home.html', {'text1': myText1})



