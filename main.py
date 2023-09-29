import tkinter as tk
import service as Service

window = tk.Tk()
window.geometry("1000x650")
window.title("Youtube Music Downloader")

video_boxes = ["Music", "Music", "Music", "Music", "Music"]

def update_button_text(event=None):
    text_content = textbox.get("1.0", "end-1c")  # Get the content of the Text widget
    if "https" in text_content.lower():
        button_search.config(text="DOWNLOAD")
    else:
        button_search.config(text="SEARCH")

# Title
header = tk.Label(text="Youtube Music Downloader", font=("Arial", 28))
header.pack(padx=20, pady=20)

# Input box
textbox = tk.Text(window, height=2, font=("Arial", 16))
textbox.bind("<KeyRelease>", update_button_text)
textbox.pack(padx=200, pady=20)

# Search button
button_search = tk.Button(window, text="SEARCH", bg="red", fg="white", command=print("Ok"))
button_search.pack()

# Container logic
container = tk.Frame(window, width=200, height=100, background="green")
container.pack(fill=tk.BOTH, expand=True)
container.pack_forget()

label = tk.Label(container, text="Music Box", padx=20, pady=20)
label.pack()


window.mainloop()