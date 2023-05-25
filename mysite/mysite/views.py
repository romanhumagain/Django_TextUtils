# Newly created file

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
   
def analyze(request):
    # get the text
    djtext =(request.GET.get('text', 'default'))
    removepunc = request.GET.get('removepunc', 'off')
    full_caps = request.GET.get("captialize", "off")
    newline = request.GET.get('newline', "off")
    spaceremover = request.GET.get("spaceremover", "off")
    charactercount = request.GET.get("charactercount", "off")
    wordcount = request.GET.get("wordcount", "off")

    puncts ='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    if removepunc == 'on':
        analyzed = ""
        
        for char in djtext:
            if char not in puncts:
                analyzed = analyzed + char
        parameters = {  
                
    'purpose':'Remove Punctuation','analyzed_text' : analyzed}
        return render(request, 'analyze.html',parameters)

    if (full_caps == "on"):
        analyzed = ""

        for char in djtext:
            analyzed = analyzed+char.upper()
        
        parameters = {'purpose':'Capitalize','analyzed_text' : analyzed}
        return render(request, 'analyze.html',parameters)
    
    if(newline == "on"):
        analyzed = djtext.replace("\n", " ")
        parameters = {'purpose':'New Line Remover','analyzed_text' : analyzed }
        return render(request, 'analyze.html', parameters)

    if(spaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        parameters = {'purpose':'Space Remover Between Words','analyzed_text' : analyzed }
        return render(request, 'analyze.html',parameters)
    
    if (charactercount == "on"):
        analyzed_count = 0

        for char in djtext:
            if not (char.isspace()):
                analyzed_count += 1
        parameters = {'purpose':'Character Counter','analyzed_text' : "The Number Of Character is " +str(analyzed_count) }
        return render(request , "analyze.html", parameters)

    if(wordcount == "on"):
        word_count = 0
        listed_word =djtext.split()
        for i in listed_word:
            word_count +=1
        parameters = {'purpose':'Character Counter','analyzed_text' : "The Number Of Words is " +str(word_count) }
        return render(request , "analyze.html", parameters)
    # else:
    #     return HttpResponse("ERROR 404")
    
    
    
    


