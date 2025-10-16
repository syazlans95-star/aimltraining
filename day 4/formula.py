# Contoh asas simbol penting Python

# 1️⃣ " " atau ' ' — String (teks)
name = "Syazlan"
food = 'fried chicken'

# 2️⃣ () — digunakan dalam fungsi
print("Hello,", name)

# 3️⃣ \n — baris baru
print("Saya suka makan:\n", food)

# 4️⃣ \t — tab (jarak)
print("Menu hari ini:\tNasi + Ayam Goreng")

# 5️⃣ [] — senarai (list)
my_list = ["chicken", "fish", "egg"]
print("Senarai makanan:", my_list)

# 6️⃣ {} — dictionary (data berpasangan)
info = {"name": "Syazlan", "age": 29}
print("Maklumat:", info)

# 7️⃣ : — digunakan dalam fungsi, loop, if, dictionary
if 5 > 3:
    print("5 lebih besar dari 3")

# 8️⃣ # — komen (Python akan abaikan baris ni)
# Ini contoh komen

# 9️⃣ \\ — backslash sebenar (bila nak tulis tanda \)
print("Folder: C:\\Users\\Syazlan")

# 🔟 ''' ''' atau """ """ — multi-line string (teks panjang)
text = """
Ini contoh teks panjang.
Boleh tulis banyak baris.
Tak perlu guna \n berulang kali.
"""
print(text)

# 11️⃣ % atau f"" — untuk format teks
print(f"Nama saya {name} dan saya suka {food}.")
