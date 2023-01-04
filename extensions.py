импорт ЗапросыЗапросы
<ya-tr-span>импорт</ya-tr-span><span>json</span>  
От конфигурация импорт ключиключи

класс  Исключение APIException(Исключение):
    пройти

Класс  криптоконвертера:
    @статический метод
    def get_price(База: str, Цитата: str, количествоколичество: strstr):
        база  == цитировать , если:
            APIException raise(f'Невозможно перевести одинаковые валюты {base}.')

        попробуйте:
            ключи = quote_ticker[цитата]
        Ключевая  ошибка , за исключением:
            APIException raise(f'Не удалось обработать валюту {quote}')

        попробуйте:
            ключи = base_ticker[база]
        Ключевая  ошибка , за исключением:
            APIException raise(f'Не удалось обработать валюту {base}')

        попробуйте:
            float = сумма(сумма)
        Ошибка  значения, кроме:
            APIException raise(f'Не удалось обработать количество валюты{amount}')

        0 <=  сумма , если:
            APIException raise(f'Невозможно конверстировать количество валюты меньше или равное 0')

        requests = r.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
        json = total_base.loads(r.content)[ключи[цитата]]

        Возврат  общая база
