import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import qrcode
from tkinter import ttk

# Function to generate QR code
def generate_qr():
    link = entry.get().strip()
    if not link:
        messagebox.showwarning("Input Error", "Please enter a link or text!")
        return

    # Create QR code
    qr_img = qrcode.make(link)
    qr_img = qr_img.resize((250, 250))
    qr_tk = ImageTk.PhotoImage(qr_img)

    qr_label.config(image=qr_tk)
    qr_label.image = qr_tk
    save_btn.config(state="normal")

# Function to save QR code
def save_qr():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        link = entry.get().strip()
        qr_img = qrcode.make(link)
        qr_img.save(file_path)
        messagebox.showinfo("Saved", f"QR Code saved as {file_path}")

# ---------------- GUI ----------------
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x500")
root.config(bg="#1e1e2f")

# Heading
label = tk.Label(root, text="QR Code Generator", font=("Arial", 20, "bold"), bg="#1e1e2f", fg="white")
label.pack(pady=15)

# Entry bar
entry = ttk.Entry(root, font=("Arial", 14))
entry.pack(pady=10, padx=20, fill="x")

# Generate button
gen_btn = ttk.Button(root, text="Generate QR", command=generate_qr)
gen_btn.pack(pady=10)

# Animated loading bar (style)
progress = ttk.Progressbar(root, mode="indeterminate", length=250)
progress.pack(pady=10)

# Function to animate button click
def start_progress():
    progress.start(10)
    root.after(1000, progress.stop)  # stop after 1 second

gen_btn.config(command=lambda: [start_progress(), generate_qr()])

# QR Code display area
qr_label = tk.Label(root, bg="#1e1e2f")
qr_label.pack(pady=20)

# Save button
save_btn = ttk.Button(root, text="Save QR", command=save_qr, state="disabled")
save_btn.pack(pady=10)

root.mainloop()

