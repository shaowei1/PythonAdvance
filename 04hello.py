from flask import Flask

app = Flask(__name__)


@app.route('/index.html')
def index():
    return 'index response 200'


@app.route('/center.html')
def center():
    return 'center response 200'


if __name__ == '__main__':
    # run server
    # Map([<Rule '/index.html' (GET, OPTIONS, HEAD) -> index>,
    #  <Rule '/static/<filename>' (GET, OPTIONS, HEAD) -> static>])
    # visit web --> url --> view function --> return response
    print(app.url_map)
    app.run(debug=True)
