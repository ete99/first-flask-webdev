from flask import Flask, render_template, request
app = Flask(__name__)

students = []

@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/register", methods=['POST'])
def register():
    name = request.form.get("name")
    if not name:
        return render_template("Fail.html", name=name)
    students.append(name)
    return render_template("Success.html", students=students)


if __name__ == '__main__':

    app.debug = True
    app.run()
    '''host='192.168.0.13', port=8000'''