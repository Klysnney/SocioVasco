from..models import socio_model
from api import db

def cadastrar_torcedor(torcedor):
    torcedor_vasco = socio_model.Socio(nome=torcedor.nome, idade=torcedor.idade, plano=torcedor.plano)
    db.session.add(torcedor_vasco)
    db.session.commit()
    return torcedor_vasco

def listar_torcedor():
    socios_torcedores = socio_model.Socio.query.all()
    return socios_torcedores

def listar_torcedor_id(id):
    socio_torcedor = socio_model.Socio.query.filter_by(id=id).first()
    return socio_torcedor

def atualizar_socio(socio_antigo, socio_novo):
    socio_antigo.nome = socio_novo.nome
    socio_antigo.idade = socio_novo.idade
    socio_antigo.plano = socio_novo.plano
    db.session.commit()

def deletar_torcedor(id):
    db.session.delete(id)
    db.session.commit()