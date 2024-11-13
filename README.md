# CLI Менеджер Задач

Простой командный интерфейс (CLI) для управления задачами.

## Установка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/ваше_имя/todo-cli.git
    ```

2. Перейдите в директорию проекта:

    ```bash
    cd todo-cli
    ```

3. (Опционально) Создайте виртуальное окружение и установите зависимости:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

## Использование

### Добавить задачу
```bash
python todo.py add "Описание вашей задачи"
```
```bash
python todo.py list
```
```bash
python todo.py complete <ID_задачи>
```
```bash
python todo.py delete <ID_задачи>
```
```bash
python todo.py add "Купить продукты"
python todo.py list
python todo.py complete 1
python todo.py delete 1
```
