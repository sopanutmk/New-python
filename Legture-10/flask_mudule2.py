from flask import Flask , render_template_string
app = Flask(__name__)
html_template = ''''''

@app.route('/')
def home():
    return render_template_string(html_template, name="Alice")

@app.route('/greet/<name>')
def greet(name):
    return render_template_string(html_template, name=name)

if __name__ == '__main__':
    app.run(dubug=True)