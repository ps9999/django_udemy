from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord,User
from . import forms
from first_app.forms import UserForm

# Create your views here.
def index(request):
    context_dict = {'text':'hello world', 'number': 100}
    # return HttpResponse("Hello World!")
    # my_dict = {'insert_me': "Hello I am From views.py!"}
    # Webpages_list = AccessRecord.objects.order_by('date')
    # date_dict = {"access_rec": Webpages_list}
    return render(request, 'udemy_first_app/relative_url.html', context_dict)

# def index(request):
#     # return HttpResponse("Hello World!")
#     # my_dict = {'insert_me': "Hello I am From views.py!"}
#     Webpages_list = AccessRecord.objects.order_by('date')
#     date_dict = {"access_rec": Webpages_list}
#     return render(request, 'udemy_first_app/index.html', context=date_dict)

def form_names(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Validation is Successfull")
            print("Name:"+form.cleaned_data['name'])

    return render(request, 'udemy_first_app/form_page.html', {'form':form})

def users(request):
    form = UserForm()

    if request.method == 'POST':
        form = forms.UserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect_page_fn(request)
        else:
            print("Something went wrong")
    
    return render(request, 'udemy_first_app/user.html', {'form':form})

def redirect_page_fn(request):
    return render(request, 'udemy_first_app/user_list.html')

def other(request):
    return render(request, 'udemy_first_app/other.html')
