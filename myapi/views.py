# from django.shortcuts import render
from django.views import View
from .models import Company
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

#Existen VIEWS about CLASS and about FUNCTIONS;

class CompanyView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
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
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        Company.objects.create(name=jd['name'], website=jd['website'], foundation=jd['foundation'])
        data = {
            'message': 'Success',
        }
        return JsonResponse(data)
        

    def put(self, request):
        pass

    def delete(self, request):
        pass
