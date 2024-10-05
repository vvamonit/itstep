import datetime


class Student:
    name = ''
    year_of_birth = ''
    group = ''
    average_score = ''

    def __init__(self, name, year_of_birth, group, average_score):
        self.name = name
        self.year_of_birth = year_of_birth
        self.group = group
        self.average_score = average_score

    def show_stats(self):
        print(self)

    def __str__(self):
        return f" --{self.name} --\nРік народження: {self.year_of_birth}\n" \
               f"Група: {self.group}\nСередній бал: {self.average_score} "
    def get_age(self):
        current_year = datetime.datetime.now().year
        return current_year - self.year_of_birth