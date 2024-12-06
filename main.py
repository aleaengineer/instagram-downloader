import instaloader

# Membuat instance Instaloader
L = instaloader.Instaloader()

# Meminta input dari pengguna
username_target = input("Masukkan username target: ")

# Masuk dengan akun Instagram kamu
L.login('tiyassaputrii', '@Koplok12!!')

# Mengunduh semua konten dari profil pengguna target
L.download_profile(username_target, profile_pic=True)

print(f"Konten dari akun @{username_target} berhasil diunduh.")
