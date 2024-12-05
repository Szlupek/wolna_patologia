from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Simple list of edgy quotes
quotes = [
    "Life is hard, but it's harder when you're stupid.",
    "You only live once, but if you do it right, once is enough.",
    "Everything is temporary, including your problems.",
    "Success is not the key to happiness. Happiness is the key to success.",
    "If you want to go fast, go alone. If you want to go far, go together."
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quote')
def quote():
    return jsonify({'quote': random.choice(quotes)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
