import operator
from operator import itemgetter
from django.http import HttpResponse
from django.shortcuts import redirect, render

def homepage_(response):
    return HttpResponse('<h1>A Home Page</h1>')

def view_html(request):
    return render(request,'home.html')

def count(request):
    fulltext=request.GET['fulltext']
    wordlist=fulltext.split()


    #no of similar word count
    worddict={}
    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word]=1

        sortedword=sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request,'count.html',{'fulltext':fulltext, 'count':len(wordlist), 'worddictionary':sortedword})