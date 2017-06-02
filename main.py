"""Main program functions"""
from flask import Flask, render_template
import data
import content_handler

app = Flask(__name__)
content = content_handler.prepare_content("content.txt")


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', message="page")


@app.errorhandler(NameError)
@app.errorhandler(UnboundLocalError)
@app.errorhandler(500)
def page_not_found(error):
    return render_template('error.html', message="database")


@app.route("/")
@app.route("/index")
def index_route():
    if content:
        return render_template('index.html', content=content)


@app.route("/mentors")
def mentors():
    titles = ["Mentor's first name", "Mentor's last name", "Schools name", "Schools country"]
    table = data.get_results("""SELECT first_name, last_name, schools.name, schools.country
                                FROM mentors
                                    JOIN schools
                                        ON mentors.city=schools.city
                                ORDER BY mentors.id DESC;""")
    return render_template('list.html', data=table, titles=titles, content=content[0])


@app.route("/all-school")
def all_school():
    titles = ["Mentor's first name", "Mentor's last name", "Schools name", "Schools country"]
    table = data.get_results("""SELECT first_name, last_name, schools.name, schools.country
                                FROM mentors
                                    RIGHT JOIN schools
                                        ON mentors.city=schools.city
                                ORDER BY mentors.id DESC;""")
    return render_template('list.html', data=table, titles=titles, content=content[1])


@app.route("/mentors-by-country")
def mentors_by_country():
    titles = ["Country", "Number of mentors"]
    table = data.get_results("""SELECT schools.country, COUNT(mentors.first_name)
                                FROM schools
                                    JOIN mentors
                                        ON schools.city=mentors.city
                                GROUP BY schools.country ORDER BY schools.country ASC;""")
    return render_template('list.html', data=table, titles=titles, content=content[2])


@app.route("/contacts")
def contacts():
    titles = ["Scool's name", "Mentor's first name", "Mentor's last name"]
    table = data.get_results("""SELECT schools.name, mentors.first_name, mentors.last_name
                                FROM mentors
                                    RIGHT JOIN schools
                                        ON mentors.id=schools.contact_person
                                ORDER BY schools.name ASC;""")
    return render_template('list.html', data=table, titles=titles, content=content[3])


@app.route("/applicants")
def applicants():
    titles = ["Applicants first name", "Application code", "Application date"]
    table = data.get_results("""SELECT applicants.first_name, applicants.application_code, applicants_mentors.creation_date
                                FROM applicants
                                    JOIN applicants_mentors
                                        ON applicants.id=applicants_mentors.applicant_id
                                WHERE applicants_mentors.creation_date>CAST('2016-01-01' AS DATE)
                                ORDER BY applicants_mentors.creation_date DESC;""")
    return render_template('list.html', data=table, titles=titles, content=content[4])


@app.route("/applicants-and-mentors")
def applicants_and_mentors():
    titles = ["Applicants first name", "Application code", "Mentor first name", "Mentor last name"]
    table = data.get_results("""SELECT applicants.first_name, applicants.application_code,
                                       mentors.first_name, mentors.last_name
                                FROM applicants
                                    FULL JOIN applicants_mentors
                                        ON applicants.id=applicants_mentors.applicant_id
                                    LEFT JOIN mentors
                                        ON applicants_mentors.mentor_id=mentors.id
                                ORDER BY applicants_mentors.applicant_id ASC;""")
    return render_template('list.html', data=table, titles=titles, content=content[5])


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
