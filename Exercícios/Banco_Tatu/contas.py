# coding: utf-8
class Conta:
	def __init__(self, clientes, numero, saldo=0):
		self.saldo = 0
		self.clientes = clientes
		self.clientes.nome = nome
		self.clientes.telefone = telefone
		self.numero = numero
		self.operacoes = []
		self.deposito(saldo)

	def resumo(self):
		print("Conta Corrente Numero: %s | Saldo: %10.2f | Nome: %s | Telefone: %s" %
			(self.numero, self.saldo, self.nome, self.telefone ))

	def saque(self, valor):
		try:
			self.saldo <= valor:
			print("Saldo Insuficiente")
		except:				
			if self.saldo >= valor:
				self.saldo -= valor
				self.operacoes.append(["SAQUE", valor])

	def deposito(self, valor):
		self.saldo += valor
		self.operacoes.append(["DEPOSITO", valor])

	def extrato(self):
		print("Extrato Conta corrente Numero: %s\n" % self.numero)
		for operacao in self.operacoes:
			print("%10s %10.2f" % (o[0], o[1]))
		print("\n     Saldo: %10.2f\n" % self.saldo)