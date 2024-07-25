import os
import sys
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
import pytesseract
from pytesseract import TesseractError
import subprocess

def check_tesseract_installed():
    try:
        subprocess.run(['tesseract', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        return False

def extract_text_from_image(image_path, lang='eng'):
    try:
        with Image.open(image_path) as img:
            text = pytesseract.image_to_string(img, lang=lang)
            return text.strip()
    except IOError as e:
        messagebox.showerror("Error", f"Error opening image file: {e}")
        return None
    except TesseractError as e:
        messagebox.showerror("Error", f"Tesseract error: {e}")
        return None
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")
        return None

def process_images_in_directory(directory, lang='eng'):
    results = {}
    supported_formats = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')

    try:
        for filename in os.listdir(directory):
            if filename.lower().endswith(supported_formats):
                file_path = os.path.join(directory, filename)
                text = extract_text_from_image(file_path, lang)
                if text:
                    results[filename] = text
                else:
                    messagebox.showinfo("Info", f"No text extracted from {filename}")
    except FileNotFoundError:
        messagebox.showerror("Error", f"Directory not found: {directory}")
    except PermissionError:
        messagebox.showerror("Error", f"Permission denied to access directory: {directory}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred while processing directory: {e}")

    return results

class ImageTextExtractorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Image Text Extractor")
        master.geometry("500x350")

        self.is_dark_mode = tk.BooleanVar(value=False)

        self.create_widgets()
        self.apply_theme()

    def create_widgets(self):
        self.label_dir = ttk.Label(self.master, text="Select Directory Containing Images:")
        self.label_dir.pack(pady=5)

        self.dir_frame = ttk.Frame(self.master)
        self.dir_frame.pack(fill=tk.X, padx=5)

        self.entry_dir = ttk.Entry(self.dir_frame)
        self.entry_dir.pack(side=tk.LEFT, expand=True, fill=tk.X)

        self.btn_browse = ttk.Button(self.dir_frame, text="Browse", command=self.browse_directory)
        self.btn_browse.pack(side=tk.RIGHT)

        self.label_lang = ttk.Label(self.master, text="Enter Language Code(s) (e.g., eng, fra, eng+fra):")
        self.label_lang.pack(pady=5)

        self.entry_lang = ttk.Entry(self.master)
        self.entry_lang.insert(0, "eng")
        self.entry_lang.pack(fill=tk.X, padx=5)

        self.btn_extract = ttk.Button(self.master, text="Extract Text", command=self.extract_text)
        self.btn_extract.pack(pady=10)

        self.text_result = scrolledtext.ScrolledText(self.master, height=10)
        self.text_result.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.theme_switch = ttk.Checkbutton(
            self.master,
            text="Dark Mode",
            variable=self.is_dark_mode,
            command=self.toggle_theme,
            style="Switch.TCheckbutton"
        )
        self.theme_switch.pack(pady=5)

    def apply_theme(self):
        if self.is_dark_mode.get():
            self.master.configure(bg="#2b2b2b")
            style = ttk.Style()
            style.theme_use("clam")
            style.configure("TLabel", foreground="white", background="#2b2b2b")
            style.configure("TButton", foreground="white", background="#3c3f41")
            style.configure("TEntry", fieldbackground="#3c3f41", foreground="white")
            style.configure("TFrame", background="#2b2b2b")
            style.configure("Switch.TCheckbutton", foreground="white", background="#2b2b2b")
            self.text_result.config(bg="#3c3f41", fg="white")
        else:
            self.master.configure(bg="SystemButtonFace")
            style = ttk.Style()
            style.theme_use("clam")
            style.configure("TLabel", foreground="black", background="SystemButtonFace")
            style.configure("TButton", foreground="black", background="SystemButtonFace")
            style.configure("TEntry", fieldbackground="white", foreground="black")
            style.configure("TFrame", background="SystemButtonFace")
            style.configure("Switch.TCheckbutton", foreground="black", background="SystemButtonFace")
            self.text_result.config(bg="white", fg="black")

    def toggle_theme(self):
        self.apply_theme()

    def browse_directory(self):
        directory = filedialog.askdirectory()
        self.entry_dir.delete(0, tk.END)
        self.entry_dir.insert(0, directory)

    def extract_text(self):
        directory = self.entry_dir.get()
        lang = self.entry_lang.get()
        if not directory:
            messagebox.showerror("Error", "Please select a directory.")
            return

        results = process_images_in_directory(directory, lang)
        self.text_result.delete('1.0', tk.END)
        if results:
            for filename, text in results.items():
                self.text_result.insert(tk.END, f"Filename: {filename}\n\nExtracted text:\n{text}\n\n{'='*50}\n\n")
        else:
            self.text_result.insert(tk.END, "No text was extracted from any images in the specified directory.")

def main():
    if not check_tesseract_installed():
        messagebox.showerror("Error", "Tesseract is not installed or not in the system PATH.")
        sys.exit(1)

    root = tk.Tk()
    ImageTextExtractorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()