from enum import Enum #трибуты класса Enum конвертируются в экземпляры при парсинге.
                      #Каждый экземпляр имеет параметр name, в котором хранится название, а также value

class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Received status code is not equal to expected"
    WRONG_ELEMENT_COUNT = "Number of items is not equal to expected"