import tkinter as tk
from tkinter import filedialog, messagebox
from steg import hide_data_in_image, extract_data_from_image
from crypto import encrypt_message, decrypt_message

class CryptoStegGUI:
    def __init__(self, master):
        self.master = master
        master.title("🔐 CryptoSteg")

        self.label = tk.Label(master, text="Message to Hide:")
        self.label.pack()

        self.message_entry = tk.Entry(master, width=50)
        self.message_entry.pack()

        self.pwd_label = tk.Label(master, text="Password:")
        self.pwd_label.pack()

        self.password_entry = tk.Entry(master, show="*", width=50)
        self.password_entry.pack()

        self.select_button = tk.Button(master, text="Select Image", command=self.select_image)
        self.select_button.pack(pady=4)

        self.hide_button = tk.Button(master, text="🔒 Hide Message", command=self.hide_message)
        self.hide_button.pack(pady=4)

        self.extract_button = tk.Button(master, text="🔓 Extract Message", command=self.extract_message)
        self.extract_button.pack(pady=4)

    def select_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.bmp *.jpg")])
        if self.image_path:
            messagebox.showinfo("Selected", f"Image: {self.image_path}")

    def hide_message(self):
        msg = self.message_entry.get()
        pwd = self.password_entry.get()

        if not msg or not pwd or not hasattr(self, "image_path"):
            messagebox.showerror("Error", "Please provide message, password and image.")
            return

        try:
            encrypted = encrypt_message(msg, pwd)
            save_path = filedialog.asksaveasfilename(defaultextension=".png")
            if save_path:
                hide_data_in_image(self.image_path, encrypted, save_path)
                messagebox.showinfo("Success", f"Message hidden in {save_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def extract_message(self):
        stego_path = filedialog.askopenfilename(title="Select Stego Image", filetypes=[("Image Files", "*.png")])
        pwd = self.password_entry.get()
        if not stego_path or not pwd:
            messagebox.showerror("Error", "Please select image and enter password.")
            return
        try:
            encrypted = extract_data_from_image(stego_path)
            decrypted = decrypt_message(encrypted, pwd)
            messagebox.showinfo("Message", f"Decrypted message:\n{decrypted.decode()}")
        except Exception as e:
            messagebox.showerror("Decryption Failed", str(e))

if __name__ == "__main__":
    print("Launching CryptoSteg GUI...")
    root = tk.Tk()
    gui = CryptoStegGUI(root)
    root.mainloop()
