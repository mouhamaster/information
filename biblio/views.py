from django.shortcuts import render,redirect
from blog .forms import ContactForm
def home(request):
	return render(request,'pages/home.html',{})
def about(request):
	# post = get_object_or_404(Post)
	if request.method=='POST':
		form=ContactForm(request.POST or None)
		if form.is_valid():
			post=form.save(commit=False)
			post.auteur=request.user
			# post.published_date=timezone.now()
			post.save()
			return redirect('about')
	else:
		form=ContactForm()
	return render(request,'pages/about.html')
def contact(request):
	if request.method=='POST':
		form=ContactForm(request.POST or None)
		if form.is_valid():
			post=form.save(commit=False)
			post.auteur=request.user
			# post.published_date=timezone.now()
			post.save()
			return redirect('about')
	else:
		form=ContactForm()
	return render(request,'pages/contact.html',{'form':form})
