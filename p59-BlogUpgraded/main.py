from flask import Flask, render_template, request
import requests
import smtplib
app = Flask(__name__)

myemail = "aryansri009@gmail.com"
my_password = "Prioryofsion09"


response = requests.get("https://api.npoint.io/0067e63917ca7a5034d9")
posts = response.json()

@app.route('/')
def index():
    return render_template("index.html", all_posts = posts, length = len(posts))

@app.route('/index.html')
def home():
    return render_template("index.html")

@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/contact.html')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:blog_id>')
def post(blog_id):
    post = posts[blog_id]
    return render_template("post.html", post = post)

@app.route('/form-entry', methods = ['POST'])
def login():
    if request.method == 'POST':
        username = request.form['name']
        email = request.form['email']
        pn = request.form['phone']
        message = request.form['message']
        connection = smtplib.SMTP('smtp.gmail.com', port=587)
        connection.starttls()
        connection.login(user=myemail, password= my_password)
        connection.sendmail(from_addr=myemail, to_addrs='aryan.shrivastava9@gmail.com', msg=f"Subject:Form Entry\n\nName: {username}\nEmail: {email}\nPhone Number: {pn}\nMessage: {message}") 
        connection.close()
        return f"<h1>Successful</h1>"

if __name__ == "__main__":
    app.run(debug=True)