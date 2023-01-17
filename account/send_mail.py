from django.core.mail import send_mail


def send_confirmation_email(user, code):
    full_link = f'http://localhost:8000/api/v1/accounts/activate/{code}/'
    send_mail(
        'Здравствуйте! Активируйте Ваш аккаунт!',
        f'Чтобы активировать Ваш аккаунт нужно перейти по ссылке: \n{full_link}',
        'eldiiar.ps@gmail.com',
        [user],
        fail_silently=False
    )