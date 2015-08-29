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
# with text and it will be linked to the list. list=list_
def new_list(request):
    # list_ = List.objects.create()
    # item = Item.objects.create(text=request.POST['text'], list=list_)
    # try:
    #     item.full_clean()
    #     item.save()
    # except ValidationError:
    #     list_.delete()
    #     error = "You can't have an empty list item"
    #     return render(request, 'home.html', {"error": error})
    # return redirect(list_)
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        Item.objects.create(text=request.POST['text'], list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {"form": form})


# view a particular list

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(data=request.POST)
        if form.is_valid():
            Item.objects.create(text=request.POST['text'], list=list_)
            return redirect(list_)
    return render(request, 'list.html', {'list': list_, "form": form})
