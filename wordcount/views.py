from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request) :
    return render(request,'home.html')
    

def count(request) :
    fulltext = request.GET['fulltext']
    words = fulltext.split()

    worddico =  {}

    for word in words :
        if word in worddico :
            #incrementation
            worddico[word] += 1
        else :
            #ajout au dico
            worddico[word] = 1
    sworddico = sorted(worddico.items(),key= operator.itemgetter(1),reverse = True)
    return render(request,'count.html',{'fulltext':fulltext,'count':len(words),'sworddico': sworddico})

def about(request) :
    return render(request, 'about.html')
    

