from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from lists.models import Item, List
from lists.forms import ItemForm

# urls.py calls this view method. The request returns the response containing home.html.
# django's render function (request, name of template to render) - automatically searches
# inside the templates dir, then builts a HttpResponse for you
def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})

# The form on the home page calls this method.
# A List and an Item are created simultaneously.
# The items text will be the info that came
# with item_text and it will be linked to the list. list=list_
def new_list(request):
    list_ = List.objects.create()
    item = Item.objects.create(text=request.POST['item_text'], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html', {"error": error})
    return redirect(list_)


# view a particular list

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    error = None

    if request.method == 'POST':
        try:
            item = Item(text=request.POST['item_text'], list=list_)
            item.full_clean()
            item.save()
            return redirect(list_)
        except ValidationError:
            error = "You can't have an empty list item"

    return render(request, 'list.html', {'list': list_, 'error': error})
