# Newly created file

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
   
def analyze(request):
    # get the text
    djtext =(request.POST.get('text', 'default'))
    removepunc = request.POST.get('removepunc', 'off')
    full_caps = request.POST.get("captialize", "off")
    newline = request.POST.get('newline', "off")
    spaceremover = request.POST.get("spaceremover", "off")
    charactercount = request.POST.get("charactercount", "off")
    wordcount = request.POST.get("wordcount", "off")

    puncts ='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    if removepunc == 'on':
        analyzed = ""
        
        for char in djtext:
            if char not in puncts:
                analyzed = analyzed + char
        parameters = {  
                
    'purpose':'Remove Punctuation','analyzed_text' : analyzed}
        djtext = analyzed 
    
    if (full_caps == "on"):
        analyzed = ""

        for char in djtext:
            analyzed = analyzed+char.upper()
        
        parameters = {'purpose':'Capitalize','analyzed_text' : analyzed}
        djtext = analyzed
        
    if (newline == "on"):
        analyzed = ""
        skip_space = False
        for char in djtext:
            if char != "\n" and char != "\r":
                if char.isspace():
                    if not skip_space:
                        analyzed += char
                    skip_space = True
                else:
                    analyzed += char
                    skip_space = False
        print("pre", analyzed)
        parameters = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        djtext = analyzed
    
    if (spaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        parameters = {'purpose':'Space Remover Between Words','analyzed_text' : analyzed }
        djtext = analyzed
    
    elif (charactercount == "on"):
        analyzed_count = 0

        for char in djtext:
            if not (char.isspace()):
                analyzed_count += 1
        parameters = {'purpose':'Character Counter','analyzed_text' : "The Number Of Character is " +str(analyzed_count) }
        return render(request , "analyze.html", parameters)

    elif (wordcount == "on"):
        word_count = 0
        listed_word =djtext.split()
        for i in listed_word:
            word_count +=1
        parameters = {'purpose':'Character Counter','analyzed_text' : "The Number Of Words is " +str(word_count) }
        return render(request , "analyze.html", parameters)
    elif(removepunc != "on"  and full_caps != "on" and newline != "on" and spaceremover != "on" and wordcount != "on" and charactercount != "on"):
        return HttpResponse("ERROR 404")
    return render(request,'analyze.html',parameters)
    
    
    
    


