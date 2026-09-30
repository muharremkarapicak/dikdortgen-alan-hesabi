# Dikdörtgenin alanını hesaplayan basit bir program

print("--- Dikdörtgen Alan Hesaplayıcı ---")

# Kullanıcıdan kısa ve uzun kenar bilgilerini alıyoruz
kisa_kenar = int(input("Kısa kenar uzunluğunu giriniz: "))
uzun_kenar = int(input("Uzun kenar uzunluğunu giriniz: "))

# Alanı hesaplıyoruz (Kısa Kenar ile Uzun Kenarı çarpıyoruz)
alan = kisa_kenar * uzun_kenar

# Sonucu ekrana yazdırıyoruz
print(f"Girdiğiniz ölçülere göre dikdörtgenin alanı: {alan}")
