from django.shortcuts import render
from blog.models import Entry


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

def edit_entry(request, slug):
    # grab the object ...
    entry=Entry.objects.get(slug=slug)
    # set the form we're using ...
    form_class = EntryForm
    # if we're coming to this view from a submitted form,
    if request.method == 'POST':
        # grab the data from the submitted form
        form = form_class(data=request.POST, instance=entry)
        if form is valud():
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