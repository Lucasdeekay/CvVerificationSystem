from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from django.views import View


class HomeView(View):
    template_name = 'mysite/home.html'

    def get(self, request):
        return render(request, self.template_name)


class AboutView(View):
    template_name = 'mysite/about.html'

    def get(self, request):
        return render(request, self.template_name)


class ContactView(View):
    template_name = 'mysite/contact.html'

    def get(self, request):
        return render(request, self.template_name)


class AuthLoginView(View):
    template_name = 'mysite/auth_login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        #  Check if the form is valid
        if request.method == "POST":
            # Process the input
            username = request.POST.get('username').strip()
            password = request.POST.get('password').strip()
            # Authenticate the user login details
            user = authenticate(request, username=username, password=password)
            # Check if user exists
            if user is not None:
                # Log in the user
                login(request, user)
                # Redirect to dashboard page
                return HttpResponseRedirect(reverse('Dashboard:upload_certificate'))
            # If user does not exist
            else:
                messages.error(request, "Invalid login credentials")
                # Redirect back to the login page
                return HttpResponseRedirect(reverse('MySite:login'))


class LogoutView(View):

    # Add a method decorator to make sure user is logged in
    # @method_decorator(login_required())
    # Create get function
    def get(self, request):
        # logout user
        logout(request)
        # redirect to login page
        return HttpResponseRedirect(reverse('MySite:home'))
