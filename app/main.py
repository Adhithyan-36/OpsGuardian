
from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Count the requests received by our application
REQUEST_COUNT = Counter(
    "opsguardian_requests_total",
    "Total number of requests received"
)


@app.before_request
def count_requests():
    from flask import request

    if request.path != "/metrics":
        REQUEST_COUNT.inc()


@app.route("/")
def home():
    return "OpsGuardian Demo Application"


@app.route("/health")
def health():
    return {
        "status": "healthy"
    }


@app.route("/metrics")
def metrics():
    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)