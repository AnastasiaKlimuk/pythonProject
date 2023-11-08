from pydantic import BaseModel, validator  #, Field    #это библиотека , которая предоставляет ряд функций проверки и анализа данных

class Post(BaseModel):
    id: int #= Field(le=2)
    title: str
#     name: str = Field(alias="_name")                 #аргумент alias в функции Field - работать со snake_case в python и с любым другим форматом извне

# та же самая валидация, что и = Field(le=2)
    @validator("id")
    def Check_that_id_less_then_two(cls, v):           #cls — это стандартное имя первого аргумента методов класса
        if v > 2:
            raise ValueError('Id is not less than two')
        else:
            return v



##[{'id': 1, 'title': 'Post 1', '_name': 'Igor'}