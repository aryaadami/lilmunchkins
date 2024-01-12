from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from . forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
from django.conf import settings
import os
from . models import Memory

def landing_page(request):
    # If use is authenticated, go to home page
    if request.user.is_authenticated:
        return redirect('main:home-page')
    # Create blank login form and set login failed status to false
    form = LoginForm()
    login_failed = False
    if request.method == "POST":
        form = LoginForm(request.POST)
        # Form submitted
        if form.is_valid():
            # Clean data
            data = form.cleaned_data
            # Try to authenticate and login
            user = authenticate(username = data['username'],
                                password = data['password'])
            # Login and display page
            if user is not None:
                login(request, user)
                return redirect('main:home-page')
            else:
                login_failed = True
        else:
            form = LoginForm()

    return render(request,
                  'landing_page.html',
                  {'form' : form,
                   'login_failed' : login_failed})   

@login_required
def home_page(request):
    # Get all objects
    memories = Memory.objects.all()
    # Paginate
    paginator = Paginator(memories, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request,
                  'home_page.html',
                  {'page_obj' : page_obj})

@login_required
def memory_detail(request, slug):
    memory = get_object_or_404(Memory, slug=slug)
    return render(request,
                  'memory_detail.html',
                  {'memory' : memory})

@login_required
def serve_media(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'))
    raise Http404('Media not found')

def custom_404(request, exception):
    return render(request, 'utilities/404.html', {}, status=404)
