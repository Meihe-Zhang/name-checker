from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Name Checker</title>
  <style>
    body { font-family: system-ui, Arial, sans-serif; max-width: 640px; margin: 40px auto; }
    .card { border: 1px solid #e5e7eb; border-radius: 12px; padding: 18px; box-shadow: 0 4px 10px rgba(0,0,0,.04); }
    input[type=text]{ width:100%; padding:10px; font-size:16px; border:1px solid #cbd5e1; border-radius:8px; }
    button{ margin-top:10px; padding:10px 16px; font-size:16px; border:0; border-radius:8px; background:#4f46e5; color:#fff; cursor:pointer;}
    .result{ margin-top:14px; font-weight:600; }
  </style>
</head>
<body>
  <h1>Name Checker</h1>
  <div class="card">
    <form method="POST">
      <label>Enter Name:</label>
      <input type="text" name="name" value="{{ name or '' }}" placeholder="type a name…">
      <button type="submit">Check</button>
    </form>
    {% if result is not none %}
      <div class="result">Result: {{ result }}</div>
    {% endif %}
  </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    name = ""
    if request.method == "POST":
        name = (request.form.get("name") or "").strip()
        key = name.lower()
        if key == "wangjunqiao":
            result = "Percentage of being a GAY = 100%."
        elif key == "zhangmeihe":
            result = "Percentage of being a PRINCESS = 100%."
        elif key == "wangzhihong":
            result = "Percentage of being a CHAIRMAN = 100%."
        else:
            n = 6 * key.count("h")
            result = f"Percentage of being a GAY ={n}%"
    return render_template_string(HTML, result=result, name=name)
