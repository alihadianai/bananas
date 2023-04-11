install Flask
install SQLAlchemy

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# دیتا مدل ها

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Company %r>' % self.name

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)

    def __repr__(self):
        return '<Customer %r>' % self.name

# روت ها

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        company = Company.query.filter_by(email=email, password=password).first()
        if company:
            return redirect(url_for('dashboard', company_id=company.id))
        else:
            return render_template('login.html', error='Invalid email or password')
    else:
        return render_template('login.html')

@app.route('/dashboard/<int:company_id>')
def dashboard(company_id):
    company = Company.query.get(company_id)
    customers = Customer.query.filter_by(company_id=company_id).all()
    return render_template('dashboard.html', company=company, customers=customers)

# بدنه وب اپلیکیشن

if __name__ == '__main__':
    app.run(debug=True)
