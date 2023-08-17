from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')


def all_category(request):
    category_header = "All topics"
    return render(request,"category_list.html",locals())