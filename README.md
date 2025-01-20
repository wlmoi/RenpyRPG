# RenpyRPG
RenpyRPG/
├── game/
│   ├── images/
│   │   ├── hero.png          # Gambar karakter utama
│   │   ├── goblin.png        # Gambar musuh Goblin
│   │   ├── orc.png           # Gambar musuh Orc
│   │   ├── attack.png        # Gambar aksi serangan
│   │   ├── fireball.png      # Gambar aksi Fireball
│   │   ├── heal.png          # Gambar aksi Heal
│   │   ├── defend.png        # Gambar aksi bertahan
│   ├── battle_setup.rpy      # Inisialisasi data karakter, giliran pertama
│   ├── player_turn.rpy       # Logika aksi pemain (serangan, guard, dll.)
│   ├── player_skill.rpy      # Logika skill pemain (termasuk cooldown)
│   ├── enemy_turn.rpy        # Logika giliran musuh
│   ├── victory_defeat.rpy    # Hasil akhir (kemenangan/kekalahan)
│   ├── script.rpy            # Intro dan navigasi utama
├── renpy/                    # Folder engine Ren'Py
├── common/                   # Folder common assets Ren'Py
├── options.rpy               # Opsi konfigurasi proyek (dari Ren'Py)
└── gui/                      # GUI default untuk game
