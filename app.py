from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample

app = Flask(__name__)
app.config['SECRET_KEY'] = "chickeneater123"
debug = DebugToolbarExtension(app)

# Decorator


@app.route('/')
def home_page():

    return render_template('home.html')

# Greeting Dynamic


@app.route('/greet')
def greetings():
    return render_template('form.html')


complements = ["cool", "clever", "tenacious", "awesome", "Pythonic"]


@app.route('/showgreet')
def showGreet():
    username = request.args['username']
    niceThings = choice(complements)
    return render_template('greet.html', username=username, compliments=niceThings)

# V2 Greet


@app.route('/form-2')
def show_form2():
    return render_template('form_2.html')


@app.route('/greet-2')
def get_greeting_2():
    username = request.args['username']
    wants_compliments = request.args.get('wants_compliments')
    niceThings = sample(complements, 3)
    return render_template('greet_2.html', username=username, wants_compliments=wants_compliments, niceThings=niceThings)

# Dynamic template


@app.route('/lucky')
def luckyNumber():
    number = randint(1, 10)
    return render_template('lucky.html', lucky_num=number)


@app.route('/spell/<word>')
def spelling(word):
    capsWord = word.upper()
    return render_template('spell.html', word=capsWord)


@app.route('/hello')
def say_hello():

    return render_template('hello.html')


@app.route('/search')
def search_path():
    term = request.args["term"]
    sort = request.args["sort"]
    return f"<h1>Search Result For: {term}</h1><p>Sorting by {sort}"


# @app.route('/post', methods=['POST', "GET"])
# def postDemo():
#     return "You made a post request"


# Name important to send the value
@app.route('/add-comment')
def addCommentForm():
    return """
    <h1>Add Comment</h1>
    <form method="POST">
        <input type='text' placeholder='comment' name='comment'/>
        <input type='text' placeholder='username' name='username'/>  
        <button>Submit</button>
    </form>
"""

# POST ROUTE


@app.route('/add-comment', methods=["POST"])
def saveComment():
    comment = request.form["comment"]
    username = request.form["username"]

    return f"""
            <p>Save your comment with text of {comment} with Username: {username}</p>"""

# Routing portion


@app.route('/r/<subreddit>')
def showSubreddit(subreddit):
    return f"""<h1>Browsing {subreddit} subreddit</h1>"""


@app.route('/r/<subreddit>/comments/<int:postId>')
def showComments(subreddit, postId):
    return f"<h1>Veiwing comments for post with id: {postId} from the {subreddit} Subreddit</h1>"


# Hard coded database
post = {
    1: "I like beef curry",
    2: "I hate fish",
    3: "Double petty burgers are on the way",
    4: "YOKOSIMA (LOL)"
}


@app.route('/posts/<int:id>')
def getPost(id):
    posts = post.get(id, "Posst not found")
    return f"<h1>{posts}</h1>"


# Condition
if __name__ == "__main__":
    app.run(debug=False)
