from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = (request.POST.get('text','default'))
    analyze = (request.POST.get('analyze', 'off'))
    capitalise = (request.POST.get('capitalise', 'off'))
    charcount = (request.POST.get('charcount', 'off'))
    extra_space_remover = (request.POST.get('extra_space_remover','off'))
    new_line_remover = (request.POST.get('new_line_remover','off'))
    punctuations = '''.?""',-!--:;()[]{}.../\|'''
    analyzed = ""
    if (charcount == "on"):
        analyzed = len(djtext)
        params = {"analyzed_text": analyzed}
        djtext = analyzed

    if analyze == "on":
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {"analyzed_text": analyzed}
        djtext = analyzed

    if (capitalise == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {"analyzed_text": analyzed}
        djtext = analyzed

    if(new_line_remover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {"analyzed_text": analyzed}
        djtext = analyzed

    if(extra_space_remover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {"analyzed_text": analyzed}
        djtext = analyzed

    return render(request,'analyze.html',params)
