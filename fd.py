current_year = 2021class Person:    __total_person = 0    def __init__(self,name, birght_year, **kwargs):        self.__name = name        self.__birght_year = birght_year        self.language = kwargs.get("language")        self.year = current_year - self.__birght_year        Person.__total_person += 1        # if self.__birght_year > current_year:        #        raise TypeError ("Mistake")    def is_abult(self):        if current_year - self.__birght_year >= 18:            return True        return False    def get_age(self):        self.year = current_year - self.__birght_year        if self.year > 0:            print(f'Your age {self.year}')        else:            print(f'Your age {self.year}')    @classmethod    def get_total_person(cls):        return cls.__total_person    def talk(self):        print(f"{self.__name}says Hello world!")    def print_language(self):        print(f"{self.__name}'s language:{self.language}")class Teacher(Person):    '''child class Teacher'''    def talk(self):        print("Greetings,{self.name} your teacher")    def teach(self):        print("Lesson started by Teacher")d1 = Person('Aidai', 1994, launguage='ENG')d2 = Person('Aiperi', 1992, launguage='RU')d3 = Person('Dariha', 1998, )e1 = Person('Mariyam', 2006, launguage='JAP')e2 = Person('Hadija', 2012, launguage='KG')e3 = Person('Bahiana', 2018, launguage='RU')print(d1.get_age())d1.talk()d1.print_language()print(d2.get_age())d2.talk()d2.print_language()print(d3.get_age())d3.talk()d3.print_language()print(e1.get_age())e1.talk()e1.print_language()print(e2.get_age())e2.talk()e2.print_language()print(e3.get_age())e3.talk()e3.print_language()print(e3.get_total_person())