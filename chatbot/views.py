from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def chatbot (request):
    if(request.method == 'POST'):
        message = request.POST.get('message')
        response = "The young kijana is done with school"
        return JsonResponse({'message' : message , 'response' : response})
    return render (request, 'chatbot.html')
# at this point django already knows where to get the templates from