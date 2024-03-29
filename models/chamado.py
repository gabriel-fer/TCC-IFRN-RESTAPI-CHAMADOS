from sql_alchemy import banco
from datetime import datetime

class ChamadoModel(banco.Model):
    __tablename__ = 'chamado'

    chamado_id = banco.Column(banco.Integer,primary_key=True)
    user = banco.Column(banco.String(100))
    cliente = banco.Column(banco.String(100))
    contato = banco.Column(banco.String(20))#Estudar a quantidade de caracteres necessários 
    relato = banco.Column(banco.String(200))#Estudar a quantidade de caracteres necessários 
    relato_final = banco.Column(banco.String(200))#Estudar a quantidade de caracteres necessários
    data = banco.Column(banco.String(20))#estudar melhor padrão de salvar data
    data_fechamento = banco.Column(banco.String(20))#estudar melhor padrão de salvar data
    status = banco.Column(banco.String(20))    



    def __init__(self,user,cliente,contato,relato,status):
        self.user = user
        self.cliente = cliente
        self.contato = contato
        self.relato = relato
        self.data = datetime.today().strftime('%Y-%m-%d %H:%M')
        self.status =  status
    def json(self):
        return{
            'chamado_id':self.chamado_id,
            'user':self.user,
            'cliente':self.cliente,
            'contato':self.contato,
            'relato':self.relato,
            'data':self.data,
            'data_fechamento':self.data_fechamento,
            'relato_final':self.relato_final,
            'status':self.status
        }
    def save_chamado(self):
        banco.session.add(self)
        banco.session.commit()
    
    @classmethod
    def encontrar_chamado(cls,chamado_id):
        chamado = cls.query.filter_by(chamado_id=chamado_id).first()
        if chamado:
            return chamado
        return None
    def update_chamado(self,user,relato_final,status):
        self.user = user
        self.relato_final = relato_final
        self.data_fechamento = datetime.today().strftime('%Y-%m-%d %H:%M')
        self.status =  status