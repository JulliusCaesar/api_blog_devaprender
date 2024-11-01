from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Criar um API flask
app = Flask(__name__)
# Criar uma instância de SQLAlchemy
app.config['SECRET_KEY'] ="IMPEJC@JULIUS"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres.hrmttrchzmzentzhuntq:dk5NV*4fJCvsXs*@aws-0-sa-east-1.pooler.supabase.com:6543/postgres' # sqlite:///blog.db é o caminho sql sem precisar especificar pastas mais profundas

db = SQLAlchemy(app)
db:SQLAlchemy

# Definir a estrutura da tabela Postaegm
# id_postagem, titulo, autor
class Postagem(db.Model):
    __tablename__ = 'postagem'
    id_postagem = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String)
    # autor
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'))
    
# Definir a estrutura da tabela Autor
# id_autor, nome, email, senha, admin, postagens
class Autor(db.Model):
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    postagens = db.relationship('Postagem')

# Executar o comando para criar o banco de dados
def inicializar_banco():
    with app.app_context():
        db.drop_all()
        db.create_all()
        # Criar usuários adminitradores
        autor = Autor(nome='julio', email='impejc@proton.me', senha='193752', admin=True)
        db.session.add(autor)
        db.session.commit()
    
if __name__ == '__main__':
    inicializar_banco()