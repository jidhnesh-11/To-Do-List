import matplotlib.pyplot as plt

font_name ="Footlight MT Light"
plt.rcParams["font.family"] = "Arial"
'''
tasks = [
    {"id": 1, "title": "Buy milk",    "due_date": "2026-09-20", "priority": "high",   "done": False},
    {"id": 2, "title": "Read book",   "due_date": "2026-09-20", "priority": "low",    "done": True},
    {"id": 3, "title": "Call mom",    "due_date": "2026-09-20", "priority": "medium", "done": True},

    {"id": 4, "title": "Gym",         "due_date": "2026-09-21", "priority": "high",   "done": False},
    {"id": 5, "title": "Essay",       "due_date": "2026-09-21", "priority": "high",   "done": False},

    {"id": 6, "title": "Groceries",   "due_date": "2026-09-22", "priority": "medium", "done": True},
    {"id": 7, "title": "Study DBMS",  "due_date": "2026-09-22", "priority": "high",   "done": True},
    {"id": 8, "title": "Walk dog",    "due_date": "2026-09-22", "priority": "low",    "done": False},
    {"id": 9, "title": "Laundry",     "due_date": "2026-09-22", "priority": "low",    "done": True},

    {"id": 10, "title": "Project",    "due_date": "2026-09-23", "priority": "high",   "done": False},
    {"id": 11, "title": "Call friend", "due_date": "2026-09-23", "priority": "low",   "done": True},

    {"id": 12, "title": "Meeting",    "due_date": "2026-09-24", "priority": "medium", "done": False},
    {"id": 13, "title": "Submit HW",  "due_date": "2026-09-24", "priority": "high",   "done": False},
    {"id": 14, "title": "Read news",  "due_date": "2026-09-24", "priority": "low",    "done": True},
]
'''
def show_dashboard(tasks, completed_color,pending_color):
    if not tasks:
        print("No tasks to show.")
        return

    dates = sorted(set(t["due_date"] for t in tasks))

    totals    = [sum(1 for t in tasks if t["due_date"] == d) for d in dates]
    completed = [sum(1 for t in tasks if t["due_date"] == d and t["done"]) for d in dates]
    pending   = [total - comp for total, comp in zip(totals, completed)]

    plt.figure(figsize=(13, 6))
    
    plt.bar(dates, completed, width=0.2, color=completed_color, label="Completed")
    plt.bar(dates, pending,   width=0.2, bottom=completed, color=pending_color, label="Pending")
    
    plt.title("Task Completion Overview", fontsize=20, fontweight="bold")
    plt.xlabel("Due Date",           fontsize=14, fontweight="bold")
    plt.ylabel("Number of Tasks",    fontsize=14, fontweight="bold")
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(True)
    plt.show()
'''
show_dashboard(tasks,
                   completed_color="#10B981",   # soft green
                   pending_color="#EF4444")     # soft red
'''