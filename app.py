from flask import Flask, render_template, url_for, request
import sqlite3
from datetime import date

app = Flask(__name__)
conn = sqlite3.connect("database.db")

@app.route('/', methods=["GET"])
def home():
   with sqlite3.connect("database.db") as con:
      cun = con.cursor()
      cun.execute("SELECT * FROM news;")
      allnews = cun.fetchall()
   return render_template('home.html', allnews=allnews)

@app.route('/news', methods=["GET", "POST"])
def news():
   # open database
   with sqlite3.connect("database.db") as con:
      cun = con.cursor()

   if request.method == "POST":
      search = request.form.get("search")
      cun.execute("SELECT * FROM news WHERE title LIKE ? OR tag LIKE ? OR content LIKE ?", ('%'+search+'%','%'+search+'%','%'+search+'%'))
      allnews= cun.fetchall()
      con.close()
      return render_template('news.html', allnews=allnews)

   else:
      cun.execute("SELECT * FROM news;")
      allnews = cun.fetchall()
      con.close()
      return render_template('news.html', allnews=allnews)

@app.route('/write', methods=["GET", "POST"])
def write():
   tags = [
      "Tech",
      "Movies",
      "Games",
      "Reviews"
   ]
      
   if request.method == "GET":   
      return render_template('write-news.html', tags=tags)
   else:
      title = request.form.get("title")
      subtitle = request.form.get("subtitle")
      content = request.form.get("content")
      tag = request.form.get("tags")
      today = date.today()
      today = today.strftime("%m/%d/%y")

      forms =[title,subtitle,content, tag] 
      with sqlite3.connect("database.db") as con:
         cun = con.cursor()
         forms = cun.execute("SELECT * FROM news").fetchall()
         cun.execute("INSERT INTO news VALUES(?,?,?,?,?)", (title, subtitle, content, tag, today))
         con.commit()
         cun.close()

      return render_template('write-news.html', tags=tags)
      
@app.route('/contact', methods=["GET"])
def contact():
   return render_template('contact.html')

@app.route('/page/<index>')
def page(index):
   with sqlite3.connect("database.db") as con:
      cun = con.cursor()
      cun.execute("SELECT * FROM news;")
      allnews = cun.fetchall()
      
   index = int(index)
   return render_template("page.html", index=index, allnews=allnews)
if __name__ == '__main__':
   app.run(debug = True)

# export FLASK_ENV=development