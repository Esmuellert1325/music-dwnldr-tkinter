import tkinter as tk
import service as Service

from PIL import Image, ImageTk
import requests
from io import BytesIO

window = tk.Tk()
window.geometry("1000x650")
window.title("Youtube Music Downloader")

videos = []

def update_button_text(event=None):
    text_content = textbox.get("1.0", "end-1c")  # Get the content of the Text widget
    if "https" in text_content.lower():
        button_search.config(text="DOWNLOAD")
        button_search.config(command=lambda: download_video(text_content))
    else:
        button_search.config(text="SEARCH")
        button_search.config(command=lambda: search_for_video(text_content))

def create_video_box(video):
    video_frame = tk.Frame(container, bd=1, bg="white", padx=10, pady=10)
    video_frame.pack(pady=5, fill=tk.X)
    #label = tk.Label(video_frame, image=video['cover'])
    #label.pack(side=tk.LEFT)
    response = requests.get(video['cover'])
    image_data = response.content

    image = Image.open(BytesIO(image_data))

    desired_width = 200  # Adjust this to your preferred width
    desired_height = 150  # Adjust this to your preferred height
    image.thumbnail((desired_width, desired_height))

    photo = ImageTk.PhotoImage(image)

    image_label = tk.Label(video_frame, image=photo)
    image_label.image = photo
    image_label.pack()

    title_label = tk.Label(video_frame, text=video['title'])
    title_label.pack(side=tk.LEFT, padx=10)
    
    download_button = tk.Button(video_frame, text="DOWNLOAD", command=lambda: download_video(video['url']), bg="red", fg="white")
    download_button.pack(side=tk.RIGHT)

def add_videos_to_container():
    for video in videos:
        create_video_box(video)
        #label = tk.Label(scrollable_frame, font=("Arial", 20), text=video, wraplength=300)
        #label.pack(fill='x', padx=10, pady=5)

def download_video(url: str):
    try:
        Service.get_video_by_url(url)
    except:
        print("Server error!")

def search_for_video(search_query: str):
    global videos
    videos = Service.get_videos_by_search(search_query)
    textbox.delete(1.0, tk.END)
    clear_container()
    add_videos_to_container()

def clear_container():
    for widget in container.winfo_children():
        widget.destroy()

# Title
header = tk.Label(text="Youtube Music Downloader", font=("Arial", 28))
header.pack(padx=20, pady=20)

# Input box
textbox = tk.Text(window, height=2, font=("Arial", 16))
textbox.bind("<KeyRelease>", update_button_text)
textbox.pack(padx=200, pady=20)

# Search button
button_search = tk.Button(window, width=10, height=1, font=("Arial", 14), text="SEARCH", bg="red", fg="white")
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
canvas.create_window((canvas.winfo_width() / 2, 0), window=container, anchor="n")

def on_mousewheel(event):
    canvas.yview_scroll(-1 * (event.delta // 120), "units")

canvas.bind_all("<MouseWheel>", on_mousewheel)

# Configure the canvas to update the scrollregion when the container changes size
def configure_scroll_region(event):
    canvas.config(scrollregion=canvas.bbox("all"))

container.bind("<Configure>", configure_scroll_region)

#container.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

window.mainloop()