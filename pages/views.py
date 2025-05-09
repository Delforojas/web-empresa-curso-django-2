from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from .models import Page
from django.shortcuts import redirect
from .forms import PageForm


class StaffRequiredMixin(object):

    @method_decorator(staff_member_required)
    def dispatch(self, request , *args, **kwargs):
        return super(PageCreate, self).dispatch(request, *args , **kwargs)



# Create your views here.
class PagesListView(ListView):
    model = Page
    template_name = 'pages/page_list.html' 

class PageDetailView(DetailView):
    model = Page

@method_decorator(staff_member_required, name='dispatch')
class PageCreate(CreateView):
    model = Page
    form_class = PageForm
    template_name = 'pages/includes/pages_form.html'
    success_url =reverse_lazy('pages:pages')

@method_decorator(staff_member_required, name='dispatch')
class PageUpdate(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = "_update_form"
    template_name = 'pages/includes/page_update_form.html'
    
    
    def get_success_url (self):
        return reverse('pages:page', args=[self.object.id, self.object.slug])+ '?ok'

@method_decorator(staff_member_required, name='dispatch')
class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy("pages:pages")
    template_name = 'pages/includes/pages_confirm_delete.html'