# Todo List CLI Application

This is a simple command line interface (CLI) application for managing a to-do list. You can add tasks, remove tasks, and show all the tasks in the list.

## Requirements

- Python 3

Sure, here's an expanded version of the installation section for the Todo list CLI application:

## Installation

1. Clone the repository or download the source code:

   ```
   git clone https://github.com/BitH0xker/ToDo-List.git
   ```

   Alternatively, you can download the source code as a ZIP file from the repository's main page on GitHub and extract it to a directory on your computer.

2. Install Python 3 if it's not already installed. You can download the latest version of Python 3 from the official website: https://www.python.org/downloads/

   If you're not sure whether Python 3 is installed on your system, you can check by running the following command in a terminal or command prompt:

   ```
   python3 --version
   ```

   If Python 3 is installed, the command will display the version number. If it's not installed, you will see an error message.

3. Open a terminal or command prompt and navigate to the directory where the source code is located:

   ```
   cd todo-list-cli
   ```

4. Create a virtual environment for the project (optional):

   ```
   python3 -m venv venv
   ```

   This will create a new virtual environment named "venv" in the project directory. You can activate the virtual environment by running the following command:

   ```
   source venv/bin/activate
   ```

5. Run the following command to start the application:

   ```
   python3 todo.py
   ```

   You should now see the prompt for the Todo list CLI application, and you can start managing your to-do list!

## Usage

When you run the application, you will be prompted to enter a command. Here are the available commands:

- `add`: Add a task to the list.
- `remove`: Remove a task from the list.
- `show`: Show all the tasks in the list.
- `quit`: Quit the application.

## Examples

To add a task, type `add` at the prompt and then enter the task:

```
Enter command (add/remove/show/quit): add
Enter task: Buy groceries
Task added: Buy groceries
Enter command (add/remove/show/quit): 
```

To remove a task, type `remove` at the prompt and then enter the task:

```
Enter command (add/remove/show/quit): remove
Enter task: Buy groceries
Task removed: Buy groceries
Enter command (add/remove/show/quit): 
```

To show all the tasks in the list, type `show` at the prompt:

```
Enter command (add/remove/show/quit): show
Tasks:
- Do laundry
- Clean the house
Enter command (add/remove/show/quit): 
```

To quit the application, type `quit` at the prompt:

```
Enter command (add/remove/show/quit): quit
```

## License

This project is licensed under the GNU License - see the [LICENSE.txt](LICENSE.txt) file for details.
