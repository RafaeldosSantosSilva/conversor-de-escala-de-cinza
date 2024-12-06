import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def processar_imagem(caminho_imagem, limiar=127):
    """
    Processa uma imagem, convertendo para níveis de cinza e binarizando.
    
    Parâmetros:
    - caminho_imagem: Caminho para o arquivo de imagem
    - limiar: Valor de limiarização (padrão 127)
    
    Retorna:
    - imagem_original: Imagem original
    - imagem_cinza: Imagem em níveis de cinza
    - imagem_binaria: Imagem binarizada
    """
    # Verificar se o arquivo existe
    if not os.path.exists(caminho_imagem):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_imagem}")
    
    # Carregar imagem
    imagem_original = cv2.imread(caminho_imagem)
    
    # Verificar se a imagem foi carregada corretamente
    if imagem_original is None:
        raise ValueError(f"Não foi possível carregar a imagem: {caminho_imagem}")
    
    # Converter para RGB (OpenCV usa BGR por padrão)
    imagem_original_rgb = cv2.cvtColor(imagem_original, cv2.COLOR_BGR2RGB)
    
    # Converter para escala de cinza
    imagem_cinza = cv2.cvtColor(imagem_original, cv2.COLOR_BGR2GRAY)
    
    # Binarização usando limiarização simples
    _, imagem_binaria = cv2.threshold(imagem_cinza, limiar, 255, cv2.THRESH_BINARY)
    
    return imagem_original_rgb, imagem_cinza, imagem_binaria

def visualizar_imagens(imagem_original, imagem_cinza, imagem_binaria):
    """
    Visualiza as imagens processadas em uma única figura.
    
    Parâmetros:
    - imagem_original: Imagem original em RGB
    - imagem_cinza: Imagem em níveis de cinza
    - imagem_binaria: Imagem binarizada
    """
    # Configurar subplot
    plt.figure(figsize=(15, 5))
    
    # Imagem Original
    plt.subplot(131)
    plt.title('Imagem Original')
    plt.imshow(imagem_original)
    plt.axis('off')
    
    # Imagem em Níveis de Cinza
    plt.subplot(132)
    plt.title('Níveis de Cinza')
    plt.imshow(imagem_cinza, cmap='gray')
    plt.axis('off')
    
    # Imagem Binarizada
    plt.subplot(133)
    plt.title('Imagem Binarizada')
    plt.imshow(imagem_binaria, cmap='gray')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()

def main():
    # Solicitar caminho da imagem ao usuário
    while True:
        try:
            # Solicitar caminho completo absoluto da imagem
            caminho_imagem = input("Digite o caminho completo para a imagem: ").strip()
            
            # Solicitar valor de limiar
            while True:
                try:
                    limiar = input("Digite o valor de limiar (0-255, padrão é 127): ").strip()
                    
                    # Se o usuário não digitar nada, usa o padrão
                    if limiar == "":
                        limiar = 127
                    else:
                        limiar = int(limiar)
                    
                    # Validar o limiar
                    if 0 <= limiar <= 255:
                        break
                    else:
                        print("Erro: O limiar deve estar entre 0 e 255.")
                
                except ValueError:
                    print("Erro: Digite um número válido para o limiar.")
            
            # Processar imagem
            img_original, img_cinza, img_binaria = processar_imagem(caminho_imagem, limiar)
            
            # Visualizar imagens
            visualizar_imagens(img_original, img_cinza, img_binaria)
            
            # Perguntar se quer processar outra imagem
            continuar = input("Deseja processar outra imagem? (s/n): ").strip().lower()
            if continuar != 's':
                break
        
        except FileNotFoundError as e:
            print(e)
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"Erro inesperado: {e}")

# Executar o script
if __name__ == "__main__":
    main()