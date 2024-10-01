## Дипломный проект. Задание 3: веб-приложение

### Автотесты для проверки функциональности веб-приложения Stellar Burgers в браузерах Google Chrome и Mozilla Firefox.

### Стректура проекта:

- `locators` - дирректория локаторов
- `pages` - дирректория методов страниц
- `tests` - дирректория тестов

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Команда для запуска**

> `pytest -v`
 
**Создание allure отчета** 

> `$ pytest tests --alluredir=allure_results`
 
**Открыть allure отчет в формате веб страницы**

> `$ allure serve allure_results`
