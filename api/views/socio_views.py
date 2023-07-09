from api import api
from flask_restful import Resource
from flask import request, make_response, jsonify
from..schemas import socio_schema
from..entidades import socio
from..services import socio_service

class SocioVasco(Resource):
    def get(self):
        socios_torcedores = socio_service.listar_torcedor()
        socio_listado = socio_schema.SocioVasco(many=True)
        return make_response(socio_listado.jsonify(socios_torcedores), 200)

    def post(self):
        socio_torcedor = socio_schema.SocioVasco()
        validate = socio_torcedor.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            idade = request.json['idade']
            plano = request.json['plano']

            novo_socio = socio.Socio(nome=nome, idade=idade, plano=plano)
            resultado = socio_service.cadastrar_torcedor(novo_socio)
            x = socio_torcedor.jsonify(resultado)
            return make_response(x, 201)
class SocioDetalhes(Resource):
    def get(self, id):
        socio = socio_service.listar_torcedor_id(id)
        if socio is None:
            return make_response(jsonify("Sócio não encontrado"), 404)
        socio_vasco = socio_schema.SocioVasco()
        return make_response(socio_vasco.jsonify(socio), 200)
    def put(self, id):
        socio_torcedor = socio_service.listar_torcedor_id(id)
        if socio_torcedor is None:
            return make_response(jsonify("Curso não encontrado"), 404)
        sc = socio_schema.SocioVasco()
        validate = sc.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            idade = request.json['idade']
            plano = request.json['plano']
            novo_socio = socio.Socio(nome=nome, idade=idade, plano=plano)

            socio_service.atualizar_socio(socio_torcedor, novo_socio)
            socio_atualizado = socio_service.listar_torcedor_id(id)
            return make_response(sc.jsonify(socio_atualizado), 200)
    def delete(self, id):
        socio_torcedor = socio_service.listar_torcedor_id(id)
        if socio_torcedor is None:
            return make_response(jsonify("Curso não encontrado"), 404)
        socio_service.deletar_torcedor(socio_torcedor)
        return make_response("Curso excluído com sucesso", 204)


api.add_resource(SocioVasco, '/sociovasco')
api.add_resource(SocioDetalhes, '/sociovasco/<int:id>')
