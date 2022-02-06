# from django.shortcuts import render
from django.views import View
from .models import Company
from django.http.response import JsonResponse

# Create your views here.

#Existen VIEWS about CLASS and about FUNCTIONS;

class CompanyView(View):
    
    def get(self, request):
        # companies = Company.objects.all()
        companies = list(Company.objects.values())
        if len(companies) > 0:
            data = {
                'message': 'Success',
                'companies': companies,
            }
        else:
            data = {
                'message': 'Error: Companies not found...'
            }
        return JsonResponse(data)
    
    
    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass
