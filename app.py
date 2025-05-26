from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SECRET_KEY'] = 'the_key'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/login', methods=['GET', 'POST']) 
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('ana'))
        flash('E-posta veya şifre hatalı!', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST']) 
def register():
    if request.method == 'POST': 
        email = request.form.get('email') 
        password = request.form.get('password') 

        if User.query.filter_by(email=email).first():
            flash('Bu e-posta zaten kayıtlı!', 'danger') 
            return redirect(url_for('login'))

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        name = request.form.get('name') 
        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Kayıt başarılı! Giriş yapabilirsiniz.', 'success') 
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login.html'))

@app.route('/ana')
@login_required
def ana():
    return render_template('ana.html')

@app.route('/hos')
@login_required
def hos():
    return render_template('hos.html')

@app.route('/hos1')
@login_required
def ho1():
    return render_template('hos1.html')

@app.route('/hos2')
@login_required
def ho2():
    return render_template('hos2.html')

@app.route('/hos3')
@login_required
def ho3():
    return render_template('hos3.html')

@app.route('/hos4')
@login_required
def ho4():
    return render_template('hos4.html')

@app.route('/hos5')
@login_required
def ho5():
    return render_template('hos5.html')



@app.route('/duyurlar')
def duyurlar():
    return render_template('duyurlar.html')

@app.route('/Dashbord')
def Dashboard():
    return render_template('Dashbord.html')

@app.route('/Dashbord')
@login_required
def dashboard():
    user = user.query.filter_by(user_id=current_user.id).order_by(user.id.desc()).all()
    return render_template('Dashbord.html', user=user)

@app.route('/Akademik')
def Akademik():
    return render_template('Akademik.html')

@app.route('/Uyumluluk')
def Uyumluluk():
    return render_template('Uyumluluk.html')

@app.route('/Yenileme')
def Yenileme():
    return render_template('Yenileme.html')

if __name__== '__main__':
    app.run(debug=True)