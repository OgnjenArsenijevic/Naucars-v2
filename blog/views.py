from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Ad
from .forms import AdForm, AdSearchForm
from .filters import AdFilter


def home(request):
    context = {
        'ads': Ad.objects.all()
    }
    return render(request, 'blog/home.html', context)


class AdListView(ListView):
    model = Ad
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'ads'
    ordering = ['-datePosted']
    paginate_by = 5  # put 2 to test pagination


class UserAdListView(ListView):
    model = Ad
    template_name = 'blog/user_ads.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'ads'
    paginate_by = 5  # put 2 to test pagination

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Ad.objects.filter(adOwner=user).order_by('-datePosted')


class SearchResultsListView(ListView):
    model = Ad
    template_name = 'blog/search_results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = AdFilter(self.request.GET, queryset=self.get_queryset())
        return context


'''
class SearchResultsListView(ListView):
    model = Ad
    context_object_name = 'ads'
    paginate_by = 5  # put 2 to test pagination

    def get(self, request, *args, **kwargs):
        print(request.GET)
        ads = Ad.objects.all()
        form = AdSearchForm()
        return render(request, 'blog/search_results.html', {'ads': ads, 'form': form})

    def post(self, request, *args, **kwargs):
        print('here')
        print(request.POST)
        manufacturer = request.POST.get('manufacturer')
        messages.success(request, f'Your account info has been updated!')
        return redirect('search-results')
'''


class AdDetailView(DetailView):
    model = Ad


class AdCreateView(LoginRequiredMixin, CreateView):
    model = Ad
    template_name = 'blog/ad_create.html'
    form_class = AdForm

    def form_valid(self, form):
        form.instance.adOwner = self.request.user
        return super().form_valid(form)


class AdUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ad
    template_name = 'blog/ad_update.html'
    form_class = AdForm

    def form_valid(self, form):
        form.instance.adOwner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        ad = self.get_object()
        if self.request.user == ad.adOwner:
            return True
        return False


class AdDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Ad
    template_name = 'blog/ad_delete.html'
    success_url = '/'

    def test_func(self):
        ad = self.get_object()
        if self.request.user == ad.adOwner:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
