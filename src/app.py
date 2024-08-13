import os
import json
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return json.dumps({
        'message': 'Hello EXA!',
        'hostname': os.environ.get('HOSTNAME'),
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000')
