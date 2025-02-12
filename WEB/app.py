from flask import Flask, jsonify
from redis import Redis
import os

app = Flask(__name__)
redis = Redis(host=os.environ.get('REDIS_HOST', 'redis'), port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return jsonify({
        'message': 'Bonjour depuis le conteneur Docker !',
        'nombre_de_visites': redis.get('hits').decode('utf-8')
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)