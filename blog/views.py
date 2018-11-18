from django.template.defaultfilters import slugify
from django.shortcuts import render, redirect
from blog.forms import EntryForm
from blog.models import Entry
from django.contrib.auth.decorators import login_required
from django.http import Http404


def index(request):
    entries = Entry.objects.all()
    # don't forget the quotes because it's a string, not an integer
    return render(request, 'index.html', {
        # don't forget to pass it in, and the last comma
        'entries': entries,
    })

def entry_detail(request, slug):
    # grab the object...
    entry = Entry.objects.get(slug=slug)
    # and pass to the template
    return render(request, 'entries/entry_detail.html', {
        'entry': entry,
    })

def browse_by_name(request, initial=None):
    if initial:
        entries = Entry.objects.filter(name__istartswith=initial).order_by('name')
    else:
        entries = Entry.objects.all().order_by('name')
    return render(request, 'search/search.html', {
        'entries': entries,
        'initial': initial,
    })

@login_required
def edit_entry(request, slug):
    # grab the object ...
    entry = Entry.objects.get(slug=slug)
    
    if entry.user != request.user:
        raise Http404
    # set the form we're using ...
    form_class = EntryForm
    # if we're coming to this view from a submitted form,
    if request.method == 'POST':
        # grab the data from the submitted form
        form = form_class(data=request.POST, instance=entry)
        if form.is_valid():
            # save the new data
            form.save()
            return redirect('entry_detail', slug=entry.slug)
    # otherwise just create the form
    else:
        form = form_class(instance=entry)
    # and render the template
    return render(request, 'entries/edit_entry.html', {
    'entry': entry, 'form': form,
    })

def create_entry(request):
    form_class = EntryForm
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.slug = slugify(entry.name)
            entry.save()
            return redirect('entry_detail', slug=entry.slug)
    else:
        form = form_class()

    return render(request, 'entries/create_entry.html', {'form' : form,
    })