import requests
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse

def home(request):
	context = {}
	return render(request, 'html/home.html', context) 

def search(request): 
	search_result = str(request.GET.get('search_result'))
	apiresult = 'https://api.dictionaryapi.dev/api/v2/entries/en/'+search_result
	print(apiresult) 
	apiresult = requests.get(apiresult).json() 
	print(apiresult)
	data = {'apiresult' : apiresult}
	return JsonResponse(data) 