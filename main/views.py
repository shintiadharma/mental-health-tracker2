from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306245655',
        'name': 'Shintia Dharma Shanty',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)