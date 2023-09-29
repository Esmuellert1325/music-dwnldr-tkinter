import tkinter as tk
import service as Service

window = tk.Tk()
window.geometry("1000x650")
window.title("Youtube Music Downloader")

videos = [{"title": "Brother Loui - Modern Talking", "url": "https://"}, {"title": "Music", "url": "https://"}, {"title": "Music", "url": "https://"}, {"title": "Music", "url": "https://"}, {"title": "Music", "url": "https://"}, {"title": "Music", "url": "https://"},]

def update_button_text(event=None):
    text_content = textbox.get("1.0", "end-1c")  # Get the content of the Text widget
    if "https" in text_content.lower():
        button_search.config(text="DOWNLOAD")
        button_search.config(command=lambda: download_video('url'))
    else:
        button_search.config(text="SEARCH")

def clear_text():
    add_videos_to_container()
    textbox.delete(1.0, tk.END)

def create_video_box(video):
    video_frame = tk.Frame(container, bd=1, bg="white", padx=10, pady=10)
    video_frame.pack(pady=5, fill=tk.X)

    #label = tk.Label(video_frame, image=video['url'])
    #label.pack(side=tk.LEFT)
    
    title_label = tk.Label(video_frame, text=video['title'])
    title_label.pack(side=tk.LEFT, padx=10)
    
    download_button = tk.Button(video_frame, text="Download", command=lambda: download_video(video['url']))
    download_button.pack(side=tk.RIGHT)

def add_videos_to_container():
    for video in videos:
        create_video_box(video)
        #label = tk.Label(scrollable_frame, font=("Arial", 20), text=video, wraplength=300)
        #label.pack(fill='x', padx=10, pady=5)

def download_video(url: str):
    print(url)

# Title
header = tk.Label(text="Youtube Music Downloader", font=("Arial", 28))
header.pack(padx=20, pady=20)

# Input box
textbox = tk.Text(window, height=2, font=("Arial", 16))
textbox.bind("<KeyRelease>", update_button_text)
textbox.pack(padx=200, pady=20)

# Search button
button_search = tk.Button(window, width=10, height=1, font=("Arial", 14), text="SEARCH", bg="red", fg="white", command=clear_text)
button_search.pack()

# Container logic
#container = tk.Frame(window, width=200, height=100, background="green")
#container.pack(fill=tk.BOTH, expand=True)
#container.pack_forget()

canvas = tk.Canvas(window)
canvas.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(window, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

container = tk.Frame(canvas)
canvas.create_window((0, 0), window=container, anchor="nw")

container.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

window.mainloop()