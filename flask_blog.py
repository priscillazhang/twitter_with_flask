from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        "author": "Priscilla Zhang",
        "title": "First Blog Post",
        "content": " First post content, hello world",
        "date_posted": "April 28th, 2024"
    },
    {
        "author": "John Doe",
        "title": "Second Blog Post",
        "content": " Here is the second post on this platform",
        "date_posted": "April 28th, 2024"
    }
]


@app.route("/")
def hello():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == "__main__":
    app.run(debug=True)
