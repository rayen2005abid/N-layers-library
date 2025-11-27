from flask import Flask, render_template, request, redirect
from data_access import DataAccessLayer
from business import BusinessLogicLayer

app = Flask(__name__)

dal = DataAccessLayer()
bll = BusinessLogicLayer(dal)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""

    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")

        ok, message = bll.add_book(title, author)

    books = bll.get_books()
    return render_template("index.html", books=books, message=message)

@app.route("/delete/<int:book_id>")
def delete(book_id):
    bll.delete_book(book_id)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
