try:
	import pygame, pygame.locals
except:
	print('#- Mohon Maaf Modul Pygame Tidak Ditemukan -#')
	exit()

import random

UKURAN_LAYAR = (960, 540)
TOMBOL_AKTIF = 0

pygame.init()

def gambar(*variabel):
	def ambil_gambar(lokasi_file, nama_gambar):		
		return pygame.image.load(f'Assets\\{lokasi_file}\\{nama_gambar}')
	if len(variabel[1]) == 1:
		return ambil_gambar(variabel[0], variabel[1][0])	
	return [ambil_gambar(variabel[0], i) for i in variabel[1]]


rubah_ukuran = lambda A,B,C: A * C / B

GAMBAR = {
	'MENU_UTAMA' : {
		'LatarBelakang' : gambar('Menu_Utama', ('LatarBelakang.jpg',)),
		'Mulai' 	: gambar('Menu_Utama', ('Mulai.png',)),
		'Karakter' 	: gambar('Menu_Utama', ('Karakter.png',)),
		'Pengaturan' 	: gambar('Menu_Utama', ('Pengaturan.png',)),
		'Keluar' 	: gambar('Menu_Utama', ('Keluar.png',)),
		'Info' 		: gambar('Menu_Utama', ('Info.png',)),
	}
}

class Tombol(pygame.sprite.Sprite):
	def __init__(self, **variabel):
		super(Tombol, self).__init__()
		self.id = variabel['id']
		self._ukuran = (variabel['panjang'], variabel['lebar'])
		self._pos = (variabel['x'], variabel['y'])
		self._file = variabel['gambar']
		self.gambar = pygame.transform.smoothscale(self._file, self._ukuran)
		self.posisi = self.gambar.get_rect(center = self._pos)
	def aktif(self, Layar):
		global TOMBOL_AKTIF
		if TOMBOL_AKTIF == self.id:
			self.gambar = pygame.transform.smoothscale(self._file, (self._ukuran[0] + 15, self._ukuran[1] + 15))
		else:
			self.gambar = pygame.transform.smoothscale(self._file, self._ukuran)
		self.posisi = self.gambar.get_rect(center = self._pos)
		Layar.blit(self.gambar, self.posisi)
		
TOMBOL = {
	'menu' : {
		'mulai' : Tombol(
			id = 0,
			panjang = 280,
			lebar = rubah_ukuran(
				GAMBAR['MENU_UTAMA']['Mulai'].get_height(),
				GAMBAR['MENU_UTAMA']['Mulai'].get_width(),
				280),
			x = UKURAN_LAYAR[0] / 4,
			y = 100,
			gambar = GAMBAR['MENU_UTAMA']['Mulai']
		),
		'karakter' : Tombol(
			id = 1,
			panjang = 280,
			lebar = rubah_ukuran(
				GAMBAR['MENU_UTAMA']['Karakter'].get_height(),
				GAMBAR['MENU_UTAMA']['Karakter'].get_width(),
				280),
			x = UKURAN_LAYAR[0] / 4,
			y = 200,
			gambar = GAMBAR['MENU_UTAMA']['Karakter']
		),
		'Pengaturan' : Tombol(
			id = 2,
			panjang = 280,
			lebar = rubah_ukuran(
				GAMBAR['MENU_UTAMA']['Pengaturan'].get_height(),
				GAMBAR['MENU_UTAMA']['Pengaturan'].get_width(),
				280),
			x = UKURAN_LAYAR[0] / 4,
			y = 300,
			gambar = GAMBAR['MENU_UTAMA']['Pengaturan']
		),
		'keluar' : Tombol(
			id = 3,
			panjang = 280,
			lebar = rubah_ukuran(
				GAMBAR['MENU_UTAMA']['Keluar'].get_height(),
				GAMBAR['MENU_UTAMA']['Keluar'].get_width(),
				280),
			x = UKURAN_LAYAR[0] / 4,
			y = 400,
			gambar = GAMBAR['MENU_UTAMA']['Keluar']
		),
		'informasi' : Tombol(
			id = 4,
			panjang = 60,
			lebar = 60,
			x = UKURAN_LAYAR[0] - 50,
			y = UKURAN_LAYAR[1] - 50,
			gambar = GAMBAR['MENU_UTAMA']['Info']
		)
	}
}
	
Layar = pygame.display.set_mode(UKURAN_LAYAR)

pygame.display.set_caption('Petualangan Si Pele By Sepele.SQD')

Latar_belakang = pygame.transform.smoothscale(
	GAMBAR['MENU_UTAMA']['LatarBelakang'], UKURAN_LAYAR)

musik = pygame.mixer.music.load('Assets\\Music\\Musik_Menu.mp3')
pygame.mixer.music.play(-1)

berjalan = True
while berjalan:
	Layar.blit(Latar_belakang, (0, 0))
	
	for tombol in TOMBOL['menu'].values():
		tombol.aktif(Layar)
	
	for acara in pygame.event.get():
		if acara.type == pygame.QUIT:
			berjalan = False
		elif acara.type == pygame.locals.KEYUP:
			if acara.key in (pygame.locals.K_DOWN, pygame.locals.K_RIGHT):
				TOMBOL_AKTIF = (TOMBOL_AKTIF + 1) % 5
			elif acara.key in (pygame.locals.K_UP, pygame.locals.K_LEFT):
				TOMBOL_AKTIF = (TOMBOL_AKTIF + 4) % 5
	pygame.display.flip()
pygame.quit()
