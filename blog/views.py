from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Post
from .forms import ContactForm

def contact_home(request):
    posts = Post.objects.all().order_by('-created_at')
    success = False

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send email to your inbox
            send_mail(
                subject=f"New Contact Form Submission from {name}",
                message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],  # Your email here
                fail_silently=False,
            )

            success = True  # Show success message
            form = ContactForm()  # Clear form after success
    else:
        form = ContactForm()

    return render(request, 'blog/home.html', {'posts': posts, 'form': form, 'success': success})
