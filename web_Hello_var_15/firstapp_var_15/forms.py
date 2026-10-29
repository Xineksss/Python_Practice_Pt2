from django.forms import Form
from django.forms import CharField
from django.forms import MultipleChoiceField
from django.forms import IntegerField
from django.forms import CheckboxSelectMultiple
from django.forms import ChoiceField


class UserForm(Form):
     name = CharField(label="Имя клиента")
     surname = CharField(label="Фамилия клиента")


class PurchaseForm(Form):
    name = CharField(label="Ваше имя")
    quantity = IntegerField(label="Количество")

    # Выбор одного варианта
    component = ChoiceField(
        label="Комплектующее",
        choices=[
            ('Видеокарта', 'Видеокарта'),
            ('Процессор', 'Процессор'),
            ('Материнская плата', 'Материнская плата'),
            ('Корпус', 'Корпус'),
            ('HDD', 'HDD'),
            ('SSD', 'SSD'),
            ('Оперативная память', 'Оперативная память'),
            ('Блок питания', 'Блок питания'),
        ]
    )

    # Выбор нескольких вариантов (галочки)
    extras = MultipleChoiceField(
        label="Дополнительно",
        choices=[
            ('Гарантия', 'Гарантия'),
            ('Доставка', 'Доставка'),
            ('Сборка', 'Сборка')
        ],
        widget=CheckboxSelectMultiple,
        required=False
    )