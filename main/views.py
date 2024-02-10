from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View


# Create your views here.

def say_hello(req):
    return HttpResponse("<h1> Hello Fleur<h1/>")

def user_profile(req):
    return JsonResponse({
        'name':'Sika',
        'number': 55500005550,
        'email': "sikaantwi@gmail.com"
    })

def company_profile(req):
    return HttpResponse("<a href='www.youtube.com'>youtubeee</a>")



def filter_queries(req, query_id):
    return JsonResponse({
        'id' : query_id,
        'title': "Quezy Quezy",
        'description': "THE MOPAD DOPAD GOPAD LOPAD SHOWED UP",
        'status': True,
        'submitted_by': "Beezy",
  })


def tried(req, query_id,try_number):
    return JsonResponse({
        'id' : query_id,
        'title': try_number,
        'description': "THE MOPAD DOPAD GOPAD LOPAD SHOWED UP",
        'status': True,
        'submitted_by': "Beezy",
  })


class QueryView(View):
        queries = [
            {'id': 1, 'title': 'Adama decclined Val shots'},
            {'id': 2, 'title': 'Samson declined Val shots'}
        ]
        def get(self, request):
            return JsonResponse({"result":self.queries})
        
        def post(self, request):
             return JsonResponse({"status": "ok"})



# write a view fucntion with the name user_profile .The view function should return a json response and the json response data should include name, email and phone number

# register the view function on a path called profile 