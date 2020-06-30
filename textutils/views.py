from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')


def analyze(request):
    # Get the text
    djtext=request.GET.get('text', 'default')

    # checkbox value
    removepunc = request.GET.get('removepunc','off')
    fullcaps  = request.GET.get('fullcap','off')
    newlineremover = request.GET.get('newlineremover','off')
    extraspaceremover = request.GET.get('extraspaceremover','off')

    # check which check box is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char 
        params={'purpose':'Remove Punctuation','analyzed_text': analyzed}
        return render(request,'analyze.html',params) 


    elif(fullcaps == "on"):  
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params={'purpose':'changed to Uppercase','analyzed_text': analyzed}
        return render(request,'analyze.html',params) 

    elif(newlineremover == "on"):
        analyzed=""
        for char in djtext:
            if char !="\n" and char !="\r":
             analyzed = analyzed + char
        params={'purpose':'Remove New Line','analyzed_text': analyzed}
        return render(request,'analyze.html',params) 

    elif(extraspaceremover == "on"):
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params={'purpose':'Extra Space Remover','analyzed_text': analyzed}
        return render(request,'analyze.html',params) 





    else:
        return render(request,'notfound.html') 

# def capfirst(request):
#     return HttpResponse("We Capilitize First letter" )        

# def newlineremover(request):
#     return HttpResponse("hello i am newlineremover ")        

# def spaceremover(request):
#     return HttpResponse("hello i am spaceremover")
    
# def charcount(request):
#     return HttpResponse("hello i am charcount")    