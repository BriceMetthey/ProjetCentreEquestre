from flask import Flask, g, render_template, redirect, url_for, request, flash, session
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
import sqlite3


DATABASE = 'bdd/centreEquestre.db'

app = Flask(__name__)
app.config.from_object('config.Config')

# Configuration de Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'login'


# Définition de la classe User avec des propriétés
class User(UserMixin):
    def __init__(self, id, username, email, password, role):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.role = role


# Charger un utilisateur depuis la base de données
@login_manager.user_loader
def load_user(user_id):
    db = get_db()
    (userid, username, email, password, role) = db.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
    
    if userid is not None:
        return User(userid, username, email, password, role)
    return None


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db



@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


# Page de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        db = get_db()
        user = db.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password)).fetchone()
        
        if user is not None:
            (userid, username, email, password, role) = user
            login_user(User(userid, username, email, password, role))
            #flash(f'Bienvenue, {username}!', 'success')
            
            session['username'] = username
            session['role'] = role  # Stocke le rôle dans la session
            
            return redirect(url_for('home'))
        else:
            flash('Nom d\'utilisateur ou mot de passe incorrect', 'danger')
    return render_template('login.html')

# Page de logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    session.clear()
    #flash('Vous vous êtes déconnecté avec succès', 'success')
    return redirect(url_for('login'))


# Page d'accueil
@app.route('/')
@login_required
def home():
    return render_template('base.html', role=session.get('role'))



 
# Page d'administration
@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    db = get_db()

    if request.method == 'POST':
        # Création d'un nouvel utilisateur
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        role = request.form.get('role', 'user')

        # Insertion d'un nouvel utilisateur
        db.execute('INSERT INTO users (username, email, password, role) VALUES (?, ?, ?, ?)',
                     (username, email, password, role))
        db.commit()
        flash('Utilisateur créé avec succès !', 'success')
        return redirect(url_for('admin'))

    # Récupération de tous les utilisateurs
    db.row_factory = sqlite3.Row  # Cela transforme chaque ligne en dictionnaire
    users = db.execute('SELECT * FROM users').fetchall()
        
    if session.get('role') == 'admin':  # Vérifie que l'utilisateur est administrateur
        return render_template('admin.html', role=session.get('role'), users=users)
    else:
        return redirect(url_for('home'))  # Redirige si l'utilisateur n'est pas admin
 
    
# Route pour supprimer un utilisateur
@app.route('/delete_user/<int:user_id>', methods=['POST'])
@login_required
def delete_user(user_id):
    db = get_db()
    db.execute('DELETE FROM users WHERE id = ?', (user_id,))
    db.commit()
    
    flash('Utilisateur supprimé avec succès !', 'success')
    return redirect(url_for('admin'))

# Route pour modifier un utilisateur
@app.route('/edit_user/<int:user_id>', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    db = get_db()
    (userid, username, email, password, role) = db.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
    user = User(userid, username, email, password, role)
    if request.method == 'POST':
        # Mettre à jour les informations de l'utilisateur
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        role = request.form.get('role', 'user')

        db.execute('UPDATE users SET username = ?, email = ?, password = ?, role = ? WHERE id = ?',
                     (username, email, password, role, user_id))
        db.commit()
        
        flash('Utilisateur modifié avec succès !', 'success')
        return redirect(url_for('admin'))

    return render_template('edit_user.html', role=session.get('role'), user=user)




