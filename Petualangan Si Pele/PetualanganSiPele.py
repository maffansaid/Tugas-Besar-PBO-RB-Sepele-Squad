try:
	import pygame, pygame.locals
except:
	print('#- Mohon Maaf Modul Pygame Tidak Ditemukan -#')
	exit()

import random

pygame.init()

UKURAN_LAYAR = (960, 540)
TOMBOL_AKTIF = 0

EFEK_SUARA = True
MUSIK = True
MUSIK_MENU = pygame.mixer.Sound('Assets\\Musik\\Musik_Menu.mp3')

def gambar(lokasi, nama):
	def ambil_gambar(lokasi_file, nama_gambar):
		return pygame.image.load(f'Assets\\{lokasi_file}\\{nama_gambar}')
	if len(nama) == 1:
		return ambil_gambar(lokasi, nama[0])	
	return [ambil_gambar(lokasi, i) for i in nama]

GAMBAR = {
	'MENU_UTAMA' : {
		'Icon' 		: gambar('Menu_Utama', ('Icon.jpg',)),
		'LatarBelakang' : gambar('Menu_Utama', ('LatarBelakang.jpg',)),
		'Mulai' 	: gambar('Menu_Utama', ('Mulai.png',)),
		'Karakter' 	: gambar('Menu_Utama', ('Karakter.png',)),
		'Pengaturan' 	: gambar('Menu_Utama', ('Pengaturan.png',)),
		'Keluar' 	: gambar('Menu_Utama', ('Keluar.png',)),
		'Info' 		: gambar('Menu_Utama', ('Info.png',)),
	},
	'MENU_PENGATURAN' : {
		'LatarBelakang' : gambar('Menu_Pengaturan', ('LatarBelakang.jpg',)),
		'Musik' 	: gambar('Menu_Pengaturan', ('Musik.png',)),
		'EfekSuara' 	: gambar('Menu_Pengaturan', ('EfekSuara.png',)),
		'MusikHidup' 	: gambar('Menu_Pengaturan', ('MusikHidup.png',)),
		'MusikMati' 	: gambar('Menu_Pengaturan', ('MusikMati.png',)),
		'Kembali' 	: gambar('Menu_Pengaturan', ('Kembali.png',))
	},
	'MENU_INFO' : {
		'Info' 		: gambar('Menu_Info', ('Info.png',)),
	},
}

class Tombol:
	def __init__(self, **variabel):
		self.id = variabel['id']
		self.__ukuran = (variabel['panjang'], variabel['lebar'])
		self.__posisi = (variabel['x'], variabel['y'])
		self.__file = variabel['gambar']
	def aktif(self, Layar):
		global TOMBOL_AKTIF
		if TOMBOL_AKTIF == self.id:
			gambar = pygame.transform.smoothscale(
				self.__file, (self.__ukuran[0] + 15, self.__ukuran[1] + 15))
		else:
			gambar = pygame.transform.smoothscale(
				self.__file, self.__ukuran)
		Layar.blit(gambar, gambar.get_rect(center = self.__posisi))
		
