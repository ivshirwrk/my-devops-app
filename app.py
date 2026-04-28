from flask import Flask, request
import redis
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Статическая метрика о количестве запросов
metrics.info('app_info', 'Application info', version='1.0.0')

r = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def hello():
    count = r.incr('visits')
    return f'Привет, DevOps! Эту страницу посетили {count} раз(а).'

# Эндпоинт /metrics создаётся автоматически

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
