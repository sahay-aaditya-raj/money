from django.shortcuts import render, redirect
from .models import Entry, Payement, ExpenseType
from datetime import datetime
from django.db.models import Sum
from django.db.models import Q
# Get today's date
today = datetime.today().date()

# Create your views here.


def homepage(request):
    return render(request, 'home.html')

def new_entry(request):
    dropdown = Payement.objects.all()
    message = None
    exp_type = ExpenseType.objects.all()
    
    if request.method == 'POST':
        print(request.POST.get('date') == '')
        if request.POST.get('p-Drop') == 'Empty' or request.POST.get('exp_type') == 'Empty':
            message = 'neg'
        else:
            try:
                try:
                    amount=float(request.POST.get('amount'))
                    exp = ExpenseType.objects.get(expense_type=request.POST.get('exp_type'))
                    type = Payement.objects.get(type=request.POST.get('p-Drop'))
                    if request.POST.get('date') == '':
                        date = today
                    else:
                        date = request.POST.get('date')
                    ent = Entry.objects.create(type = type,
                                               exp_type = exp,
                                                description = request.POST.get('description'),
                                                amount = amount,
                                                date = date)
                    message = 'pos'
                except: 
                    message = 'amount'
            except:
                message = 'error'           
                
            
    context = {'dropdown': dropdown, 'msg': message, 'exp_type': exp_type}
    return render(request, 'new_entry.html', context)


def view(request):
    print(f"from:{request.POST.get('from')}")
    print(f"to:{request.POST.get('to')}")
    print(f"type:{request.POST.get('type')}")
    print(f"order:{request.POST.get('order')}")
    entries = Entry.objects.all()
    if request.POST.get('from') == None :
        pass
    elif request.POST.get('from') == '':
        pass
    else:
        fr = request.POST.get('from')
        entries = entries.filter(date__gte=fr)
        
    if request.POST.get('to') == None :
        pass
    elif request.POST.get('to') == '':
        pass
    else:
        to = request.POST.get('to')
        entries = entries.filter(date__lte=to)
        
    if request.POST.get('type') != None:
        ty = request.POST.get('type')
        entries = entries.filter(exp_type__expense_type__contains=ty)
        
        
    if request.POST.get('order') == 'asc-date':
        entries = entries.order_by('date')
    elif request.POST.get('order') == 'desc-date':
        entries = entries.order_by('-date')
    elif request.POST.get('order') == 'asc-amt':
        entries = entries.order_by('amount')
    elif request.POST.get('order') == 'desc-amt':
        entries = entries.order_by('-amount')
    
        
    
    
    count = entries.count()
    total = entries.aggregate(total_sum=Sum('amount'))['total_sum'] # to get sum
    context ={'entries': entries , 'count': count, 'total':total}
    return render(request, 'view.html', context)

def view_data(request, pk):
    entry = Entry.objects.get(id=pk)
    context = {'entry': entry}
    return render(request, 'view_data.html', context)

def delete_data(request, pk):
    try:
        entry = Entry.objects.get(id=pk)
        entry.delete()
    except:
        pass
    return redirect('home')