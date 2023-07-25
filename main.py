from datetime import datetime
class project:
    def __init__(self, name, start_date, end_date, programmers):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.programmers = programmers


    def __str__(self):
        return f'Название:  {self.name}\n' \
               f'Дата начала:  {self.start_date}\n' \
               f'Дата окончания:  {self.end_date}\n' \
               f'Список программистов:  {self.programmers}\n'

    def handle_date(self, date):
        self.end_date = date

project1 = project("NEWSPROJECT", datetime.now(),datetime(2024, 1, 1, 0, 0 ), ['Иван', 'Петр', 'Сидор', 'Сергей', 'Алексей', 'Михаил'])
print("------------------------------------------------")
print(project1.__str__(), end='\n\n')
print("------------------------------------------------")

project1.handle_date(datetime(2023, 12, 31, 0, 0))
print(project1, end='\n\n')
print("------------------------------------------------")
project1.programmers.append('Саша')
print(project1, end='\n\n')
print("------------------------------------------------")
project1.programmers.remove('Иван')
print(project1, end='\n\n')