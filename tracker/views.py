from django.shortcuts import render, redirect, get_object_or_404
from .models import TrackingHistory, CurrentBalance
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        description = request.POST.get('description')

        if not description:
            messages.error(request, "Description cannot be empty")
            return redirect('index')
        
        raw_amount = (request.POST.get('amount'))

        try:
            amount = float(raw_amount)
        except (TypeError, ValueError):
            messages.error(request, "Invalid amount")
            return redirect('index')
        
        if amount == 0:
            messages.error(request, 'Amount can not Be Zero')
            return redirect('index')
            
        expense_type = 'DEBIT' if amount < 0 else 'CREDIT'
        
        current_balance, _   = CurrentBalance.objects.get_or_create(id = 1)
        
        tracking_history = TrackingHistory.objects.create(
            description=description,
            amount=amount,
            expense_type=expense_type,
            current_balance = current_balance,
        )
        current_balance.current_balance += float(tracking_history.amount)
        current_balance.save()
        
        messages.success(request, "Transaction added successfully")
        return redirect('/tracker')


    current_balance, _ = CurrentBalance.objects.get_or_create(id = 1)
    transactions = TrackingHistory.objects.all().order_by('-id')
    income = 0
    expence = 0
    for tracking_history in TrackingHistory.objects.all():
        if tracking_history.expense_type == "DEBIT":
            expence += tracking_history.amount
        else:
            income += tracking_history.amount
            
            
    return render(request, 'tracker/index.html', {
        'transactions': transactions,
        'current_balance': current_balance,
        'expence' : expence,
        'income' : income,
    })

    
def delete_transaction(request, id):
    if request.method == "POST":
        transaction = get_object_or_404(TrackingHistory, id=id)
        balance = transaction.current_balance

        balance.current_balance -= float(transaction.amount)
        balance.save()

        transaction.delete()
        messages.warning(request, "Transaction deleted")

    return redirect('index')

def delete_all_transactions(request):
    if request.method == "POST":
        if not TrackingHistory.objects.exists():
            messages.warning(request, "No transactions to delete")
            return redirect('index')

        TrackingHistory.objects.all().delete()

        current_balance, _ = CurrentBalance.objects.get_or_create(id=1)
        current_balance.current_balance = 0
        current_balance.save()

        messages.success(request, "All transactions deleted")

    return redirect('index')
