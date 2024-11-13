import argparse
import json
import os

TASKS_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    tasks = load_tasks()
    task = {'id': len(tasks) + 1, 'description': description, 'completed': False}
    tasks.append(task)
    save_tasks(tasks)
    print(f"Задача добавлена: {description}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Список задач пуст.")
        return
    for task in tasks:
        status = '✓' if task['completed'] else '✗'
        print(f"{task['id']}. [{status}] {task['description']}")

def complete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            save_tasks(tasks)
            print(f"Задача {task_id} отмечена как выполненная.")
            return
    print(f"Задача с ID {task_id} не найдена.")

def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    print(f"Задача {task_id} удалена.")

def main():
    parser = argparse.ArgumentParser(description="CLI Менеджер Задач")
    subparsers = parser.add_subparsers(dest='command')

    # Добавить задачу
    parser_add = subparsers.add_parser('add', help='Добавить новую задачу')
    parser_add.add_argument('description', type=str, help='Описание задачи')

    # Просмотреть задачи
    parser_list = subparsers.add_parser('list', help='Просмотреть все задачи')

    # Отметить задачу как выполненную
    parser_complete = subparsers.add_parser('complete', help='Отметить задачу как выполненную')
    parser_complete.add_argument('id', type=int, help='ID задачи')

    # Удалить задачу
    parser_delete = subparsers.add_parser('delete', help='Удалить задачу')
    parser_delete.add_argument('id', type=int, help='ID задачи')

    args = parser.parse_args()

    if args.command == 'add':
        add_task(args.description)
    elif args.command == 'list':
        list_tasks()
    elif args.command == 'complete':
        complete_task(args.id)
    elif args.command == 'delete':
        delete_task(args.id)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()