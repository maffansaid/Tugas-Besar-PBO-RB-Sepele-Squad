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

def gambar(*variabel):
	def ambil_gambar(lokasi_file, nama_gambar):
		lokasi_gambar = os.path.join('Assets', lokasi_file, nama_gambar)
		file_gambar = pygame.image.load(lokasi_gambar)
		return file_gambar
	return [ambil_gambar(variabel[0], i) for i in variabel[1]]

GAMBAR_MENU_UTAMA = gambar('Menu_Utama', ('Background.jpg','Title.png', 'Play.png', 'Character.png', 'Setting.png', 'Exit.png', 'Info.png'))
	
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
