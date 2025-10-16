# Buat custom exception (kesalahan sendiri)
class InvalidMarkError(Exception):
    pass

while True:
    try:
        mark = int(input("Masukkan markah (0 - 50): "))

        if mark < 0 or mark > 50:
            # Kalau luar julat, naikkan error
            raise InvalidMarkError("Markah tak sah! Sila masukkan antara 0 hingga 50.")
        
        # Kalau betul, keluar dari loop
        print("Markah sah ✅:", mark)
        break

    except ValueError:
        print("Sila masukkan nombor sahaja ya.")
    except InvalidMarkError as e:
        print(e)

