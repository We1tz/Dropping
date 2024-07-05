from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
import requests
from key import app_secret_key
import os
from key import url

app = Flask(__name__)
app.secret_key = app_secret_key




@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        pw = request.form['password']

        current_url = f"{url}/login"
        data = {
            "username": f"{username}",
            "password": f"{pw}"
        }

        response = requests.post(current_url, json=data)
        result = int(response.json()['result'])

        if result == 200:
            return render_template('main.html')
        else:
            flash('Неверный логин или пароль')
            return render_template('index.html')
    return render_template('index.html')


@app.route('/reg', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        current_url = f'{url}/register'

        data = {
            f"username": f"{username}",
            "password": f"{password}"
        }

        if password == confirm_password:
            response = requests.post(current_url, json=data)
            result = int(response.json()['result']) #
            if result == 200:
                flash('Регистрация прошла успешно')
                return redirect(url_for('success_reg'))
            else:
                flash('Повторите попытку')
                return redirect(url_for('register'))
        else:
            return "Пароль не подходит"

    return render_template('reg.html')


@app.route('/success', methods=['POST', 'GET'])
def success_reg():
    return render_template('main.html')


@app.route('/', methods=['POST', 'GET'])
def main():
    frontend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../website_frontend'))
    return send_from_directory(frontend_path, 'index.html')


if __name__ == '__main__':
    app.run(debug=True)
