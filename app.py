from flask import Flask, jsonify
from flask_restful import Api
from blacklist import BLACKLIST
from resources.chamado import Chamado,chamados,ChamadoComId
from resources.usuario import User,UserLogin,UserRegistre,UserLogout
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'DontTellAnyone'
app.config['JWT_BLACKLIST_ENABLE'] = True


api = Api(app)
jwt = JWTManager(app)

@app.before_first_request
def cria_banco():
    banco.create_all()

@jwt.token_in_blocklist_loader
def verificar_blacklist(self,token):
    return token['jti'] in BLACKLIST

@jwt.revoked_token_loader
def token_de_acesso_invalidado(jwt_header,jwt_payload):
    return jsonify({'message':'You have been logged out'}),401


api.add_resource(chamados,'/chamados')  
api.add_resource(Chamado,'/chamado')
api.add_resource(ChamadoComId,'/chamado/<string:chamado_id>')
api.add_resource(UserRegistre,'/cadastro')
api.add_resource(UserLogin,'/login')
api.add_resource(UserLogout,'/logout')

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)