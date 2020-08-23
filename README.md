Это решение задания: **запуск автотестов для разных языков интерфейса** в рамках курса **Автоматизация тестирования с помощью Selenium и Python** на [stepic.org](https://stepik.org/course/575/syllabus).

Ссылка на страницу с заданием: https://stepik.org/lesson/237240/step/9?unit=209628

###Как запустить проект (на Linux/macOS)

1. Склонировать себе репозиторий
2. Поднять виртуальное окружение. Например, командой:
```python
python -m venv test_env
```
3. Активировать окружение:
```python
python test_env/bin/activate
```
4. Установить зависимости:
```python
pip install -r requirements.txt
```
5. Запустить тест:
```python
pytest --language=fr test_items.py
```
В качестве --language можно передавать различные локали, например es, ru, ar, it и т.д.