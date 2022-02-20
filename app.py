from flask import Flask, render_template

app = Flask(__name__,
            static_url_path='',
            static_folder='web/static',
            template_folder='web/templates')

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/how-website-was-built')
def about():
    return render_template('how-website-was-built.html')

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80)
