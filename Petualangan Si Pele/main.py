import pygame, os

pygame.init()

# > NILAI POKOK (KONSTANTA)
UKURAN_LAYAR = (852, 480)

# > KELAS (CLASS)
class GLOBAL(pygame.sprite.Sprite):
	def __init__(self, **G_var):
		super(GLOBAL, self).__init__()
		self.ukuran = (G_var['panjang'], G_var['lebar'])
		self.pos = (G_var['x'], G_var['y'])
		self.gambar = pygame.transform.scale(G_var['gambar'], self.ukuran)
		self.posisi = self.gambar.get_rect(center = self.pos)

class Tombol(GLOBAL):
	def __init__(self, **var):
		super().__init__(**var)

# > FUNGSI / METODE
def gambar():
	def ambil_gambar(nama_gambar):
		lokasi_gambar = os.path.join('Assets','Menu',nama_gambar)
		file_gambar = pygame.image.load(lokasi_gambar)
		return file_gambar
	return {'bg' : ambil_gambar('Background.jpg'),
			'icon' : ambil_gambar('Title.png'),
			'mulai' : ambil_gambar('Play.png'),
			'karakter' : ambil_gambar('Character.png'),
			'pengaturan' : ambil_gambar('Setting.png'),
			'keluar' : ambil_gambar('Exit.png'),
			'informasi' : ambil_gambar('Info.png')}

# > NILAI POKOK (KONSTANTA)
GAMBAR = gambar()

# > OBJEK (OBJECT)
Tombol_mulai = Tombol(
	panjang = 150,
	lebar = 75,
	x = UKURAN_LAYAR[0] / 2 + 5,
	y = 230,
	gambar = GAMBAR['mulai']
)
Tombol_karakter = Tombol(
	panjang = 150,
	lebar = 75,
	x = UKURAN_LAYAR[0] / 2,
	y = 290,
	gambar = GAMBAR['karakter']
)
Tombol_pengaturan = Tombol(
	panjang = 150,
	lebar = 75,
	x = UKURAN_LAYAR[0] / 2,
	y = 350,
	gambar = GAMBAR['pengaturan']
)
Tombol_keluar = Tombol(
	panjang = 150,
	lebar = 75,
	x = UKURAN_LAYAR[0] / 2,
	y = 410,
	gambar = GAMBAR['keluar']
)
Tombol_informasi = Tombol(
	panjang = 50,
	lebar = 50,
	x = UKURAN_LAYAR[0] - 30,
	y = UKURAN_LAYAR[1] - 30,
	gambar = GAMBAR['informasi']
)


TOMBOL_MENU = pygame.sprite.Group()
TOMBOL_MENU.add(Tombol_mulai, Tombol_karakter, Tombol_pengaturan, Tombol_keluar, Tombol_informasi)


# > PROGRAM UTAMA
Layar = pygame.display.set_mode(UKURAN_LAYAR)
# Layar = pygame.display.set_mode(UKURAN_LAYAR, pygame.RESIZABLE)

pygame.display.set_caption('Petualangan Si Pele By Sepele.SQD')
pygame.display.set_icon(GAMBAR['icon'])

# Latar_Belakang = pygame.transform.scale(GAMBAR['bg'], UKURAN_LAYAR)
Latar_Belakang = GAMBAR['bg']
Judul = pygame.transform.scale(GAMBAR['icon'], (400, GAMBAR['icon'].get_height() * (400 / GAMBAR['icon'].get_width())))

Waktu = pygame.time.Clock()

berjalan = True

while berjalan:
	for acara in pygame.event.get():
		if acara.type == pygame.QUIT:
			berjalan = False
	Layar.fill((255, 255, 255))
	Layar.blit(Latar_Belakang, (0, 0))
	Layar.blit(Judul, (Judul.get_rect(center = (UKURAN_LAYAR[0] / 2, 80))))
	
	for tombol in TOMBOL_MENU:
		Layar.blit(tombol.gambar, tombol.posisi)

	pygame.display.flip()
	Waktu.tick(30)

pygame.quit()