from src.enums.global_enums import GlobalErrorMessages #атрибут класса для эррор месседжей

class Response_test_two:                                     #класс для респонса

    def __init__(self, response):                   #функция для получения респонса. __init__(self, ...) — метод класса, который инициализирует созданный объект.
        self.response = response                    #получение респонса
        self.response_json = response.json().get('data')       #перевод респонса в формат json и извлечение даты
        self.response_status = response.status_code #получение статус кода респонса

    def validate(self, schema):                    #функция для валидации респонса в соответствии со схемой
        if isinstance(self.response_json, list):   #isinstance - проверяет, является ли объект экземпляром указанного класса или его подкласса
            for item in self.response_json:
                schema.parse_obj(item)                       #для метода валидации pydentic
                ## validate(item, schema)          #для метода валидации с json schema
        else:
            schema.parse_obj(self.response_json)             #для метода валидации pydentic
            ##validate(self.response_json, schema) #для метода валидации с json schema
            return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, self #assert - это булевы выражения, которые проверяют, является ли условие истинным "assert condition, message"
        else:
            assert self.response_status == status_code, self
        return self

    def __str__(self):  #позволяет кастомизировать ответ после теста
        return \
            f"\nStatus code: {self.response_status} \n" \
            f"Requested url: {self.response.url} \n" \
            f"Response body:{self.response_json}"