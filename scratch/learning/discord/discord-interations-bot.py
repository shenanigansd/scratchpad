from flask import Flask, abort, jsonify, request
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
import json

PUBLIC_KEY = ""
app = Flask(__name__)


@app.post("/")
def handle_request():
    verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))

    signature = request.headers["X-Signature-Ed25519"]
    timestamp = request.headers["X-Signature-Timestamp"]
    body = request.data.decode("utf-8")

    try:
        verify_key.verify(f"{timestamp}{body}".encode(), bytes.fromhex(signature))
    except BadSignatureError:
        abort(401, "invalid request signature")

    print(json.dumps(request.headers["X-Signature-Ed25519"]))
    print(json.dumps(request.headers["X-Signature-Timestamp"]))
    print(str(request.data))

    if request.json["type"] == 1:
        return jsonify({
            "type": 1
        })

    else:
        return jsonify({
            "type": 4,
            "data": {
                "tts": False,
                "content": "Congrats on sending your command!",
                "embeds": [],
                "allowed_mentions": {"parse": []}
            }
        })


if __name__ == "__main__":
    app.run(host="0.0.0.0")
