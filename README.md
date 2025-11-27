# 📚 Library Management System

A simple Flask + SQLite web application that lets users add books through an HTML interface and store them locally in a database.

## 🚀 Features

* Add books (title + author) using a web form
* Store books in a local SQLite database
* Display all stored books in a table
* Lightweight, easy to run — no external database required

## 🗂 Project Structure

```
project/
│
├── app.py               # Main Flask application
├── requirements.txt     # Dependencies
└── templates/
      └── index.html     # HTML interface (Jinja2)
```

## 🧰 Requirements

Before running the app, ensure you have:

* Python 3.8+
* Pip package manager
* A terminal/command prompt

Install the required packages:

```bash
pip install -r requirements.txt
```

## ▶️ How to Run the Application

### 1. Download / Clone the project

```bash
git clone <your-repo-link>
cd project
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Flask server

```bash
python app.py
```

You should see something like:

```
 * Running on http://127.0.0.1:5000
```

### 4. Open the application in your browser

Go to:

```
http://127.0.0.1:5000
```

⚠️ **Do NOT open the HTML file directly** (`file://…`) — It must run through Flask for the form to work properly.

## 🗃 Database Information (SQLite)

The application automatically creates:

```
books.db
```

### ▶️ Database Table Structure

| Column | Type |
|--------|------|
| id | INTEGER PRIMARY KEY AUTOINCREMENT |
| title | TEXT |
| author | TEXT |

No manual setup needed — the database initializes itself automatically.

## 📝 How to Add a Book

1. Open the homepage
2. Fill in:
   * Book Title
   * Author
3. Click **Add**
4. The new book will appear in the table below the form.

## 🐞 Troubleshooting

### 1. Form not sending data

* Make sure you're opening: `http://127.0.0.1:5000`
* Ensure `index.html` is inside a folder named `templates/`
* Check form attributes: `method="POST"` and `action="/"`

### 2. Flask not running

Try:

```bash
pip install Flask
python app.py
```

### 3. Database not updating

Delete the file:

```bash
books.db
```

Then restart the app — it will be recreated automatically.

## 📄 License

This project is free to use for learning, assignments, or university work.
