
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import joblib 
from django.conf import settings
import os
# Create your views here.

class PrediccionAvocado(APIView):
    def post(self,request):
       model_file = os.path.join(settings.BASE_DIR,'api_avocado_app','modelo_avocado.pkl')
       modelo = joblib.load(model_file) 
       data = request.data
       try:
           pred = modelo.predict([[
               data['color'],
               data['tamano'],
               data['firmeza']
           ]])
           return Response({'maduro':pred[0]},status=status.HTTP_200_OK)
       except Exception as e:
           return Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)