def send_email(message, recipient, sender = "university.help@gmail.com"):
    if recipient.endswith("@" and ".com" or ".ru" or ".net" not in recipient or sender):
        print(f"Невозможно отправить письмо с адреса {sender}на адрес {recipient}")
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса{sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

send_email('messagje', 'vasyok1337@gmail.com')
send_email('messagje', '@.com', 'vasyok1337@gmail.com')
send_email('messagje', 'university.help@gmail.')
send_email('messagje', 'university.help@gmail.com')

# message(сообщение), recipient(получатель) и sender = "univerity.help@gmail.com"
