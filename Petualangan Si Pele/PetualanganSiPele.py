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

EFEK_TOMBOL_GESER = pygame.mixer.Sound('Assets\\Efek_Suara\\Tombol_Geser.wav')
EFEK_TOMBOL_TEKAN = pygame.mixer.Sound('Assets\\Efek_Suara\\Tombol_Tekan.mp3')

tombol_atas = pygame.locals.K_UP
tombol_bawah = pygame.locals.K_DOWN
tombol_kanan = pygame.locals.K_RIGHT
tombol_kiri = pygame.locals.K_LEFT
tombol_bawah_kanan = (tombol_bawah, tombol_kanan)
tombol_atas_kiri = (tombol_atas, tombol_kiri)

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
			x = 240,
			y = 100,
			gambar = GAMBAR['MENU_UTAMA']['Mulai']
		),
		'karakter' : Tombol(
			id = 1,
			panjang = 280,
			lebar = 107,
			x = 240,
			y = 200,
			gambar = GAMBAR['MENU_UTAMA']['Karakter']
		),
		'Pengaturan' : Tombol(
			id = 2,
			panjang = 280,
			lebar = 107,
			x = 240,
			y = 300,
			gambar = GAMBAR['MENU_UTAMA']['Pengaturan']
		),
		'keluar' : Tombol(
			id = 3,
			panjang = 280,
			lebar = 107,
			x = 240,
			y = 400,
			gambar = GAMBAR['MENU_UTAMA']['Keluar']
		),
		'informasi' : Tombol(
			id = 4,
			panjang = 60,
			lebar = 60,
			x = 910,
			y = 490,
			gambar = GAMBAR['MENU_UTAMA']['Info']
		)
	},
	'pengaturan' : {
		'musik' : Tombol(
			id = 0,
			panjang = 340,
			lebar = 88,
			x = 480,
			y = 210,
			gambar = GAMBAR['MENU_PENGATURAN']['Musik']
		),
		'efek_suara' : Tombol(
			id = 1,
			panjang = 340,
			lebar = 88,
			x = 480,
			y = 300,
			gambar = GAMBAR['MENU_PENGATURAN']['EfekSuara']
		),
		'kembali' : Tombol(
			id = 2,
			panjang = 70,
			lebar = 70,
			x = 70,
			y = 490,
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

	while True:
		Layar.blit(Latar_belakang, (0, 0))
		
		for tombol in TOMBOL['pengaturan'].values():
			tombol.aktif(Layar)

		musik = Suara_hidup if MUSIK else Suara_mati
		Layar.blit(musik, musik.get_rect(center = (600, 210)))

		efek_suara = Suara_hidup if EFEK_SUARA else Suara_mati
		Layar.blit(efek_suara, efek_suara.get_rect(center = (600, 300)))
		
		for acara in pygame.event.get():
			if acara.type == pygame.QUIT:
				return False
			elif acara.type == pygame.locals.KEYUP:
				if acara.key in tombol_bawah_kanan or acara.key in tombol_atas_kiri:
					if EFEK_SUARA:
						EFEK_TOMBOL_GESER.play()
					if acara.key in tombol_bawah_kanan:
						TOMBOL_AKTIF = (TOMBOL_AKTIF + 1) % 3
					elif acara.key in tombol_atas_kiri:
						TOMBOL_AKTIF = (TOMBOL_AKTIF + 2) % 3
				elif acara.key == pygame.locals.K_RETURN:
					if EFEK_SUARA:
						EFEK_TOMBOL_TEKAN.play()
					for tombol in TOMBOL['pengaturan'].values():
						if TOMBOL_AKTIF == tombol.id:
							if tombol.id == 0:
								MUSIK = not MUSIK
								if MUSIK:
									MUSIK_MENU.play(-1)
								else:
									MUSIK_MENU.stop()
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

MUSIK_MENU.play(-1)

Utama = berjalan = True
while berjalan:
	Layar.blit(Latar_belakang, (0, 0))
	
	for tombol in TOMBOL['menu'].values():
		tombol.aktif(Layar)
		
	if not Utama:
		Layar.blit(Latar_belakang_info, (0, 0))
		Layar.blit(Gambar_Info, Gambar_Info.get_rect(center = (480, 270)))
		
	for acara in pygame.event.get():
		if acara.type == pygame.QUIT:
			berjalan = False
		elif acara.type == pygame.locals.KEYUP:
			if Utama and (acara.key in tombol_bawah_kanan or acara.key in tombol_atas_kiri):
				if EFEK_SUARA:
					EFEK_TOMBOL_GESER.play()
				if acara.key in tombol_bawah_kanan:
					TOMBOL_AKTIF = (TOMBOL_AKTIF + 1) % 5
				elif acara.key in tombol_atas_kiri:
					TOMBOL_AKTIF = (TOMBOL_AKTIF + 4) % 5
			elif acara.key == pygame.locals.K_RETURN:
				if EFEK_SUARA:
					EFEK_TOMBOL_TEKAN.play()
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
