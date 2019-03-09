from flask import Flask, jsonify
from sqlalchemy import create_engine

from .db import db_engine

application = Flask(__name__)
engine = db_engine()


@application.route("/healthz")
def health():
    return jsonify({"data": "OK"})


@application.route("/connection-test")
def connection_test():
    with engine.begin() as conn:
        version = list(conn.execute("SELECT version()").fetchone())[0]
        return jsonify({"version": version})
