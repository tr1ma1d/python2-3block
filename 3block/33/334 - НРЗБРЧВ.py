translated_text = ""


def translate(text):
    global translated_text

    letters = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е',
               'А', 'У', 'О', 'Ы', 'И', 'Э', 'Я', 'Ю', 'Ё', 'Е',
               '.', ',', '-']
    for letter in text:
        if letter not in letters:
            translated_text += letter

    translated_text = ' '.join(translated_text.split())
    return translated_text


def main():

    translate("Удивительный факт, но текст на языке НЕРАЗБОРЧИВО оказывается довольно просто читать. "
              "Достаточно небольшой тренировки - и вы сможете это делать.")
    print(translated_text)


main()
