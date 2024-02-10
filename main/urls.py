from django.urls import path
from .views import *

urlpatterns = [
    path('say_hello/', say_hello),
    path('profile/', user_profile),
    path('company/', company_profile),
    path('queries/<int:query_id>/', filter_queries),
    path('try/<int:query_id>/<int:try_number>/', tried),
    path("queries/", QueryView.as_view(), name="query-view"),
]


