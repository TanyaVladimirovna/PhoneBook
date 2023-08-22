class User:
    def __init__(self,
                 lastname = None, 
                 firstname = None, 
                 patronymic = None, 
                 name_organization = None, 
                 work_phone = None, 
                 personal_phone = None,
                 curr = None):
        if curr is None:
            self.lastname = lastname
            self.firstname = firstname
            self.patronymic = patronymic
            self.name_organization = name_organization
            self.work_phone = work_phone
            self.personal_phone = personal_phone
        else:
            self.lastname, self.firstname, self.patronymic, self.name_organization, self.work_phone, self.personal_phone = str(curr).replace(" ", '').split("|")
    
    def input_curr(self):
        self.lastname = input('lastname: ')
        self.firstname = input('firstname: ')
        self.patronymic = input('patronymic: ')
        self.name_organization = input('name organization: ')
        self.work_phone = input('work phone: ')
        self.personal_phone = input('personal phone: ')
    
    def __str__(self):
        return '{} | {} | {} | {} | {} | {}'.format(self.lastname,
                                                    self.firstname,
                                                    self.patronymic,
                                                    self.name_organization,
                                                    self.work_phone,
                                                    self.personal_phone) + '\n'

class PhoneBook:
    """ Вывод всех записей на экран из справочника """
    def show(self):
        with open('data.txt') as file:
            for line in file:
                user = User(curr = line)
                print(user)
    
    """ Поиск записи по имени и фамилии """
    def find(self, query):
        with open('data.txt') as file:
            for line in file:
                user = User(curr = line)
                if (user.lastname, user.firstname) == query:
                    return user
    
    """ Добавление новой записи в справочник """
    def add(self):
        user = User()
        user.input_curr()
        if PhoneBook().find(query = (user.lastname, user.firstname)) is None:
            file = open('data.txt', 'a')
            file.write('{} | {} | {} | {} | {} | {}'.format(user.lastname,
                                                            user.firstname,
                                                            user.patronymic,
                                                            user.name_organization,
                                                            user.work_phone,
                                                            user.personal_phone) + '\n')
            print('\nUser {lastName} {name} added successfully\n'.format(lastName = user.lastname,
                                                                          name = user.firstname))
            file.close()
        else:
            print('There is already such a contact')
    
    """ Изменение записей в справочнике """
    def change(self, query):
        print(PhoneBook().find(query = query))
       
        with open('data.txt', 'r') as f:
            old_data = f.read()
            input_search = input('search: ')
            input_replace = input('replace: ')
            new_data = old_data.replace(input_search, input_replace)
        
        with open('data.txt', 'w') as f:
            f.write(new_data)
                
def choice():
    selector = None
    try:
        selector = int(input('Input "1" if you want to find a contact\n' + \
                             'Input "2" if you want to add a new contact\n' + \
                             'Input "3" if you want to change the contact\n' + \
                             'Input "4" if you want to view the entire address book\n' + \
                             'Enter here ------->:'))
    except ValueError:
        print('\n\nIncorrect input!!!\n')
        print('You must enter an integer!!!\n\n')
    return selector

""" Создание экземпляра класса PhoneBook """
phone_book = PhoneBook()

""" Для того, чтобы посмотреть данные в справочнике, а также изменить данные,
    найти определённую запись, либо добавить запись, требуется ввести целое число, 
    соответствующее данной команде """
while True:
    selector = choice()
    if selector == 1:
        query = ((input('To search for a contact, enter his last name: ').capitalize(),
                  input('To search for a contact, enter his name: ').capitalize()))
        print(phone_book.find(query))
    elif selector == 2:
        phone_book.add()
    elif selector == 3:
        query = ((input('To change a contact, enter his last name: ').capitalize(),
                  input('To change a contact, enter its name: ').capitalize()))
        phone_book.change(query)
    elif selector == 4:
        phone_book.show()