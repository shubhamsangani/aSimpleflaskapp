from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<center><h1>FLASK APP DEPLOY ON MICROSOFT AZURE</h2></center>"

if __name__ == "__main__":
    app.run()