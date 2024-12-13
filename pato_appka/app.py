"""Main file of our basic app."""

import random
from flask import Flask, render_template, jsonify


app = Flask(__name__)

# Simple list of edgy quotes
quotes = [
    "Life is hard, but it's harder when you're stupid.",
    "You only live once, but if you do it right, once is enough.",
    "Everything is temporary, including your problems.",
    "Success is not the key to happiness. Happiness is the key to success.",
    "If you want to go fast, go alone. If you want to go far, go together.",
]


@app.route("/")
def home():
    """
    Function to handle the home route.

    This function is responsible for handling requests to the root URL ("/") 
    of the application. When a user navigates to this URL, this function 
    will be called, and it will render the "index.html" template.

    Returns:
        A rendered HTML template for the home page.    """
    return render_template("index.html")


@app.route("/quote")
def quote():
    """
    Function to handle the quote route.
    
    This function is responsible for handling requests to the "/quote" URL
    of the application. When a user navigates to this URL, this function
    will be called, and it will return a random quote as a JSON response.

    Returns:
        A JSON object containing a random quote.
    """
    return jsonify({"quote": random.choice(quotes)})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
