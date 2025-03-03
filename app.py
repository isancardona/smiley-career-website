from flask import Flask, render_template, jsonify


JOBS = [
    {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'McAllen, TX',
    'salary': '$120,000'
    },
    {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'McAllen, TX',
    'salary': '$110,000'
    },
    {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Mission, TX',
    },
    {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Austin, TX',
    'salary': '$105,000'
    }
]


app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name="Smiley's")

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)
    
if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=True)