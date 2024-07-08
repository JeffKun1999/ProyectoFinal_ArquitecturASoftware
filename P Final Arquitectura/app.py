from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

reservations = []

@app.route('/')
def index():
    return render_template('index.html', reservations=reservations)

@app.route('/reserve', methods=['POST'])
def reserve():
    name = request.form.get('name')
    date = request.form.get('date')
    time = request.form.get('time')
    
    if name and date and time:
        reservations.append({'name': name, 'date': date, 'time': time})
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
