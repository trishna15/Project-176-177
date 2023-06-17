from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

templates = [
    {
        "inputs": 9,
        "category": " Outdoor Sports",
        "word": "Badminton"
    },
    {
        "inputs": 4,
        "category": "A birthday sweet dish",
        "word": "Cake"
    },

]

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/get-template")
def get_template():
  return jsonify({
        "status": "success",
        "word": random.choice(templates)
  })

if __name__ == '__main__':
  app.run()