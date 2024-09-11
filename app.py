from flask import Flask

app = Flask(__name__)
counter = 0

@app.route('/')
def increment_counter():
    global counter
    counter += 1
    return f'Counter: {counter}'

if __name__ == '__main__':
    app.run(debug=True)
