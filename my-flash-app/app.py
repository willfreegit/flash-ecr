from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from my flask app on ecs"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 80))