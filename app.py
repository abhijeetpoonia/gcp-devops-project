from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>We are proud Jaat!</h1>"

if __name__ == '__main__':
    # Run the app on 0.0.0.0 to make it accessible from outside the container
    app.run(host='0.0.0.0', port=5000)

