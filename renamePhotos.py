import os

def renomear_fotos(caminho_pasta="images"):
    """
    Renomeia todas as fotos em uma pasta para um formato sequencial (foto01.jpeg, foto02.jpeg, ...).

    Args:
        caminho_pasta (str): O nome da pasta que contém as imagens.
    """
    # Verifica se a pasta existe
    if not os.path.isdir(caminho_pasta):
        print(f"Erro: A pasta '{caminho_pasta}' não foi encontrada.")
        return

    # Lista todos os arquivos na pasta
    try:
        arquivos = os.listdir(caminho_pasta)
    except OSError as e:
        print(f"Erro ao acessar a pasta: {e}")
        return

    # Filtra apenas por arquivos de imagem comuns
    extensoes_imagem = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')
    imagens = [arquivo for arquivo in arquivos if arquivo.lower().endswith(extensoes_imagem)]

    # Ordena os arquivos para uma nomeação consistente
    imagens.sort()

    contador = 1
    for nome_antigo in imagens:
        # Define o novo nome do arquivo com zero à esquerda para números menores que 10
        novo_nome = f"foto{contador:02d}.jpeg"

        # Cria o caminho completo para o arquivo antigo e o novo
        caminho_antigo = os.path.join(caminho_pasta, nome_antigo)
        caminho_novo = os.path.join(caminho_pasta, novo_nome)

        # Renomeia o arquivo
        try:
            os.rename(caminho_antigo, caminho_novo)
            print(f"Renomeado: '{nome_antigo}' para '{novo_nome}'")
            contador += 1
        except OSError as e:
            print(f"Erro ao renomear o arquivo {nome_antigo}: {e}")


if __name__ == "__main__":
    renomear_fotos()