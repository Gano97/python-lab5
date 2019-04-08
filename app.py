from flask import Flask, redirect, url_for, render_template, request
import db_interaction_file

app = Flask(__name__)


@app.route('/')
def main():
    return redirect(url_for("index"))

@app.route('/index')
def index():
    tasks= db_interaction_file.showTask()
    return render_template("index.html", list= tasks)

@app.route('/newTask', methods=["POST"])
def newTask():
    task_description= request.form["task_description"]
    urgent = False
    if request.form.get("urgent","") != "":
        urgent = True
    db_interaction_file.newTask(task_description, urgent)
    return redirect(url_for("index"))

@app.route('/removeTask/<task_id>')
def removeTask(task_id):
    db_interaction_file.removeTask(task_id)
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run()
