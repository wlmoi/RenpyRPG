init python:
    import random

    # Data karakter utama
    protagonist = {
        "name": "Hero",
        "hp": 100,
        "max_hp": 100,
        "attack": 10,
        "defense": 5,
        "skills": {
            "fireball": {"damage": 20, "cooldown": 2, "last_used": -999},
            "heal": {"healing": 30, "cooldown": 3, "last_used": -999},
            "double_slash": {"damage": 15, "cooldown": 1, "last_used": -999},
        },
    }

    # Data musuh
    enemy1 = {"name": "Goblin", "hp": 50, "max_hp": 50, "attack": 8}
    enemy2 = {"name": "Orc", "hp": 75, "max_hp": 75, "attack": 12}

    # Variabel turn tracking
    current_turn = 0  # Digunakan untuk cooldown tracking

label battle_setup:
    # Tampilkan latar dan gambar musuh
    scene bg battlefield
    show goblin at left
    show orc at right

    "Seekor Goblin dan Orc muncul! Bersiaplah untuk bertarung!"

    # Mulai giliran pertama
    $ current_turn = 1
    jump player_turn
