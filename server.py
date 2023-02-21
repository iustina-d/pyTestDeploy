from flask import Flask,render_template
import os


@app.route("/")
def main():
  return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')