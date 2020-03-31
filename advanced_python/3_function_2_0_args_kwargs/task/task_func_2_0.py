class Contact:
    def __init__(self, name, surname, number_phone, *args, favorite_contact=False, **kwargs):
        self.name = name
        self.surname = surname
        self.number_phone = number_phone
        self.favorite_contact = favorite_contact

        if not self.favorite_contact:
            self.favorite_contact = 'нет'
        else:
            self.favorite_contact = self.favorite_contact

        self.info = ''
        for item in args:
            self.info += f'{"":5}{item}\n'
        for key, value in kwargs.items():
            self.info = self.info + f'{"":5}{key} : {value}\n'

    def __str__(self):
        str_print = f'Имя: {self.name}\n' \
                    f'Фамилия: {self.surname}\n' \
                    f'В избранных: {self.favorite_contact}\n' \
                    f'Дополнительная информация:\n' \
                    f'{self.info}'
        return str_print


if __name__ == '__main__':
    jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    print(jhon)
