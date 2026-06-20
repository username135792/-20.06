from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, ApplicationForm, ReviewForm
from .models import Application


def index(request):
    return render(request, 'App/index.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'App/register.html', {'form': form})


@login_required
def profile(request):
    applications = request.user.applications.all()
    review_form = ReviewForm()
    return render(request, 'App/profile.html', {
        'applications': applications,
        'review_form': review_form,
    })


@login_required
def application_create(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            return redirect('profile')
    else:
        form = ApplicationForm()
    return render(request, 'App/application_form.html', {'form': form})


@login_required
def review_create(request, app_id):
    application = get_object_or_404(Application, id=app_id, user=request.user)
    if application.status == 'new':
        return redirect('profile')
    if hasattr(application, 'review'):
        return redirect('profile')
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.application = application
            review.save()
    return redirect('profile')
