from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegisterForm  # Импортируем форму, созданную ранее

# Псевдо-список существующих пользователей
users = ["alice", "bob", "charlie"]

def sign_up_by_html(request):
    info = {}  # Пустой словарь для контекста

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age', 0))  # По умолчанию 0, если поле пустое

        # Проверка условий
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            # Если всё в порядке, возвращаем приветствие
            return HttpResponse(f"Приветствуем, {username}!")

    return render(request, 'registration_page.html', context=info)

def sign_up_by_django(request):
    info = {}  # Пустой словарь для контекста

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            # Проверка условий
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                # Если всё в порядке, возвращаем приветствие
                return HttpResponse(f"Приветствуем, {username}!")
        else:
            info['error'] = 'Некорректные данные формы'
    else:
        form = UserRegisterForm()

    info['form'] = form  # Добавляем форму в контекст
    return render(request, 'registration_page.html', context=info)