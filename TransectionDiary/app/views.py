from django.shortcuts import render
from .models import Cost
from .forms import CostEntryForm
import datetime


# Create your views here.
def home(request):
    add_record = False
    form = CostEntryForm()
    if request.method == 'POST':
        form = CostEntryForm(request.POST)
        if form.is_valid():
            newcost = form.save(commit=False)
            try:
                last_Entry = Cost.objects.latest('created')
                balance = last_Entry.balance
            except:
                balance = 0
            if form.cleaned_data.get('cost_type') == 'Cost':
                balance -= newcost.amount
            else:
                balance += newcost.amount
            newcost.balance = balance
            newcost.save()
            add_record = True

    today = datetime.datetime.now()
    costList = Cost.objects.filter(created__year=today.year,
                                   created__month=today.month)
    context = {'costs': costList, 'added': add_record, 'form': form}
    return render(request, 'index.html', context)
