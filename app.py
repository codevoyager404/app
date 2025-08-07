from flask import Flask, request, jsonify
from flask_cors import CORS
from supabase_client import supabase

app = Flask(__name__)
CORS(app)  # 🔐 Επιτρέπει αιτήματα από το iOS app

@app.route("/api/posts", methods=["GET", "POST"])
def handle_posts():
    if request.method == "GET":
        res = supabase.table("posts").select("*").order("created_at", desc=True).execute()
        return jsonify(res.data)

    if request.method == "POST":
        data = request.get_json()
        content = data.get("content")

        if not content or len(content) < 3:
            return jsonify({"error": "Too short"}), 400

        # ❗ Προσωρινά χωρίς user_id για να αποφύγουμε uuid error
        res = supabase.table("posts").insert({
            "content": content
        }).execute()

        return jsonify({"message": "created", "data": res.data}), 201
