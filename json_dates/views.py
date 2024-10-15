from django.views import View
from django.http import JsonResponse
from .models import Data
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize


@method_decorator(csrf_exempt, name='dispatch')
class DataView(View):
    def get(self, request):
        dates = Data.objects.all()  # Get all book objects from the database

        dates_serialized_data = serialize('python', dates)

        data = {
            'dates':  dates_serialized_data
        }
        return JsonResponse(data)

    def post(self, request):
        post_body = json.loads(request.body)

        name = post_body.get('name')
        last_name = post_body.get('author')
        birthday = post_body.get('birthday')
        phone_number = post_body.get('phone_number')
        university = post_body.get('university')

        dates = {
            'name': name,
            'last_name':  last_name,
            'birthday': birthday,
            'phone_number': phone_number,
            'university': university
        }

        data_obj = Data.objects.create(**dates)
        data = {
            'message': f'New book object has been created with id {data_obj.id}'
        }
        return JsonResponse(data, status=201)

