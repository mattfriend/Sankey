from flask import Flask, render_template

# configure application.
app = Flask(__name__)

# ensure responses aren't cached.
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response


@app.route("/")
def index():
    """
    Renders index page.
    Input: None.
    Returns: render_template for sankey.html
    """
    # If wish to print the sankey diagram with data labels
    # ...comment out the line immediately below, and comment in
    # ... the bottom line

    # return render_template("sankey.html")
    return render_template("sankey_with_data_labels.html")
