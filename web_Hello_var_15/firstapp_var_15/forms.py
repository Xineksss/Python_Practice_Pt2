from django.forms import CharField, Form

class UserForm(Form):
    name=CharField(label= "Имя клиента")
    surname=CharField(label= "Фамилия клиента")
