from django.http import HttpResponse
from django.template import loader

from .req import countries_all, country_name, regions_api, get_capitals, capital


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


def capitals(request):
    template = loader.get_template("capitals.html")
    c = get_capitals()
    context = {'capitals': c}
    return HttpResponse(template.render(context, request))


def capital_info(request, name):
    template = loader.get_template("capital_info.html")
    c = capital(name)
    context = {'info': c}
    return HttpResponse(template.render(context, request))