import tkinter as tk

def check_code():
    if entry.get() == "1234":
        root.destroy()
    else:
        label.config(text="Неверный код! Попробуй снова.")

root = tk.Tk()
root.title("WinLocker (шутка)")

# Полноэкранный режим
root.attributes("-fullscreen", True)

label = tk.Label(root, text="Ваш компьютер 'заблокирован'!\nВведите код:", font=("Arial", 24))
label.pack(pady=50)

entry = tk.Entry(root, show="*", font=("Arial", 24))
entry.pack(pady=20)

btn = tk.Button(root, text="Разблокировать", command=check_code, font=("Arial", 24))
btn.pack(pady=20)

root.mainloop()
