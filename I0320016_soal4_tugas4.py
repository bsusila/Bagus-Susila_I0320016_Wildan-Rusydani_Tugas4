umur = 21
x = int(input("Berapa umur Anda :"))
if umur <= x :
    print("Anda cukup umur")
    y = input("Apakah Anda sudah lulus ujian kualifikasi (Y/T) :")
    if y == "Y" :
        print("Anda boleh mendaftar di kursus.")
    elif y == "T" :
        print("Anda tidak boleh mendaftar di kursus.")
else :
    print("Anda belum cukup umur")