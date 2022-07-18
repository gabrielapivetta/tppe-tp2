import pytest 
from acesso import Acesso
from estacionamento import Estacionamento

@pytest.mark.parametrize("acesso, estacionamento, saida",[
    (Acesso(placa='AM31J', horaEntrada='03:40', horaSaida='11:30', isEvento=1), Estacionamento(valor_evento=40), 40),
    (Acesso(placa='SFD45', horaEntrada='05:50', horaSaida='13:10', isEvento=1), Estacionamento(valor_evento=60), 60),
])
class TesteFuncionalValorEvento():

    def testeValorEvento(self, acesso, estacionamento, saida):
        assert acesso.calculaAcesso(estacionamento) == saida