from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item


def home_page(request):
    if request.method == 'POST':
        item_text = request.POST.get('item_text', '')
        Item.objects.create(text=item_text)
        return redirect('/')

    items = Item.objects.all()
    return render(
        request,
        'lists/home.html',
        {'items': items})
