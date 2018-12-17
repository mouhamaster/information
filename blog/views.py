from django.shortcuts import render,redirect
from . models import Post
from .forms import ContactForm
# Create your views here.
def index(request):
	posts=Post.objects.all()
	return render(request,'blog/index.html',{'posts':posts})
def show(request,id):
	posts=Post.objects.get(pk=id)
	return render(request,'blog/show.html',{'posts':posts})
def contact(request):									
	if request.method=='POST':
		form=Post(request.POST or None)
		if form.is_valid():
			post=form.save(commit=False)
			post.Auhor=request.user
			post.published_date=timezone.now()
			post.save()
			return redirect('show')
	else:
		form=Post()
	return render(request,'blog/contact.html',{'form':form})
