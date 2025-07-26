from django.shortcuts import render
from .models import Post, Contact
from .forms import ContactForm

def contact_home(request):
    posts = Post.objects.all().order_by('-created_at')
    success = False

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success = True  # Show success message
            form = ContactForm()  # Clear form after success
    else:
        form = ContactForm()

    return render(request, 'blog/home.html', {'posts': posts, 'form': form, 'success': success})