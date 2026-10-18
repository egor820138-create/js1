from textblob import TextBlob
import tkinter as tk

def ask():
    question = entry.get()
    blob = TextBlob(question)
    # Пример: определяем язык и настроение
    answer = f"Язык: {blob.detect_language()}, Полярность: {blob.sentiment.polarity}"
    chat.insert(tk.END, "Ты: " + question + "\n")
    chat.insert(tk.END, "ИИ: " + answer + "\n\n")
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("ИИ-бот (TextBlob)")
root.geometry("600x400")

chat = tk.Text(root, font=("Arial", 12))
chat.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(fill="x", padx=10, pady=5)

btn = tk.Button(root, text="Спросить", command=ask, font=("Arial", 14))
btn.pack(pady=5)

root.mainloop()
