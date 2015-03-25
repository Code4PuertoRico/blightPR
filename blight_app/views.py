from django.shortcuts import render
from blight_app.forms import AbndSiteForm
from blight_app.models import AbndSite


def add_abandoned(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = AbndSiteForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new property to the database.
            #form.save(commit=True)
            abn = form.save(commit=True)
            print abn

            # Now call the index() view.
            # The user will be shown the homepage.
            # return index(request)
            return render(request, 'mvp_app/home.html')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = AbndSiteForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'blight/add_abandoned.html', {'form': form})


def suggest(request, catastro):
    try:
        propiedad = AbndSite.objects.get(catastro=catastro)
    except AbndSite.DoesNotExist:
        raise Http404
    return render(request, 'blight/detail.html', {'propiedad': propiedad})

