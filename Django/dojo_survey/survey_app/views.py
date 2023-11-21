from django.shortcuts import render ,redirect

def index(request):
    return render(request,'form.html')

def create_info(request):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['experience'] = request.POST['experience']
    request.session['comment'] = request.POST['comment']
    
    print(request.POST)
    return redirect('/result')

def result(request):
    return render(request, 'show.html')