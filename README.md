# flask-VisitorBook

#  Visitor Book – Flask-Based Web Application

This is a simple yet effective web application built with **Flask** that allows users to leave a message in a digital visitor book. They can enter their name, message, rating, and some additional information. The data is stored in JSON format and can be viewed, deleted, or restored later.

This project is a great example of a lightweight CRUD (Create, Read, Update, Delete) system for those learning Flask or building small-scale feedback systems.

---

##  Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Who Is It For?](#who-is-it-for)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation & Usage](#installation--usage)
- [License](#license)

---

##  About the Project

This web app allows users to fill out a form with:

- Name
- Email (optional)
- Location (City / Country)
- Topic
- Message
- Rating (1 to 5 stars)

All entries are saved in `data.json`. Deleted entries are moved to `trash.json`, and can be restored later. Each entry is timestamped and assigned a unique UUID.

---

##  Features

| Feature           | Description |
|-------------------|-------------|
|  Add Entries    | Users submit form data |
|  View History   | `/history` page lists all past entries |
|  Delete Entry  | `/delete/<id>` removes entry and moves it to trash |
|  Undo Delete   | `/undo/<id>` restores deleted entry |
|  Timestamping   | Each entry includes date and time |
|  Unique UUID   | Each entry has a unique identifier |
|  HTML Interface | User-friendly and clean UI with forms |

---

##  Who Is It For?

- Developers learning **Flask**
- Personal website owners who want to add a guestbook
- Event organizers collecting visitor comments
- Developers building a simple feedback system

---

##  Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python** | Main programming language |
| **Flask**  | Web framework |
| **HTML/CSS** | UI layout and styling |
| **JSON**   | Data storage (instead of a database) |
| **UUID**   | Generating unique IDs |
| **datetime** | Tracking entry time |

---

##  Project Structure

VisitorBook/

    app.py      # Main Flask app
    data.json   # Saved entries (auto-generated)
    trash.json  # Deleted entries (auto-generated)
    visits.txt  # Example visitor list (optional)
    
    templates/        # HTML templates
        index.html    # Main form page
        greet.html    # Thank-you page after submission
        history.html  # Entry listing (you can add it)
        deleted.html  # Message after deleting
        
    static/
        style.css     # Styling (if exists)

##  Installation & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/flask-VisitorBook.git
cd flask-VisitorBook
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install flask
```

### 4. Run the Application
```bash
python3 app.py
```

### 5. Open in Your Browser
```bash
Visit: http://localhost:5000
```

### 6. When you're done working in the virtual environment, leave it using:
```bash
deactivate
```

##  License
This project is open-source and provided under the MIT License. You are free to use, modify, and distribute it.

