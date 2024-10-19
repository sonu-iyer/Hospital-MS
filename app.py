from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy data for demo purposes
users = {"admin": "password"}
patients = []
appointments = []
reports = []
equipment = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users[username] = password
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return redirect(url_for('home'))
        else:
            return "Invalid credentials"
    return render_template('login.html')

@app.route('/patients')
def view_patients():
    return render_template('patients.html', patients=patients)

@app.route('/add_patient', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        patient = {
            'name': request.form['name'],
            'age': request.form['age'],
            'condition': request.form['condition']
        }
        patients.append(patient)
        return redirect(url_for('view_patients'))
    return render_template('add_patient.html')

@app.route('/appointments')
def view_appointments():
    return render_template('appointments.html', appointments=appointments)

@app.route('/add_appointment', methods=['GET', 'POST'])
def add_appointment():
    if request.method == 'POST':
        appointment = {
            'patient': request.form['patient'],
            'date': request.form['date'],
            'time': request.form['time']
        }
        appointments.append(appointment)
        return redirect(url_for('view_appointments'))
    return render_template('add_appointment.html')

@app.route('/reports')
def view_reports():
    return render_template('reports.html', reports=reports)

@app.route('/add_report', methods=['GET', 'POST'])
def add_report():
    if request.method == 'POST':
        report = {
            'patient': request.form['patient'],
            'date': request.form['date'],
            'details': request.form['details']
        }
        reports.append(report)
        return redirect(url_for('view_reports'))
    return render_template('add_report.html')

@app.route('/equipment')
def view_equipment():
    return render_template('equipment.html', equipment=equipment)

@app.route('/add_equipment', methods=['GET', 'POST'])
def add_equipment():
    if request.method == 'POST':
        item = {
            'name': request.form['name'],
            'quantity': request.form['quantity'],
            'status': request.form['status']
        }
        equipment.append(item)
        return redirect(url_for('view_equipment'))
    return render_template('add_equipment.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
