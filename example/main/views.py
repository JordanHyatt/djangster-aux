from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DeleteView, CreateView, UpdateView
from django_filters.views import FilterView
from django_aux.views import SaveFilterMixin, RedirectPrevMixin, InlineFormsetMixin, SinglePlotMixin
from main.tables import *
from main.filters import *
from main.models import *
from main.forms import *


class MainBase:
    ''' A base view for main app that implements common methods '''
    paginate_by = 50
    template_name = "django_aux/standard.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = '------- Main Portal --------'
        context['extend_str'] = 'main/base.html'
        return context

class HomePageView(MainBase, TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sub_header'] = 'Select Option From Side Bar'
        return context


class PersonBase(MainBase):
    model = Person
    table_class = PersonTable
    filterset_class = PersonFilter

class PersonLookup(PersonBase, SaveFilterMixin, FilterView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sub_header'] = 'Person Lookup'
        context.update(dict(url1='person-create', url1_text='[Create New Person]'))
        return context

class PersonCreate(PersonBase, SaveFilterMixin, CreateView):
    form_class = PersonForm
    success_url = reverse_lazy('person-lookup')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sub_header'] = 'Person Create'
        return context

class PersonDelete(PersonBase, RedirectPrevMixin, DeleteView):
    ''' Delete view for Person object '''
    template_name = 'django_aux/delete.html'


class PersonUpdate(PersonBase, RedirectPrevMixin, UpdateView):
    ''' Update view for Person instance '''
    form_class = PersonForm


class PersonUpdateInline(PersonBase, InlineFormsetMixin, UpdateView):
    ''' Update view for Person instance '''
    template_name = 'django_aux/inline-formset.html'
    form_class = PersonForm
    form_helper = PersonHelper
    factories = [{'factory':award_factory, 'helper':PersonAwardHelper, 'header':'Awards'}]
    success_url = reverse_lazy('person-lookup')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_lines_btn'] = True
        return context


class SaleBase(MainBase):
    model = Sale
    table_class = SaleTable
    filterset_class = SaleFilter

class SaleLookup(SaleBase, SaveFilterMixin, FilterView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sub_header'] = 'Sale Lookup'
        return context


class SalePlotly(SaleBase, SinglePlotMixin ,SaveFilterMixin, FilterView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sub_header'] = 'Sale Data Exploration'
        return context


    