from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from user import User, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supermegasecreto' 


login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return session.query(User).get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        existing_user = session.query(User).filter_by(username=username).first()
        if existing_user:
            return 'Nome de usuário já existe', 400

        new_user = User(username=username, password=password)

        session.add(new_user)
        session.commit()

        login_user(new_user)
        return redirect(url_for('home'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = session.query(User).filter_by(username=username).first()

        if user and user.password == password: 
            login_user(user)
            return redirect(url_for('home'))
        else:
            return 'Usuário ou senha incorretos', 401

    return render_template('login.html')

@app.route('/home')
@login_required
def home():
    usuarios = session.query(User).all()  
    return render_template('home.html', name=current_user.username, usuarios=usuarios)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
