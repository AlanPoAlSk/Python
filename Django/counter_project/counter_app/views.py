from django.shortcuts import render,redirect

def index (request):
    if 'count_num' in request.session :
        request.session['count_num'] += 1
        print(request.session['count_num'])
    else:
        request.session['count_num'] =1
    return render(request,'counter.html', {'count_num': request.session['count_num']})

def destroy(request):
    if 'count_num' in request.session :
        del request.session['count_num']
    return redirect('/')

def plus_two(request):
    if 'count_num' in request.session :
        request.session['count_num'] += 1
    return redirect('/')


