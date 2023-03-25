from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(Exception)
def handle_error(error):
    return render_template('error.html', error=error), 500

# Set the secret key for your app
app.config['SECRET_KEY'] = 'your-secret-key-here' 

# Initialize the SQLAlchemy instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
db = SQLAlchemy(app)


# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ''
    
    # Check if the user is already logged in
    if 'username' in session:
        return redirect(url_for('home'))

    # Check if the form has been submitted
    if request.method == 'POST':
        # Get the username and password from the form
        username = request.form['username']
        password = request.form['password']

        # Check if the username and password are correct
        if username == 'myusername' and password == 'mypassword':
            # Store the username in the session
            session['username'] = username

            # Redirect to the home page
            return redirect(url_for('home'))

        # If the username and password are incorrect, show an error message
        error = 'Invalid credentials'

    # Render the login template
    return render_template('login.html', error=error)



# Route for the registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    # Check if the form has been submitted
    if request.method == 'POST':
        # Get the email, username, and password from the form
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        # TODO: Implement registration logic here

        # Redirect to the login page
        return redirect(url_for('login'))

    # Render the registration template
    return render_template('register.html')

# Route for the home page
@app.route("/")
def home():
    return render_template("base.html", register_link=url_for('register'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/skills")
def skills():
    return render_template("skills.html")

@app.route('/notes/<int:note_id>')
def view_note(note_id):
    note = note.query.get(note_id)
    if note:
        return render_template('note.html', note=note)
    else:
        return render_template('note.html', note=note)





@app.route('/create_note', methods=['GET', 'POST'])
def create_note():
    if request.method == 'POST':
        # Get the note title and content from the form
        title = request.form['title']
        content = request.form['content']

        # Create a new note and add it to the database
        note = note(title=title, content=content)
        db.session.add(note)
        db.session.commit()

        # Redirect to the home page
        return redirect(url_for('home'))

    # Render the create_note template
    return render_template('create_note.html')

if __name__ == "__main__":
    app.run(debug=True)

