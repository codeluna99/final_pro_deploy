from django.shortcuts import render
import processing

def deployer(request):
    return render(request, 'chatbotDeployment/index.html')

def bot_search(request):

    query = request.GET.get('query')
    ans = processing.chatbot_response(query)
    return render(request, 'chatbotDeployment/index.html', {'ans': ans, 'query': query})
