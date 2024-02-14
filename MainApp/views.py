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
    text = """<h1>"Изучаем django"</h1>
              <strong>Автор</strong>: <i>Миронцов Р.С.</i>
           """
    return HttpResponse(text)


def about(request):
    result = f"""
    Имя: <b>{author['Имя']}</b><br>
    Отчество: <b>{author['Отчество']}</b><br>
    Фамилия: <b>{author['Фамилия']}</b><br>
    телефон: <b>{author['телефон']}</b><br>
    email: <b>{author['email']}</b><br>
    """
           
    return HttpResponse(result)


def get_item(request, id):
    for item in items:
        if item["id"] == id:
            result = f""" 
            <h2>Имя: {item["name"]}</h2
            <p> Количество: {item["quantity"]} </p>
            """
            return HttpResponse(result)
    return HttpResponseNotFound(f'Item with id = {id} not found.')    