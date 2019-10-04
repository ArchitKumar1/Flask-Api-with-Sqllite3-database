from flask import Flask
app = Flask(__name__)

@app.route('/hi/<int:num>')
def hi(num):
    return 'Hello %s!' % num

@app.route('/bye')
def bye():
    return 'bye world'

if __name__ == '__main__':
    app.run()