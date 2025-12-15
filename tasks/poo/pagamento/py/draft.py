from abc import ABC, abstractmethod;

class Pagamento(ABC):
    def __init__(self, valor: float, descriçao: str):
        self.valor = valor;
        self.descriçao = descriçao;

    def resumo(self):
        print(f"Pagamento de R$ {self.valor}: {self.descriçao}");

    def validar_valor(self):
        if self.valor <= 0:
            raise ValueError("O valor deve ser maior do que 0");

    @abstractmethod
    def processar(self):
        pass;

class Cartão_de_Crédito(Pagamento):
    def __init__(self, numero: int, nome_titular: str, limite_disponivel: float):
        self.numero = numero;
        self.nome_titular = nome_titular;
        self.limite_disponivel = limite_disponivel;

    def processar(self):
        if self.valor > self.limite_disponivel:
            print("Transação recusada: Limite insuficiente");
        else:
            self.limite_disponivel = self.limite_disponivel - self.valor;
            print("Pagamento confirmado.");

class Pix(Pagamento):
    def __init__(self, chave, descriçao):
        

class Boleto(Pagamento):