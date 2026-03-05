import argparse
from lib.models import Task, User

users = {}

def add_task(args):
    if args.user not in users:
        users[args.user] = User(args.user)
        print(f"Created new user: {args.user}")
    
    task = Task(args.title)
    users[args.user].add_task(task)

def complete_task(args):
    if args.user not in users:
        print(f"User '{args.user}' not found.")
        return
    
    user = users[args.user]
    
    for task in user.tasks:
        if task.title.lower() == args.title.lower():
            task.complete()
            return
    
    print(f"Task '{args.title}' not found for {args.user}.")

def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers()

    add_parser = subparsers.add_parser("add-task", help="Add a task for a user")
    add_parser.add_argument("user")
    add_parser.add_argument("title")
    add_parser.set_defaults(func=add_task)

    complete_parser = subparsers.add_parser("complete-task", help="Complete a user's task")
    complete_parser.add_argument("user")
    complete_parser.add_argument("title")
    complete_parser.set_defaults(func=complete_task)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()