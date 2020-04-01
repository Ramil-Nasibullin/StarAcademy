from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from . import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.views.generic import TemplateView
from admin_panel.models import Test


# Create your views here.
class Questions(TemplateView):
    template_name = 'test_page.html'
    def get(self, request):
        all_tests = Test.objects.all()
        ctx = {
            'all_tests': all_tests
        }
        return render(request, self.template_name, ctx)





def form(request):
    recrut_contact_form = forms.CreateNewRecrut
    context = {
        'recrut_contact_form': recrut_contact_form
    }
    return render(request, 'recrutregform.html', context)


def recrut_add(request):
    form = forms.CreateNewRecrut(request.POST)
    result = 'Рекрут успешно добавлен! %s' % request.path
    if request.method == 'POST':
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            print(data)
            return HttpResponse("Автор добавлен! %s" % request.path)


class MainView(TemplateView):
    template_name = 'main_page.html'

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name, {})
        else:
            return render(request, self.template_name, {})


















