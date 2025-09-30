from flask import Flask, request, jsonify
import fasttext

app = Flask(__name__)

# Load the pre-trained language ID model
model = fasttext.load_model("lid.176.bin")

@app.route("/", methods=["GET"])
def index():
    return jsonify({"status": "ok", "message": "FastText Language Detection API", "endpoint": "/detect"})

@app.route("/detect", methods=["POST"])
def detect_language():
    data = request.json
    text = data.get("text", "").strip()

    if not text:
        return jsonify({"error": "No text provided"}), 400

    predictions = model.predict(text, k=1)  # top-1 prediction
    lang = predictions[0][0].replace("__label__", "")
    confidence = float(predictions[1][0])

    return jsonify({"language": lang, "confidence": confidence})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
