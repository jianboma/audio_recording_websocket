# audio_recording_websocket
A simple demo to show how to use websocket to record audio

* step 1. create a virtual environment
```
virtualenv venv
source venv/bin/activate
```
* step 2. install the dependencies by
```
pip install -r requrements.txt
```
* step 3. run the [<code>websocket-server.py</code>](websocket-server.py)
```
python websocket-server.py
```
* step 4. run the [<code>websocket-client.py</code>](websocket-server.py)
```
python websocket-client.py
```
* step 5. you can run other clients to test the multi-thread of server