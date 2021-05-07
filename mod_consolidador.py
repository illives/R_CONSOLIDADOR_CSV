from os import system, remove
import pandas as pd 
import glob



class arquivo:
	
	def __init__(self, arquivo, text):
		self.arquivo = arquivo
		self.text = text

	def write_txt(text, arquivo):
		"""
		Grava texto em um arquivo txt
		(text = Texto a ser guardado,
		arquivo = diretorio completo do arquivo)
		"""
		arquivo = open(arquivo, 'a')
		arquivo.write(str(text))
		arquivo.close()

	def read_txt(arquivo):
		"""
		Faz a leitura da ultima linha do arquivo txt
		(arquivo = Diretorio do arquivo a ser lido)
		"""
		arquivo = open(arquivo, 'r')
		line = arquivo.readlines()
		last_line = line[len(line)-1]
		arquivo.close()
		return last_line

	def create_txt(arquivo):
		"""
		Cria um arquivo TXT
		(arquivo = Diretorio completo do arquivo txt a ser criado)
		"""
		arquivo = open(arquivo, 'w')
		arquivo.close()


class agendamento(arquivo):

	def __init__ (self, arquivo):
		arquivo.__init__(self, arquivo)

	def file_delete(arquivo = None):
		"""
		Exlcui arquivo especificado.
		Argumento obrigatorio é o path do arquivo.
		"""
		if arquivo == None:
			return 'Obrigatorio especificar caminho do Arquivo.'
		else:
			remove(arquivo)
			print(f'{arquivo}\nArquivo acima foi Excluido!')		


class consolidar:

	def __init__(self, arquivo):
		"""
		Consolida os arquivos de Agendamento e Cancelamento
		tem duas instancias sendo: agendamento() e cancelamento()
		"""
		arquivo.__init__(self, arquivo)

	def csv_files(arquivo):
		"""
		Consolida os arquivos recebidos
		(Path = Diretorio com os arquivos)
		"""
		Geral = []
		files = glob.glob(arquivo + '*.CSV')
		for f in files:
			try:
				df = pd.read_csv(f, encoding = 'ANSI', sep = ';')
			except:
				df = pd.read_csv(f, encoding = 'UTF-8', sep = ';')
			for k in range(0,100000):
				try:
					valor = df.iloc[k]
					Geral.append(valor)
				except:
					break
		df2 = pd.DataFrame(Geral)
		df2.to_csv(arquivo + 'Total_Agend.CSV', header = 1, sep = ';', index = False)
