#Создайте функцию send_email, которая принимает 2 обычных аргумента: message(сообщение), recipient(получатель) и
# 1 обязательно именованный аргумент со значением по умолчанию sender = "university.help@gmail.com".
def send_email(message, recipient, *, sender= 'university.help@gmail.com'):
    list_domen = ['.com','.ru','.net']
    index = 0
    index_ = recipient.rfind('.')
    rec_ok = ''
    if len(recipient)>3:
        rec_ok = recipient[index_:len(recipient)]
    sen_ok = ''
    index_ = sender.rfind('.')
    if len(sender)>3:
        sen_ok = sender[index_:len(sender)]
    # Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net", то вывести на экран(в консоль)
    # строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
    if (not ('@' in recipient) or not ('@' in sender)) or (not(rec_ok in list_domen) or not(sen_ok in list_domen)):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    # Если же sender и recipient совпадают, то вывести "Нельзя отправить письмо самому себе!"
    elif sender == recipient:
        print(f'Нельзя отправить письмо самому себе! Отправитель: {sender} = получатель: {recipient}!')
    # Если же отправитель по умолчанию - university.help@gmail.com, то вывести сообщение:
    # "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        # В противном случае вывести сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес
        # <recipient>."
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email('Это сообщение для проверки связи','vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
