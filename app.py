from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "update, Azure Container Apps!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


