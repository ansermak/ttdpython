from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item


def home_page(request):
    if request.method == 'POST':
        item_text = request.POST.get('item_text', '')
        Item.objects.create(text=item_text)
        return redirect('/lists/the-only-list-in-the-world/')

    items = Item.objects.all()
    return render(
        request,
        'lists/home.html',
        {'items': items})


def view_list(request):
    items = Item.objects.all()
    return render(request, 'lists/list.html', {'items': items})
