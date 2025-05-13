import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import filters

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizador de Imagens com Filtros")
        
        self.original_image = None
        self.processed_image = None

        # Botões
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Carregar Imagem", command=self.load_image).grid(row=0, column=0)
        tk.Button(btn_frame, text="Escala de Cinza", command=self.apply_gray).grid(row=0, column=1)
        tk.Button(btn_frame, text="Inversão de Cores", command=self.apply_invert).grid(row=0, column=2)
        tk.Button(btn_frame, text="Aumento de Contraste", command=self.apply_contrast).grid(row=0, column=3)
        tk.Button(btn_frame, text="Desfoque", command=self.apply_blur).grid(row=0, column=4)
        tk.Button(btn_frame, text="Nitidez", command=self.apply_sharpen).grid(row=0, column=5)
        tk.Button(btn_frame, text="Detecção de Bordas", command=self.apply_edges).grid(row=0, column=6)
        tk.Button(btn_frame, text="Salvar Imagem", command=self.save_image).grid(row=0, column=7)

        # Canvas para imagens
        self.canvas = tk.Canvas(self.root, width=1000, height=500, bg="white")
        self.canvas.pack()

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[
            ("Arquivos de imagem", ("*.png", "*.jpg", "*.jpeg", "*.bmp", "*.gif")),
            ("Todos os arquivos", "*.*")
        ])
        if file_path:
            try:
                self.original_image = Image.open(file_path).convert("RGB")
                self.processed_image = self.original_image.copy()
                self.display_images()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao carregar imagem: {e}")

    def display_images(self):
        # Redimensiona imagens para caber no canvas (max 480px)
        display_original = self.original_image.resize((480, 480))
        display_processed = self.processed_image.resize((480, 480))

        self.tk_original = ImageTk.PhotoImage(display_original)
        self.tk_processed = ImageTk.PhotoImage(display_processed)

        self.canvas.delete("all")
        self.canvas.create_image(250, 250, image=self.tk_original)
        self.canvas.create_image(750, 250, image=self.tk_processed)

    def apply_filter(self, func):
        if self.processed_image:
            self.processed_image = func(self.processed_image)
            self.display_images()
        else:
            messagebox.showwarning("Aviso", "Carregue uma imagem primeiro.")

    def apply_gray(self): self.apply_filter(filters.gray_scale)
    def apply_invert(self): self.apply_filter(filters.invert_colors)
    def apply_contrast(self): self.apply_filter(filters.enhance_contrast)
    def apply_blur(self): self.apply_filter(filters.blur)
    def apply_sharpen(self): self.apply_filter(filters.sharpen)
    def apply_edges(self): self.apply_filter(filters.edge_detection)

    def save_image(self):
        if self.processed_image:
            path = filedialog.asksaveasfilename(defaultextension=".png",
                                                filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg")])
            if path:
                self.processed_image.save(path)
                messagebox.showinfo("Sucesso", "Imagem salva com sucesso!")
        else:
            messagebox.showwarning("Aviso", "Nenhuma imagem para salvar.")

    def reset_image(self):
        if self.original_image:
            self.processed_image = self.original_image.copy()
            self.display_images()
        else:
            messagebox.showwarning("Aviso", "Carregue uma imagem primeiro.")
    def close_app(self):
        if messagebox.askokcancel("Sair", "Você tem certeza que deseja sair?"):
            self.root.destroy()
        self.root.protocol("WM_DELETE_WINDOW", self.close_app)
        self.root.bind("<Control-q>", lambda _: self.close_app())
        
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageViewer(root)
    root.mainloop()
