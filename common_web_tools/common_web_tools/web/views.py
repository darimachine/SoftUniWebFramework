from django.core.paginator import Paginator
from django.shortcuts import render

from common_web_tools.web.models import Profile


# Create your views here.
def show_index(request):
    Profile.objects.create(
        name="Serhan",
        email="serhan@.com"
    )
    profiles = Profile.objects.all()
    paginator = Paginator(profiles,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    count  = request.session.get('count') or 0
    request.session['count'] = count +1
    context = {
        'count': request.session.get('count'),
        'profiles':page_obj
    }
    return render(request,'index.html',context)