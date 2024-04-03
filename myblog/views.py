from django.shortcuts import render
from myblog.models import DocumentContent

# Create your views here.

def archive(request):
    posts = DocumentContent.objects.all().order_by('-add_timestamp')[:5]
    return render(request,'archive.html',{'posts': posts})