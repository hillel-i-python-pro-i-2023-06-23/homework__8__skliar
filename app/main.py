from app.services import read_file
from app.services import generate_users
from app.services import who_is_here
from app.services import midle
from pathlib import Path
from flask import Flask, render_template


current_dir = Path(__file__).parent
app = Flask(__name__, template_folder=current_dir / "../templates")


@app.route("/")
def main():
    page_content = "main page"
    return render_template("index.html", output=page_content)


@app.route("/get-content/")
def read():
    link_1 = current_dir / "../files_input/data_input.txt"
    file_content = read_file.get_file_content(link_1)
    return render_template("index.html", output=file_content)


@app.route("/generate-users/")
def generate():
    users = generate_users.generate(num_users=10)
    return render_template("index.html", output=users)


@app.route("/space/")
def astronaft():
    link_3 = "http://api.open-notify.org/astros.json"
    who_is_here_result = f"Количество космонавтов: {who_is_here.parsing(link_3)}"
    return render_template("index.html", output=str(who_is_here_result))


@app.route("/mean/")
def parameters():
    link_4 = current_dir / "../files_input/people_data(extended).csv"
    result = midle.parameter_averaging(link_4)
    return render_template("index.html", output=result)


if __name__ == "__main__":
    app.run()
