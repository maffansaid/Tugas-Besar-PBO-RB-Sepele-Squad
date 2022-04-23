import pygame, pygame.locals

UKURAN_LAYAR = (850, 500)

pygame.init()

Layar = pygame.display.set_mode(UKURAN_LAYAR)

pygame.display.set_caption('Petualangan Si Pele By Sepele.SQD')

berjalan = True
while berjalan:
	Layar.fill((255, 255, 255))
  
  for acara in pygame.event.get():
    if acara.type == pygame.QUIT:
      berjalan = False

  pygame.display.flip()

pygame.quit()
