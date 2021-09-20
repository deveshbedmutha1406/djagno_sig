
from django.shortcuts import render

# Create your views here.

def base(request):
    if request.method == 'POST':
        #name of input button.

        num = request.POST['num']
        context = {
            'num':range(1,int(num)+1)
        }

        return render(request, 'app1/base.html',context)

    
    return render(request,'app1/base.html')

# def print_number(request):
#     if request.method == 'POST':
#         #name of input button 
#         num = request.POST['num']

#         context = {
#             'num':range(int(num))
#         }
    

#     return render(request, 'app1/number.html', context)

