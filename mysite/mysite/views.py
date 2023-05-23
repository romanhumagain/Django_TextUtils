# Newly created file

from django.http import HttpResponse

# part1
'''def index(request):
    return HttpResponse('<h3><a href = "https://www.facebook.com/roman.humagain/">Facebook</a></h3>')

def about(request):
    return HttpResponse("I am very very fine !! Thank you")'''

# code for part 2 bacic example of pipe line

def index(request):
    return HttpResponse("Home Page <a href '/'>Back</a>")
def removepunc(request):
    return HttpResponse("Remove Punc")
def capfirst(request):
    return HttpResponse("Capitalized")
def newlineremove(request):
    return HttpResponse("Line Removed")
def spaceremove(request):
    return HttpResponse("space removed")
def charcount(request):
    return HttpResponse("character counted")


