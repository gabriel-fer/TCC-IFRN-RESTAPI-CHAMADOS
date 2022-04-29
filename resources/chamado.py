from flask_restful import Resource,reqparse
from models.chamado import ChamadoModel
from flask_jwt_extended import jwt_required

argumentos = reqparse.RequestParser()
argumentos.add_argument('user')
argumentos.add_argument('cliente')
argumentos.add_argument('contato')
argumentos.add_argument('relato')
argumentos.add_argument('relato_final')
argumentos.add_argument('data')
argumentos.add_argument('data_fechamento')
argumentos.add_argument('status')
    

class chamados(Resource):
    def get(self):
        return{'chamados':[chamado.json() for chamado in ChamadoModel.query.all()]}


class Chamado(Resource):

    @jwt_required()
    def post(self):
        dados = argumentos.parse_args()
        chamado = ChamadoModel(**dados)
        chamado.save_chamado()
        return chamado.json(),201

class ModificarChamado(Resource):
    
    @jwt_required()
    def put(self,chamado_id):
        dados = argumentos.parse_args()
        chamado_encontrado = ChamadoModel.encontrar_chamado(chamado_id)
        if chamado_encontrado:
            chamado_encontrado.update_chamado(**dados)
            chamado_encontrado.save_chamado()
            return chamado_encontrado.json(),200
        return {'message':'Hotel not found.'},404
    
    def get(self,chamado_id):
        chamado = ChamadoModel.encontrar_chamado(chamado_id)
        if chamado:
            return chamado.json()
        return {'message':'chamado not found.'},404 #not found



