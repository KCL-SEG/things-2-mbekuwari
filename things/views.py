from django.shortcuts import render
from .forms import ThingForm
from .models import Thing

# def home(request):
#     return render(request, 'home.html', {'form': form})


def home(request):
    if request.method == 'POST':
        form = ThingForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect or do something else after successfully processing the form
            return redirect('home')
    else:
        form = ThingForm()

    return render(request, 'home.html', {'form': form})
