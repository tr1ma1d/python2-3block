name = ''
date = ''


def setup_profile(setup_name, setup_date):
    global name
    name = setup_name
    global date
    date = setup_date


def print_application_for_leave():
    print(f'Заявление на отпуск в период {date}. {name}')


def print_holiday_money_claim(money):
    print(f'Прошу выплатить {money} отпускных денег. {name}')


def print_attorney_letter(deputy_name):
    print(f'На время отпуска в период {date} моим заместителем назначается {deputy_name}. {name}')


def main():
    setup_profile("Иван Петров", "1 июня – 20 июня")
    print_application_for_leave()
    print_application_for_leave()
    print_holiday_money_claim("15 тысяч пиастров")
    print_attorney_letter("Василий Васильев")


main()
