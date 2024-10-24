# Importação da biblioteca tkinter.
import tkinter as tk

# Importação da função de caixa de mensagem.
from tkinter import messagebox

# Função definida quando o botão for clicado.
def mostrar_mensagem():
    messagebox.showinfo("Informação!","Botão Clicado!")

# Criação da janela principal com título.
janela = tk.Tk()
janela.title("Interface gráfica com imagens")

# Definição do tamanho da janela principal.
janela.geometry("800x400")

# Carga de imagem da janela principal (GIF ou PNG).
imagem_logo = tk.PhotoImage(file="img_android.png")

# Criação do rótulo (Label) com a imagem.
rotulo_imagem = tk.Label(janela, image=imagem_logo)

# O método pack() posiciona o rótulo na janela, com padding (espaçamento) vertical de 20px.
rotulo_imagem.pack(pady=20)

# Criação de rótulo (Label) com texto
rotulo_texto = tk.Label(janela, text="Bem-vindo! Essa é uma interface gráfica com imagens.")

# O método pack() posiciona o rótulo na janela, com padding (espaçamento) vertical de 10px.
rotulo_texto.pack(pady=10)

# Carga da imagem do botão.
imagem_botao = tk.PhotoImage(file="img_click3.png")

# Cria um botão e associa a função mostrar_mmensagem à ação de clique no botão.
botao = tk.Button(janela, image=imagem_botao,command=mostrar_mensagem)

# O método pack() posiciona o botão na janela, com padding (espaçamento) vertical de 20px.
botao.pack(pady=20)

# Exibe e mantém a janela aberta até o usuário fechá-la.
janela.mainloop()