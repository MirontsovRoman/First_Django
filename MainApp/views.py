from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

author = {"Имя": "Роман",
    "Отчество": "Сергеевич",
    "Фамилия": "Миронцов",
    "телефон": "8-910-477-01-89",
    "email": "roma419@mail.ru"
}

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]



def home(request):
    # text = """<h1>"Изучаем django"</h1>
    #           <strong>Автор</strong>: <i>Миронцов Р.С.</i>
    #        """
    # return HttpResponse(text)
    context = {
        "name": "Петров Иван Николаевич",
        "email": "my_mail@mail.ru"
    }
    return render(request, "index.html", context)


def about(request):
    result = f"""
    Имя: <b>{author['Имя']}</b><br>
    Отчество: <b>{author['Отчество']}</b><br>
    Фамилия: <b>{author['Фамилия']}</b><br>
    телефон: <b>{author['телефон']}</b><br>
    email: <b>{author['email']}</b><br><br>
    <a href='/'> Home </a>
    """
           
    return HttpResponse(result)


def get_item(request, item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        context = {
            "item": item
        }
        return render(request, "item-page.html", context)
    return HttpResponseNotFound(f'Item with id = {item_id} not found.')    


def items_list(request):
    context = {
        "items": items
    }
    return render(request, "items-list.html", context)