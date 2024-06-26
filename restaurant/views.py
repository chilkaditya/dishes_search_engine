from django.shortcuts import render
from django.db.models import Q
from .models import Restaurant
from .forms import SearchForm

def search(request):
    form = SearchForm()
    results = []
    query = None
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Restaurant.objects.filter(items__icontains=query)
    
    return render(request, 'restaurant/search.html', {'form': form, 'results': results, 'query': query})
