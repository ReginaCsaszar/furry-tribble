"""Main program functions"""
from flask import Flask, render_template
import data
import content_handler

app = Flask(__name__)
content = content_handler.prepare_content("content.txt")


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', message="page")


@app.route("/")
@app.route("/index")
def index_route():
    if content:
        return render_template('index.html', content=content)


@app.route("/mentors")
def mentors():
    titles = ["Mentor's first name", "Mentor's last name", "Schools name", "Schools country"]
    table = data.get_results("SELECT * FROM mentors")
    return render_template('list.html', data=table, titles=titles, content=content[0])


@app.route("/all-school")
def all_school():
    titles = ["Mentor's first name", "Mentor's last name", "Schools name", "Schools country"]
    table = data.get_results("SELECT * FROM mentors")
    return render_template('list.html', data=table, titles=titles, content=content[1])


@app.route("/mentors-by-country")
def mentors_by_country():
    titles = ["Country", "Number of mentors"]
    table = data.get_results("SELECT * FROM mentors")
    return render_template('list.html', data=table, titles=titles, content=content[2])


@app.route("/contacts")
def contacts():
    titles = ["Scool's name", "Mentor's first name", "Mentor's last name"]
    table = data.get_results("SELECT * FROM mentors")
    return render_template('list.html', data=table, titles=titles, content=content[3])


@app.route("/applicants")
def applicants():
    titles = ["Applicants first name", "Application code", "Application date"]
    table = data.get_results("SELECT * FROM mentors")
    return render_template('list.html', data=table, titles=titles, content=content[4])


@app.route("/applicants-and-mentors")
def applicants_and_mentors():
    titles = ["Applicants first name", "Application code", "Mentor first name", "Mentor last name"]
    table = data.get_results("SELECT * FROM mentors")
    return render_template('list.html', data=table, titles=titles, content=content[5])


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
