from django.urls import path
from .views import PrediccionAvocado


urlpatterns = [
     path('prediccion/',PrediccionAvocado.as_view(),name='prediccionavocado'),
     
     
]
