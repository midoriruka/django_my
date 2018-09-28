from django.shortcuts import render
# Create your views here.
user_list=[]

def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        temp={'user':username,'pw':password}
        user_list.append(temp)
    return render(request, 'index.html',[)

