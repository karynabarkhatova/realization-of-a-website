from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    output = render_template("index.html")
    return output


@app.route('/about/', methods=['GET', 'POST'])
def about():
    file = open('static/biography.txt')
    string = "i don't ask why patients lie, i just assume they all do."
    output = render_template("about.html", biography=file.read(), quote=string)
    return output


@app.route('/contact/', methods=['GET', 'POST'])
def contact():

    if request.method == 'POST':
        name = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        topic = request.form['topic']
        message = request.form['message']
        response = request.form['response']

        with open('data.txt', 'w') as data_file:
            data_file.write(
                f'Name: {name}\n'
                f'Last Name: {lastname}\n'
                f'Email: {email}\n'
                f'Topic: {topic}\n'
                f'Message: {message}\n'
                f'Response: {response}\n')
        return redirect('/contact/')

    output = render_template("contact.html")
    return output


@app.errorhandler(404)
def error_404(e):
    output = render_template('404err.html')
    return (output, 404)


@app.errorhandler(500)
def error_500(e):
    output = render_template('500err.html')
    return (output, 500)


if __name__ == '__main__':
    app.run()
