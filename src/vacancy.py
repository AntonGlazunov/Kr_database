class Vacancy:
    """Класс для работы с вакансиями"""
    name: str
    area_name: str
    alternate_url: str
    requirement: str
    responsibility: str
    list_object_vacancy = []

    def __init__(self, name, type_, alternate_url, requirement, responsibility, salary=None):
        self.name = name
        self.type_ = type_
        self.alternate_url = alternate_url
        self.requirement = requirement
        self.responsibility = responsibility
        if salary is None:
            self.salary = 0
            self.salary_min = 0
            self.salary_max = 0
        else:
            self.salary = salary
            if self.salary.get("from") is not None:
                self.salary_min = salary.get("from")
            else:
                self.salary_min = 0
            if self.salary.get("to") is not None:
                self.salary_max = salary.get("to")
            else:
                self.salary_max = 0
        Vacancy.list_object_vacancy.append(self)

    @classmethod
    def sort_vacancy_salary_min(cls):
        """Сортировака по минимальной зарплате"""
        Vacancy.list_object_vacancy.sort(key=lambda sort_vacancy: sort_vacancy.salary_min, reverse=True)

    @classmethod
    def sort_vacancy_salary_max(cls):
        """Сортировака по максимальной зарплате"""
        Vacancy.list_object_vacancy.sort(key=lambda sort_vacancy: sort_vacancy.salary_max, reverse=True)

    def __str__(self):
        return f"Вакансия: {self.name}, ссылка: {self.alternate_url}, предлагаемая зарплата: от {self.salary_min} рублей"