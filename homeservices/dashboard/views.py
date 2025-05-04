from django.shortcuts import render

def home(request):
    return render(request, 'dashboard/base.html')

# def color(request):
#     return render(request, 'elements/color.html')

# def typography(request):
#     return render(request, 'elements/typography.html')
