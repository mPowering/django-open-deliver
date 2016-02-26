
from django.shortcuts import render_to_response
from django.template import RequestContext

def home_view(request):
    return render_to_response('opendeliver/home.html',
                              {},
                              context_instance=RequestContext(request))