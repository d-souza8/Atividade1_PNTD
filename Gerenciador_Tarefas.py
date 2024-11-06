import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage


# Função para adicionar tarefa
def adicionar_tarefa():
    tarefa = entrada_tarefa.get()
    if tarefa:
        # Insere a nova tarefa na área de texto e pula uma linha
        lista_tarefas.insert(tk.END, tarefa)
        entrada_tarefa.delete(0, tk.END)  # Limpa a entrada
    else:
        messagebox.showwarning("Aviso", "A tarefa não pode estar vazia!")

# Função para remover tarefa
def remover_tarefa():
    try:
        # Obtém o índice da tarefa selecionada
        indice_selecionado = lista_tarefas.curselection()[0]
        lista_tarefas.delete(indice_selecionado)  # Remove a tarefa da lista
    except IndexError:
        messagebox.showwarning("Aviso", "Selecione uma tarefa para remover!")

# Função para concluir tarefa (marcar com risco no meio)
def concluir_tarefa():
    try:
        # Obtém o índice da tarefa selecionada
        indice_selecionado = lista_tarefas.curselection()[0]
        tarefa = lista_tarefas.get(indice_selecionado)
        
        # Aplica o efeito de risco se ainda não estiver concluída
        if not tarefa.startswith("✔"):  # Verifica se já está marcada como concluída
            tarefa_concluida = "✔" + tarefa
            lista_tarefas.delete(indice_selecionado)
            lista_tarefas.insert(indice_selecionado, tarefa_concluida)
    except IndexError:
        messagebox.showwarning("Aviso", "Selecione uma tarefa para marcar como concluída!")

# Configura a janela principal
janela = tk.Tk()
janela.title("Gerenciador de Tarefas")

janela.geometry("400x500")
imagem_fundo = PhotoImage(file="fundo_escuro.png")
label_fundo = tk.Label(janela, image=imagem_fundo)
label_fundo.place(x=0,y=0, relwidth=1, relheight=1)

# Entrada para nova tarefa
entrada_tarefa = tk.Entry(janela, width=50)
entrada_tarefa.pack(pady=20)
entrada_tarefa.configure(bg="lightgrey")

# Botão para adicionar tarefa
botao_adicionar = tk.Button(janela, text="➕ Adicionar Tarefa", command=adicionar_tarefa)
botao_adicionar.pack(pady=10)
botao_adicionar.configure(bg="blue")

# Lista de tarefas
lista_tarefas = tk.Listbox(janela, width=50, height=20, selectmode=tk.SINGLE)
lista_tarefas.pack(pady=10)
lista_tarefas.configure(bg="lightgrey")

# Botões para concluir
botao_concluir = tk.Button(janela, text="✅ Concluir Tarefa", command=concluir_tarefa)
botao_concluir.pack(side=tk.LEFT, padx=10, pady=5)
botao_concluir.configure(bg="green")

#Botão para remover tarefas
botao_remover = tk.Button(janela, text="⛔ Remover Tarefa", command=remover_tarefa)
botao_remover.pack(side=tk.RIGHT, padx=10, pady=5)
botao_remover.configure(bg="red")

# Inicia a interface
janela.mainloop()
