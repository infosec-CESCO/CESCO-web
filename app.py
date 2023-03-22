import os
import json
import tempfile
from flask import Flask, render_template, request, flash
from werkzeug.utils import secure_filename
import subprocess

app = Flask(__name__)
app.config["SECRET_KEY"] = "your-secret-key"

MYTHRIL_PATH = "/path/to/mythril"  # Update this with your Mythril path

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("file")
        code = request.form.get("code")
        mode = request.form["mode"]

        if file:
            filename = secure_filename(file.filename)
            _, file_ext = os.path.splitext(filename)

            if file_ext != ".sol":
                flash("Please upload a Solidity (.sol) file.")
                return render_template("index.html")

            temp_dir = tempfile.mkdtemp()
            file.save(os.path.join(temp_dir, filename))
            file_path = os.path.join(temp_dir, filename)

        elif code:
            temp_file = tempfile.NamedTemporaryFile(mode="w", dget_flashed_messageselete=False, suffix=".sol")
            temp_file.write(code)
            temp_file.close()
            file_path = temp_file.name

        else:
            flash("Please provide a Solidity file or enter the code.")
            return render_template("index.html")

        # mythril_cli = "/home/ppakjae/Downloads/mythril-0.23.17/myth"
        mythril_cli = "/home/infosec/Desktop/mythril-develop/myth"
        
        try:
            # 모드 변경은 여기서 하면 될듯 
            # switch 문을 통해 disassemble, analyze 가능할듯
            if mode == "analyze":
                mythril_output = subprocess.check_output(
                    [mythril_cli, "analyze", file_path],
                    stderr=subprocess.PIPE,
                ).decode("utf-8")
            elif mode == "disassemble":
                mythril_output = subprocess.check_output(
                    [mythril_cli, "disassemble", file_path],
                    stderr=subprocess.PIPE,
                ).decode("utf-8")

        except subprocess.CalledProcessError as e:
            mythril_output = e.output.decode("utf-8")

        mythril_json = None
        if mythril_output:
            try:
                mythril_json = json.loads(mythril_output)
            except json.JSONDecodeError as json_error:
                print(f"Failed to parse JSON: {json_error}")
                # flash("An error occurred while analyzing the Solidity code. Please try again.")

        return render_template("index.html", mythril_output=mythril_output, mythril_json=mythril_json)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)