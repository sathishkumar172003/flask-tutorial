from flask import Flask, render_template

app = Flask(__name__)


JOBS = [{
    "id": 1,
    "title": "Data Analyst",
    "location": "New York, NY",
    "salary": "$70,000 - $90,000",
}, {
    "id": 2,
    "title": "Data Scientist",
    "location": "San Francisco, CA",
    "salary": "$120,000 - $150,000",
}, {
    "id": 3,
    "title": "Machine Learning Engineer",
    "location": "Seattle, WA",
    "salary": "$110,000 - $140,000",
}, {
    "id": 4,
    "title": "Software Engineer",
    "location": "Austin, TX",
    "salary": "$100,000 - $130,000",
}]


@app.route('/')
def home():
    return render_template('index.html', jobs=JOBS, company_name="TechCorp")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)