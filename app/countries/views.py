from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse

from .req import countries_all, country_name, regions_api


def view_all(request):
    c = countries_all()
    template = loader.get_template("all.html")
    context = {'countries': c}
    return HttpResponse(template.render(context, request))


def country_info(request, country):
    c = country_name(str(country))
    template = loader.get_template("country.html")
    context = {'country': c}
    return HttpResponse(template.render(context, request))

def regions(request):
    pass

def user_auth(request, username, pswrd):
    if username == 'my_user' and pswrd == '863786':
        return JsonResponse({'status': 'authorised'})
    else:
        return JsonResponse({'status': 'unauthorised'})
