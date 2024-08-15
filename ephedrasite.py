from flask import Flask,render_template, request, redirect, url_for,session,flash, send_from_directory,send_file
app = Flask(__name__, template_folder='C:/Users/User/Desktop/Алишер/Ephedra/code', static_folder='C:/Users/User/Desktop/Алишер/Ephedra/static')
@app.route('/')
def main():
    return render_template('main.html')

@app.route('/prvpc')
def prvpc():
    return render_template('prv_pol.html')
if __name__ == '__main__':
    app.run(debug=True, port=8080)
