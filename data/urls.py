
class Urls:
    MAIN_URL = 'https://qa-stellarburgers.education-services.ru'
    URL_REGISTRATION = '/api/auth/register' # создание/регистрация польз
    URL_LOGIN = '/api/auth/login' # авторизация польз
    CHANGE_USER_DATA = '/api/auth/user' # изменение данных польз
    DELETE_USER = '/api/auth/user' # удаление данных о пользователе
    URL_CREATE_ORDER = '/api/orders' # создание заказа
    URL_GET_USER_ORDERS = '/api/orders' # получение заказа
    headers = {"Content-Type": "application/json"}
    