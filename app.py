from flask import Flask, render_template


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///demo.db'
app.secret_key = 'your_secret_key'

# Route for the main page (Home)
@app.route("/")
def home():
    return render_template("main.html")

# Route for Blog
@app.route("/blog")
def blog():
    return render_template("blog.html")

# Route for Contact
@app.route("/contact")
def contact():
    return render_template("contact.html")

# Route for About
@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
