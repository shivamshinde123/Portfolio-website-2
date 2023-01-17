from flask import Flask,render_template

app = Flask(__name__,template_folder='templates',static_folder='static')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/blogs')
def blogs():
    return render_template('blogs.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/sayhi')
def sayhi():
    return render_template('sayhi.html')

if __name__ == '__main__':
    app.run()