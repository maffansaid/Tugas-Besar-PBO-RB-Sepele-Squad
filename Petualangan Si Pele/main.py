import pygame, os, pygame.locals

UKURAN_LAYAR = (850, 500)

pygame.init()
class GLOBAL(pygame.sprite.Sprite):
	def __init__(self, **variabel):
		super(GLOBAL, self).__init__()
		self.id = variabel['id']
		self.ukuran = (variabel['panjang'], variabel['lebar'])
		self.pos = (variabel['x'], variabel['y'])
		self.file = variabel['gambar']
		self.gambar = pygame.transform.scale(self.file, self.ukuran)
		self.posisi = self.gambar.get_rect(center = self.pos)
	def aktif(self):
		pass
	def aksi(self):
		pass

def tempat_gambar(*variabel):
	def ambil_gambar(lokasi_file, nama_gambar):
		lokasi_gambar = os.path.join('Assets', lokasi_file, nama_gambar)
		file_gambar = pygame.image.load(lokasi_gambar)
		return file_gambar
	return {'key' : ambil_gambar(variabel[0],variabel[1])}
	
class Tombol(GLOBAL):
	def __init__(self, **variabel):
		pass
	
Tombol_mulai = Tombol(
    id=,
    panjang=,
    lebar=,
    x=,
    y=,
    gambar=)
Tombol_karakter = Tombol(
    id=,
    panjang=,
    lebar=,
    x=,
    y=,
    gambar=)
Tombol_pengaturan = Tombol(
    id=,
    panjang=,
    lebar=,
    x=,
    y=,
    gambar=)
Tombol_keluar = Tombol(
    id=,
    panjang=,
    lebar=,
    x=,
    y=,
    gambar=)
Tombol_informasi = Tombol(
    id=,
    panjang=,
    lebar=,
    x=,
    y=,
    gambar=)

TOMBOL_MENU = pygame.sprite.Group()
TOMBOL_MENU.add(Tombol_mulai, Tombol_karakter,Tombol_pengaturan, Tombol_keluar, Tombol_informasi)
	
Layar = pygame.display.set_mode(UKURAN_LAYAR)

pygame.display.set_caption('Petualangan Si Pele By Sepele.SQD')

berjalan = True
while berjalan:
	Layar.fill((255, 255, 255))
	for tombol in TOMBOL_MENU:
        	Layar.blit(tombol.gambar, tombol.posisi)
		
	for acara in pygame.event.get():
      	 	if acara.type == pygame.QUIT:
            		berjalan = False


	pygame.display.flip()

pygame.quit()
