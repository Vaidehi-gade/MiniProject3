from django.http import HttpResponse
from django.shortcuts import render
import joblib

def home(request):
    return render(request,"home.html")

def questions(request):
    return render(request,"questions.html")

def result(request):
    cls = joblib.load('finalized_model.sav')

    lst = []
    ocean = []
    lst.append(request.GET['q1'])
    lst.append(request.GET['q2'])
    lst.append(request.GET['q3'])
    lst.append(request.GET['q4'])
    lst.append(request.GET['q5'])
    lst.append(request.GET['q6'])
    lst.append(request.GET['q7'])
    lst.append(request.GET['q8'])
    lst.append(request.GET['q9'])
    lst.append(request.GET['q10'])

    score_o = 0
    score_c = 0
    score_e = 0
    score_a = 0
    score_n = 0

    score_o = int(lst[0])+int(lst[1])
    score_c = int(lst[2])+int(lst[3])
    score_e = int(lst[4])+int(lst[5])
    score_a = int(lst[6])+int(lst[7])
    score_n = int(lst[8])+int(lst[9])

    ocean.append(request.GET['gender'])
    ocean.append(request.GET['age'])
    ocean.append(score_o)
    ocean.append(score_c)
    ocean.append(score_e)
    ocean.append(score_a)
    ocean.append(score_n)

    print(ocean)

    ans = cls.predict([ocean])

    return render(request,"result.html",{'ans':ans})