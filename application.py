from flask import Flask
app = Flask(__name__)

@app.route('/')
def root():
    #return app.send_static_file('hostingstart.html')
    return 'Hello world'

if __name__ == '__main__':
    app.run(debug=True)
