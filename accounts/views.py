from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import UserForm
# Create your views here.
def hello_world(request):
    return HttpResponse("Hello World")


class HelloMadagascar(View):
    def get(self, request):
        return HttpResponse("Hello Madagascar")

class home(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("User created successfully")
    return render(request, 'index.html', {'form': form})