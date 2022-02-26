from django.shortcuts import render


# our home page view
def home(request):
    return render(request, 'index.html')

from Movie_Reccom_app import try1
# our result page view
def result(request):
    mName = request.GET['mName']

    result = try1.start(mName)
    return render(request, 'result.html', {'result': result})