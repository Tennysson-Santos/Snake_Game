import pygame

import random


#fazer a cobrinha
class Cobrinha:
	cor = (255, 255, 255)
	tamanho = (10, 10)
	velocidade = 10
	
	def __init__(self):
		self.textura = pygame.Surface(self.tamanho)
		self.textura.fill(self.cor)

		self.corpo = [(100, 100), (90, 100), (80, 100)]
		self.direcao = 'direita'
		self.pontos = 0

	def tela(self, tela):
		for posicao in self.corpo:
			tela.blit(self.textura, posicao)
	
	def andar(self):
		
		cabeca = self.corpo[0]
		x = cabeca[0]
		y = cabeca[1]
		
		if self.direcao == 'direita':
			self.corpo.insert(0, (x + self.velocidade, y))
			
		elif self.direcao == 'esquerda':
			self.corpo.insert(0, (x - self.velocidade, y))
			
		elif self.direcao == 'cima':
			self.corpo.insert(0, (x, y - self.velocidade))
			
		elif self.direcao == 'baixo':
			self.corpo.insert(0, (x, y + self.velocidade))
			
		self.corpo.pop(-1)
	
	def cima(self):
		if self.direcao != 'baixo':
			self.direcao = 'cima'	
		
	def baixo(self):
		if self.direcao != 'cima':
			self.direcao = 'baixo'	
		
	def direita(self):
		if self.direcao != 'esquerda':
			self.direcao = 'direita'	
		
	def esquerda(self):
		if self.direcao != 'direita':
			self.direcao = 'esquerda'	
			
	def colisao_frutinha(self, frutinha):
		return self.corpo[0] == frutinha.posicao

	def comer(self):
		self.corpo.append((0, 0))
		self.pontos += 1
		pygame.display.set_caption(f'Game Snake  Pontos:{self.pontos}')
		
	def colisao(self):
		cabeca = self.corpo[0]
		x = cabeca[0]
		y = cabeca[1]
		
		calda = self.corpo[1:]
		
		return x < 0 or y < 0 or x > 490 or y > 490 or cabeca in calda
		

#fazer a frutinha
class Frutinha:
	cor = (255, 0, 0)
	tamanho = (10, 10)
	
	
	
	def __init__(self):
		self.textura = pygame.Surface(self.tamanho)
		self.textura.fill(self.cor)
		
		x = random.randint(0, 49)* 10
		y = random.randint(0, 49)* 10
		self.posicao = (x, y)
	
	def tela(self, tela):
		tela.blit(self.textura, self.posicao)
		
	
if __name__ == "__main__":
	#inicia o pygame
	pygame.init()

	#resolução da tela
	resolucao = (500,500)
	tela = pygame.display.set_mode(resolucao)

	#nome do jogo na tela
	pygame.display.set_caption('Game Snake')

	#definir fps
	clock = pygame.time.Clock()

	#cor da tela
	cor_tela =(0, 0, 0)
		
	frutinha = Frutinha()
	
	cobrinha = Cobrinha()

#deixa a tela aberta até que fechar ela
	while True:
		clock.tick(20)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					cobrinha.cima()
					break
				elif event.key == pygame.K_DOWN:
					cobrinha.baixo()
					break
				elif event.key == pygame.K_LEFT:
					cobrinha.esquerda()
					break
				elif event.key == pygame.K_RIGHT:
					cobrinha.direita()	
					break
					

		
		if cobrinha.colisao_frutinha(frutinha):
			cobrinha.comer()
			frutinha = Frutinha()
		
		if cobrinha.colisao():
			cobrinha = Cobrinha()
						
		cobrinha.andar()
		
		tela.fill(cor_tela)
		frutinha.tela(tela)
		cobrinha.tela(tela)
			
		pygame.display.update()
