from django.contrib.auth import REDIRECT_FIELD_NAME
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import resolve_url, get_object_or_404
from django.template.response import TemplateResponse
from django.utils.http import is_safe_url
from django.views.generic import DetailView, UpdateView
from django.contrib.sites.models import get_current_site

from .forms import *
from testDjango import settings
from .models import *


class ProfileDetailView(DetailView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("profile view")


class ProfileUpdateView(UpdateView):
    form_class = ProfileUpdateForm
    model = User
    fields = ['first_name', 'last_name', 'email', 'phone',
              'address', 'cur_pwd', 'new_pwd1', 'new_pwd2']
    template_name = 'accounts/edit.html'

    def get(self, request, *args, **kwargs):
        self.object = User.objects.get(id=self.request.user.id)
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)

        return self.render_to_response(context)

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.request.user.id)



# class RegisterView(View):
# def get(self, request, *args, **kwargs):
# form = RegistrationForm(request)
#         current_site = get_current_site(request)
#
#         context = {
#             'form': form,
#             'site': current_site,
#             'site_name': current_site.name,
#         }
#         # return TemplateResponse(request, 'registration/register.html', context, current_app=accounts)
#         return render(request, 'registration/register.html', {
#             'form': form,
#         })
#
#     def post(self, request, *args, **kwargs):
#         return HttpResponse("register posted")

def register(request, template_name='registration/register.html',
             redirect_field_name=REDIRECT_FIELD_NAME,
             registration_form=RegistrationForm,
             current_app=None, extra_context=None):
    """
    Displays the login form and handles the login action.
    """
    redirect_to = request.REQUEST.get(redirect_field_name, '')

    if request.method == "POST":
        form = registration_form(data=request.POST)
        if form.is_valid():

            # Ensure the user-originating redirection url is safe.
            if not is_safe_url(url=redirect_to, host=request.get_host()):
                redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

            # Okay, security check complete. Log the user in.
            # cart = Cart()
            print("test")
            form.save()

            return HttpResponseRedirect(redirect_to)
    else:
        form = registration_form()

    current_site = get_current_site(request)

    context = {
        'form': form,
        redirect_field_name: redirect_to,
        'site': current_site,
        'site_name': current_site.name,
    }
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context,
                            current_app=current_app)