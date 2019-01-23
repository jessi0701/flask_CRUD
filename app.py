from flask import Flask, render_template, request, redirect
from flask_migrate import Migrate
from models import *
import datetime
app = Flask(__name__)
#sqlalchemy 설정
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///flask_db.sqlite3" 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


#sqlalchemy 초기화
#db = SQLAlchemy(app)
db.init_app(app)

migrate = Migrate(app,db)

@app.route("/")
def hello():
    todos = Todo.query.all()
    return render_template("index.html",todos=todos)
    
@app.route("/new")
def new():
    return render_template("new.html")
    
@app.route("/create")
def create():
    #request는 요청하는 기능 <form action="/create"> 와 @app.route("/create") 이 연결됨
    t = request.args.get("title")
    c = request.args.get("content")
    created_at = datetime.datetime.now()
    
    new_todo = Todo(title=t, content=c,created_at=created_at)
    db.session.add(new_todo)
    db.session.commit()
    
    return redirect("/")
    
@app.route("/<int:id>")
def read(id):
    todo = Todo.query.get(id)
    return render_template("read.html",todo=todo)
    
@app.route("/<int:id>/delete") 
def delete(id):
    todo = Todo.query.get(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

@app.route("/<int:id>/edit")
def edit(id):
    todo = Todo.query.get(id)
    return render_template("edit.html",todo=todo)
    
@app.route("/<int:id>/update")
def update(id):
    todo = Todo.query.get(id)
    title = request.args.get("title")
    content = request.args.get("content")
    
    todo.title = title
    todo.content = content
    db.session.commit()
    
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)