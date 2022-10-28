from flask import Flask, render_template, url_for, redirect, request
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
"""Mongo Db Starts"""
client = MongoClient("mongodb://localhost:27017") #connect
db = client.flask_db #database
todos = db.todos #collection
"""Mongo Db Ends"""
app.secret_key = "arunisto"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        content = request.form['content']
        degree = request.form['degree']
        todos.insert_one({"content":content, 'degree':degree})
        return redirect(url_for('index'))
    all_todos = todos.find()
    return render_template("index.html", todo=all_todos)

@app.route("/<id>/delete/", methods=["POST"])
def delete(id):
    todos.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)