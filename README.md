## !! DoDoingDone !!
A simple, pastel-themed To-Do List desktop application built with Python and Tkinter. Manage your daily tasks with ease—add, complete, delete, and filter them by date and status. The app features a clean, modern interface with a sidebar navigation and a friendly cat avatar.

https://img.shields.io/badge/Python-3.8%252B-blue
https://img.shields.io/badge/GUI-Tkinter-orange
https://img.shields.io/badge/License-MIT-green

## Features
- Add tasks with a title, due date, and priority (Low / Medium / High)

- Mark tasks as done – they get a strikethrough effect and move to the Completed view

- Delete tasks with a confirmation dialog

- Sidebar navigation – view Today's Tasks, All Tasks, Completed, and Settings

- Status bar showing pending, completed, and total task counts

- User notifications – subtle messages appear for actions like adding, deleting, or completing tasks

- Pastel color scheme – soft blues, creams, and playful typography for a friendly look

- Profile section – displays a cute avatar and username (customizable)

Note: Tasks are currently stored in memory only. They will be lost when the app closes. SQLite persistence is planned for a future update.

## Screenshots
Will add lated the works still in progresss!!

## Installation
Clone the repository

bash
git clone https://github.com/your-username/To-Do-List.git
cd To-Do-List
Ensure Python 3.8+ is installed (Tkinter is included with standard Python installations).

Place your avatar image
The app expects a file named cat_pfp.png in the project root. Replace it with any PNG you like (or keep the default cat).

Run the app

bash
python main.py
No additional libraries are required.

## File Structure
text
To-Do-List/
│
├── main.py          # Entry point – creates window and starts the app
├── ui.py            # All GUI code (widgets, event handlers, layout)
├── task_manager.py  # Data layer – CRUD operations (in-memory)
├── themes.py        # Color and font constants for consistent styling
├── cat_pfp.png      # Profile avatar image
└── README.md

## How It Works (Brief Overview)
main.py creates the main window, sets its size and title, then calls ui.showWidget(window) to build the interface.

ui.py is the largest module. It contains:

showWidget() – builds the entire UI inside the given window.

open_task_window() – creates a popup for adding new tasks.

refresh_task_list() – updates the task list based on the active view.

on_tree_click() – handles clicks on the checkbox and delete icon.

Helper functions for status bar, notifications, and active button highlighting.

task_manager.py holds the task data as a list of dictionaries and provides functions:

addTask(title, due_date, priority)

getTasks()

delete_task(task_id)

toggle_task(task_id)

themes.py centralizes all colors and fonts, making it easy to restyle the entire app.

## Roadmap / Planned Features
□ SQLite database – persistent storage (single user)
□ User login / signup – multi-user support with separate task lists
□ Subtasks – nested tasks with parent-child relationships
□ Dark mode and additional theme options
□ Search / filter tasks by text or priority
□ Undo delete functionality
□ Cat collision simulator – a fun Easter egg using task priorities
## Contributing
Contributions are welcome! If you'd like to improve the app, feel free to fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License – see the LICENSE file for details.

## Acknowledgements
Thanks to all open-source resources and the Python/Tkinter community.

Avatar image: cat_pfp.png (replace with your own if desired).

Feel free to adjust the repository URL, screenshot paths, or add your name in the credits. This README gives a clear overview and invites collaboration. 

