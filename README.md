# 📝 ToDoList

**ToDoList** is a simple Django-based web application for managing your daily tasks.  
You can create tasks, mark them as complete or incomplete, set optional deadlines, and categorize them using tags.

---

## ⚙️ Features

- ✅ Create, update, and delete tasks
- 🗓 Set optional deadlines
- 🔁 Toggle task completion status
- 🏷 Create, update, and delete tags, tasks
- 🎨 Clean and minimal UI with Bootstrap

---

## 🛠 Technologies

- Python 3.x
- Django 5.x
- SQLite
- HTML5 / CSS3 / Bootstrap

---

## 🚀 Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/todolist.git
cd todolist

# 2. Create a virtual environment
python -m venv venv

# 3. Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Apply migrations
python manage.py migrate

# 6. Run the development server
python manage.py runserver