TOMBOL = {
	'menu' : {
		'mulai' : Tombol(
			id = 0,
			panjang = 280,
			lebar = 107,
			x = UKURAN_LAYAR[0] / 4,
			y = 100,
			gambar = GAMBAR['MENU_UTAMA']['Mulai']
		),
		'karakter' : Tombol(
			id = 1,
			panjang = 280,
			lebar = 107,
			x = UKURAN_LAYAR[0] / 4,
			y = 200,
			gambar = GAMBAR['MENU_UTAMA']['Karakter']
		),
		'Pengaturan' : Tombol(
			id = 2,
			panjang = 280,
			lebar = 107,
			x = UKURAN_LAYAR[0] / 4,
			y = 300,
			gambar = GAMBAR['MENU_UTAMA']['Pengaturan']
		),
		'keluar' : Tombol(
			id = 3,
			panjang = 280,
			lebar = 107,
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
	},
	'pengaturan' : {
		'musik' : Tombol(
			id = 0,
			panjang = 340,
			lebar = 88,
			x = UKURAN_LAYAR[0] / 2,
			y = 210,
			gambar = GAMBAR['MENU_PENGATURAN']['Musik']
		),
		'efek_suara' : Tombol(
			id = 1,
			panjang = 340,
			lebar = 88,
			x = UKURAN_LAYAR[0] / 2,
			y = 300,
			gambar = GAMBAR['MENU_PENGATURAN']['EfekSuara']
		),
		'kembali' : Tombol(
			id = 2,
			panjang = 70,
			lebar = 70,
			x = 70,
			y = UKURAN_LAYAR[1] - 50,
			gambar = GAMBAR['MENU_PENGATURAN']['Kembali']
		)
	}
}

def Menu_pengaturan(Layar):
	global UKURAN_LAYAR, GAMBAR, TOMBOL, TOMBOL_AKTIF, MUSIK, EFEK_SUARA
	
	TOMBOL_AKTIF = 0
	
	Latar_belakang = pygame.transform.smoothscale(
		GAMBAR['MENU_PENGATURAN']['LatarBelakang'].convert(), 
		UKURAN_LAYAR)
	
	Suara_hidup = pygame.transform.smoothscale(
		GAMBAR['MENU_PENGATURAN']['MusikHidup'], (50, 50))
	Suara_mati = pygame.transform.smoothscale(
		GAMBAR['MENU_PENGATURAN']['MusikMati'], (50, 50))
	
	posisi_musik = Suara_hidup.get_rect(
		center = (UKURAN_LAYAR[0] / 2 + 120, 210))
	posisi_efek_suara = Suara_hidup.get_rect(
		center = (UKURAN_LAYAR[0] / 2 + 120, 300))

	while True:
		Layar.blit(Latar_belakang, (0, 0))
		
		if MUSIK:
			musik = Suara_hidup
		else:
			musik = Suara_mati
		Layar.blit(musik, posisi_musik)
		
		if EFEK_SUARA:
			efek_suara = Suara_hidup
		else:
			efek_suara = Suara_mati
		Layar.blit(efek_suara, posisi_efek_suara)
		
		for tombol in TOMBOL['pengaturan'].values():
			tombol.aktif(Layar)

		for acara in pygame.event.get():
			if acara.type == pygame.QUIT:
				return False
			elif acara.type == pygame.locals.KEYUP:
				if acara.key in (pygame.locals.K_DOWN, pygame.locals.K_RIGHT):
					TOMBOL_AKTIF = (TOMBOL_AKTIF + 1) % 3
				elif acara.key in (pygame.locals.K_UP, pygame.locals.K_LEFT):
					TOMBOL_AKTIF = (TOMBOL_AKTIF + 2) % 3	
				elif acara.key == pygame.locals.K_RETURN:
					for tombol in TOMBOL['pengaturan'].values():
						if TOMBOL_AKTIF == tombol.id:
							if tombol.id == 0:
								MUSIK = not MUSIK
								if MUSIK:
									pygame.mixer.music.unpause()
								else:
									pygame.mixer.music.pause()
							elif tombol.id == 1:
								EFEK_SUARA = not EFEK_SUARA
							elif tombol.id == 2:
								return True
							break
		pygame.display.flip()

# Program Utama (Menu Utama)
Layar = pygame.display.set_mode(UKURAN_LAYAR)

pygame.display.set_caption('Petualangan Si Pele By Sepele.SQD')
pygame.display.set_icon(GAMBAR['MENU_UTAMA']['Icon'].convert())

Latar_belakang = pygame.transform.smoothscale(
	GAMBAR['MENU_UTAMA']['LatarBelakang'].convert(), UKURAN_LAYAR)

Latar_belakang_info = pygame.Surface(UKURAN_LAYAR)
Latar_belakang_info.fill((0, 0, 0))
Latar_belakang_info.set_alpha(150)

Gambar_Info = pygame.transform.smoothscale(
	GAMBAR['MENU_INFO']['Info'], (600, 400))
Posisi_Info = Gambar_Info.get_rect(
	center = (UKURAN_LAYAR[0] / 2, UKURAN_LAYAR[1] / 2))

musik = pygame.mixer.music.load('Assets\\Musik\\Musik_Menu.mp3')
pygame.mixer.music.play(-1)

Utama = berjalan = True
while berjalan:
	Layar.blit(Latar_belakang, (0, 0))
	
	for tombol in TOMBOL['menu'].values():
		tombol.aktif(Layar)
		
	if not Utama:
		Layar.blit(Latar_belakang_info, (0, 0))
		Layar.blit(Gambar_Info, Posisi_Info)
		
	for acara in pygame.event.get():
		if acara.type == pygame.QUIT:
			berjalan = False
		elif acara.type == pygame.locals.KEYUP:
			if acara.key in (pygame.locals.K_DOWN, pygame.locals.K_RIGHT):
				TOMBOL_AKTIF = (TOMBOL_AKTIF + 1) % 5
			elif acara.key in (pygame.locals.K_UP, pygame.locals.K_LEFT):
				TOMBOL_AKTIF = (TOMBOL_AKTIF + 4) % 5
			elif acara.key == pygame.locals.K_RETURN:
				if Utama:
					for tombol in TOMBOL['menu'].values():
						if TOMBOL_AKTIF == tombol.id:
							if tombol.id == 2:
								berjalan = Menu_pengaturan(Layar)
							elif tombol.id == 3:
								berjalan = False
							elif tombol.id == 4:
								Utama = False
							TOMBOL_AKTIF = tombol.id
							break
				else:
					Utama = True
	pygame.display.flip()
pygame.quit()
