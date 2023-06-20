from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/js_showcase.html')  # Modify the URL path here
def javascript_showcase():
    jls_extract_var = '''<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
	<title>Eventually by HTML5 UP</title>
	<link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}">
</head>
<body>

	<header>
		<h1>Eventually</h1>
		<p>A simple template for telling the world when you'll launch<br>your next big thing. Brought to you by <a href="http://html5up.net" rel="noopener">HTML5 UP</a>.</p>
	</header>

	<div class="sidebar">
		<a href="{{ url_for('javascript_showcase') }}">Other Page</a>
		<!-- Add more links here as needed -->
	</div>

	<section>
		<form id="signup-form" method="post" action="#">
			<input type="email" name="email" id="email" placeholder="Email Address">
			<input type="submit" value="Sign Up">
		</form>
	</section>

	<footer>
		<ul class="icons">
			<li><a href="#" class="icon brands fa-twitter" rel="noopener"><span class="label">Twitter</span></a></li>
			<li><a href="#" class="icon brands fa-instagram" rel="noopener"><span class="label">Instagram</span></a></li>
			<a href="https://github.com/djones0405" target="_blank">GitHub Profile</a>
			<li><a href="#" class="icon fa-envelope" rel="noopener"><span class="label">Email</span></a></li>
		</ul>
		<ul class="copyright">
			<li>&copy; Untitled.</li>
			<li>Credits: <a href="http://html5up.net" rel="noopener">HTML5 UP</a></li>
		</ul>
	</footer>

	<script src="{{ url_for('static', filename='js/main.js') }}"></script>

</body>
</html>
'''
    return jls_extract_var


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
