from api import ma  # Importa a classe 'ma' do módulo 'api' (Marshmallow)
from ..models import socio_model  # Importa o módulo 'socio_model' do pacote '..models'
from marshmallow import fields  # Importa a classe 'fields' do módulo 'marshmallow'

class SocioVasco(ma.SQLAlchemyAutoSchema):  # Define a classe 'SocioVasco' que herda de 'SQLAlchemyAutoSchema'
    class Meta:  # Define a classe interna 'Meta' para fornecer informações adicionais ao Marshmallow
        model = socio_model.Socio  # Define o modelo associado ao esquema como 'Socio' do módulo 'socio_model'
        load_instance = True  # Define 'True' para carregar instâncias ao desserializar JSON
        fields = ('id', 'nome', 'idade', 'plano')  # Define quais campos devem ser incluídos no esquema de serialização

    nome = fields.String(required=True)  # Define o campo 'nome' como um campo de string obrigatório
    idade = fields.String(required=True)  # Define o campo 'idade' como um campo de string obrigatório
    plano = fields.String(required=True)  # Define o campo 'plano' como um campo de string obrigatório
