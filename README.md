# RenpyRPG

Turn-Based RPG Game
Deskripsi

Game RPG berbasis giliran di mana pemain (Hero) harus melawan dua musuh, yaitu Goblin dan Orc. Pemain memiliki opsi serangan, skill, bertahan (guard), atau melarikan diri (run). Sistem ini menggunakan cooldown untuk skill agar gameplay menjadi lebih strategis.
Struktur Folder

Berikut adalah struktur folder proyek ini:
```
project_name/
├── game/
│   ├── images/                 # Folder untuk gambar yang digunakan dalam game
│   │   ├── hero.png            # Gambar karakter utama (Hero)
│   │   ├── goblin.png          # Gambar musuh Goblin
│   │   ├── orc.png             # Gambar musuh Orc
│   │   ├── attack.png          # Gambar aksi serangan
│   │   ├── fireball.png        # Gambar aksi skill Fireball
│   │   ├── heal.png            # Gambar aksi skill Heal
│   │   ├── defend.png          # Gambar aksi bertahan
│   ├── battle_setup.rpy        # Inisialisasi data karakter dan setup awal pertempuran
│   ├── player_turn.rpy         # Logika giliran pemain (serangan, guard, dll.)
│   ├── player_skill.rpy        # Logika skill pemain, termasuk sistem cooldown
│   ├── enemy_turn.rpy          # Logika giliran musuh (serangan berdasarkan peluang)
│   ├── victory_defeat.rpy      # Hasil akhir permainan (kemenangan/kekalahan)
│   ├── script.rpy              # Intro dan navigasi utama
├── renpy/                      # Folder engine Ren'Py (default dari Ren'Py)
├── common/                     # Folder aset umum Ren'Py (default dari Ren'Py)
├── options.rpy                 # Konfigurasi proyek seperti ukuran layar, nama proyek, dll.
└── gui/                        # Folder GUI default untuk game
```
