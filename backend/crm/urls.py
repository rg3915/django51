from django.urls import path
from backend.crm import views as v


urlpatterns = [
    path('', v.PersonListView.as_view(), name='person_list'),
]
