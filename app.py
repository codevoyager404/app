from flask import Flask, render_template, request, redirect
from supabase_client import supabase

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    res = supabase.table("posts").select("*").order("created_at", desc=True).execute()
    posts = res.data if res.data else []
    return render_template("index.html", posts=posts)

@app.route("/submit", methods=["POST"])
def submit():
    content = request.form.get("content")
    if content:
        supabase.table("posts").insert({"content": content}).execute()
    return redirect("/")