import tkinter as tk
from tkinter import colorchooser, filedialog
from PIL import Image, ImageDraw

# إعداد النافذة
root = tk.Tk()
root.title("🎨 Hamza Paint")
root.geometry("800x600")
root.configure(bg="#f0f0f0")

# إعداد لوحة الرسم
canvas = tk.Canvas(root, bg="white", width=780, height=500)
canvas.pack(pady=20)

# إعداد الصورة في الخلفية لحفظها
image = Image.new("RGB", (780, 500), "white")
draw = ImageDraw.Draw(image)

# إعدادات الرسم
current_color = "black"
brush_size = 4
drawing = False
last_x, last_y = None, None

# بدء الرسم
def start_draw(event):
    global drawing, last_x, last_y
    drawing = True
    last_x, last_y = event.x, event.y

# الرسم المستمر
def draw_line(event):
    global last_x, last_y
    if drawing:
        canvas.create_line(last_x, last_y, event.x, event.y, fill=current_color, width=brush_size, capstyle=tk.ROUND)
        draw.line([last_x, last_y, event.x, event.y], fill=current_color, width=brush_size)
        last_x, last_y = event.x, event.y

# التوقف عن الرسم
def stop_draw(event):
    global drawing
    drawing = False

# اختيار اللون
def choose_color():
    global current_color
    color = colorchooser.askcolor()[1]
    if color:
        current_color = color

# الممحاة
def use_eraser():
    global current_color
    current_color = "white"

# مسح اللوحة
def clear_canvas():
    canvas.delete("all")
    draw.rectangle([0, 0, 780, 500], fill="white")

# حفظ الصورة
def save_image():
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG Files", "*.png")])
    if file_path:
        image.save(file_path)

# ربط الأحداث
canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw_line)
canvas.bind("<ButtonRelease-1>", stop_draw)

# الأزرار
buttons_frame = tk.Frame(root, bg="#f0f0f0")
buttons_frame.pack()

tk.Button(buttons_frame, text="🎨 لون", font=("Arial", 12), command=choose_color).pack(side="left", padx=10)
tk.Button(buttons_frame, text="🧽 ممحاة", font=("Arial", 12), command=use_eraser).pack(side="left", padx=10)
tk.Button(buttons_frame, text="🗑️ مسح الكل", font=("Arial", 12), command=clear_canvas).pack(side="left", padx=10)
tk.Button(buttons_frame, text="💾 حفظ", font=("Arial", 12), command=save_image).pack(side="left", padx=10)

tk.Label(root, text="by Hamza ❤️", font=("Arial", 10), bg="#f0f0f0", fg="gray").pack(pady=5)

root.mainloop()
