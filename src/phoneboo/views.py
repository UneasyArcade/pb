from django.views.generic import TemplateView, CreateView, DeleteView
from . import forms
from . import models
from django.urls import reverse_lazy


class HomePageView(TemplateView):
    template_name='phoneboo/home.html'

    def get_context_data(self, **kwargs):
         context=super().get_context_data(**kwargs)
         search_by=self.request.GET.get('search_by')
         query=self.request.GET.get('query')
         search_message="All phones"
         if search_by in['phone', 'name'] and query:
              if search_by =='name':
                   search_message=f"Searching for 'name' by {query}"
                   persones=models.Persone.objects.filter(name=query)
              else:
                   search_message=f"Searching for 'phone' by {query}"
                   persones=models.Persone.objects.filter(phones__phone__startswith=query)
              context["search_message"]= search_message
              context["persones"]=persones
              return context
         context["search_message"]= search_message
         context["persones"]= models.Persone.objects.all()
         return context
    


class AddphoneFormView(CreateView):
    template_name='phoneboo/add_persone.html'
    form_class=forms.CreatePersoneFrom
    success_url=reverse_lazy('home')

    def get_success_url(self) -> str:
        phone_numders = self.request.POST.get('phones')
        for phone_number in phone_numders.split('\n'):
                models.Phone.objects.create(phone=phone_number,contact=self.object)
        return super().get_success_url()

class DeletePhoneView(DeleteView):
     model=models.Persone
     template_name='phoneboo/delete_persone.html'
     success_url=reverse_lazy('home')