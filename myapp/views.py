from django.shortcuts import render, HttpResponse, redirect
from .forms import AudioForm
from .learning  import model
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            file_name = form.cleaned_data['audio'].name
            aud_path = f"C:/Users/nadua/OneDrive/Desktop/folders/mlp/musicgenre/audio_files/audi_files/{file_name}"
            print(file_name)
            genre = model.classifier(aud_path)
            genre = genre[0]
            if genre == "blues":
                return redirect("blues")
            elif genre == "classical":
                return redirect("classical")
            elif genre == "disco":
                return redirect("disco")
            elif genre == "hiphop":
                return redirect("hiphop")
            elif genre == "jazz":
                return redirect("jazz")
            elif genre == "metal":
                return redirect("metal")
            elif genre == "pop":
                return redirect("pop")
            elif genre == "reggae":
                return redirect("reggae")
            elif genre == "rock":
                return redirect("rock")
            else:
                print("Hello")
    else:
        form = AudioForm(request.POST, request.FILES)
        return render(request, "base.html", {'form': form})


def blues(request):
    return render(request, "blues.html")

def classical(request):
    return render(request, "classical.html")

def country(request):
    return render(request, "country.html")

def disco(request):
    return render(request, "disco.html")

def hiphop(request):
    return render(request, "hiphop.html")

def jazz(request):
    return render(request, "jazz.html")

def metal(request):
    return render(request, "metal.html")

def pop(request):
    return render(request, "pop.html")

def reggae(request):
    return render(request, "reggae.html")

def rock(request):
    return render(request, "rock.html")
