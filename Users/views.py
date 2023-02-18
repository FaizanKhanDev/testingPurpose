from django.conf.global_settings import DEFAULT_FROM_EMAIL
from django.contrib.auth import login, logout, authenticate
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views import View
from django.views.generic import CreateView
from .forms import HumsterSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from .forms import UserUpdateForm
from django.shortcuts import render
from django.urls import reverse
from .utils import token_generator

from django.utils.encoding import force_bytes, force_str as force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site


def index(request):
    return render(request, 'index.html')


def register(request):
    return render(request, 'register.html')


class humster_register(CreateView):
    model = User
    form_class = HumsterSignUpForm
    template_name = 'humster_register.html'

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        user = authenticate(email=email, password=password)

        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        token = token_generator.make_token(user)

        domain = get_current_site(self.request).domain
        link = reverse('activate', kwargs={'uidb64': uidb64, 'token': token})

        # IMPLEMENTS THIS URL IN THE EMAIL.
        activate_url = 'http://' + domain + link

        send_mail(
            'Activate email',
            f'Here is the message. {activate_url}',
            DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )
        return redirect('/')


class verification_view(CreateView):
    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)

        if user is not None and token_generator.check_token(user, token):
            user.email_verify = True
            user.save()
            login(self.request, user)
            return redirect('login')
        return redirect('invalid_verify')

    @staticmethod
    def get_user(uidb64):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError,
                User.DoesNotExist, ValidationError):
            user = None
        return user


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'login.html',
                  context={'form': AuthenticationForm()})


def logout_view(request):
    logout(request)
    return redirect('/')


def profile(request, username):
    if request.method == 'POST':
        user = request.user
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user_form = form.save()

            messages.success(request, f'{user_form}, Your profile has been updated!')
            return redirect('profile', user_form.username)

        for error in list(form.errors.values()):
            messages.error(request, error)

    user = get_user_model().objects.filter(username=username).first()
    if user:
        form = UserUpdateForm(instance=user)
        form.fields['api_key'].widget.attrs = {'rows': 1}
        form.fields['api_secret'].widget.attrs = {'rows': 1}
        form.fields['trader'].widget.attrs = {'rows': 1}

        return render(request, 'profile.html', context={'form': form})

    return redirect("/")
