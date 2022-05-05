from flask import Flask, render_template, redirect, url_for, request
from database import Database
from todo import Todo
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from datetime import datetime

app = Flask(__name__)

# class MyForm(FlaskForm):
#     name = StringField('name', validators=[DataRequired()])


@app.route("/", methods=["POST", "GET"])
def home():
    db = Database()
    todos = db.get_todos()
    if request.method == "POST":
        new_todo = Todo(request.form["title"], datetime.now().strftime("%d/%m/%Y"))
        db.add_todo(new_todo)
        return redirect(url_for("home"))

    return render_template("index.html", todos=todos)


@app.route("/delete/<int:id>")
def delete_todo(id):
    db = Database()
    db.delete_todo(id)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
