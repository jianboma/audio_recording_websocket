"""
 A super simple demo of flask
"""



from flask import Flask, render_template
from websocket_server import Websocket_Server
app = Flask(__name__)

websocketServer = Websocket_Server()

@app.route("/")
def index():
    print('index rendering')
    return render_template('recording_test.html') #"Hello World!"

@app.route("/websocket")
def websocket():
    # start the websocket server
    print('start websocket server ...')
    websocketServer.start()

if __name__ == "__main__":
    # print('start websocket server ...')
    # websocketServer.start()
    app.run(debug=True)