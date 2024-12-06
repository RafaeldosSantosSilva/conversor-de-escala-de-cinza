
# Processador de Imagens - Conversão para Níveis de Cinza e Binarização

## 📜 Descrição do Projeto
Este script em Python é uma ferramenta simples e eficiente para processar imagens, realizando as seguintes transformações principais:

- **Conversão de imagem colorida para níveis de cinza.**
- **Binarização da imagem** (transformação para preto e branco com base em um valor de limiar configurável).

Ideal para quem busca um ponto de partida em processamento de imagens.

---

## 🚀 Funcionalidades
- **Carregamento de imagem:** Forneça o caminho completo do arquivo.
- **Conversão para escala de cinza:** Transforme imagens coloridas para tons de cinza.
- **Binarização configurável:** Defina o limiar para separar preto e branco.
- **Visualização lado a lado:** Compare a imagem original e as processadas.
- **Processamento iterativo:** Possibilidade de processar múltiplas imagens sem reiniciar o script.
- **Tratamento de erros:** Lida com entradas inválidas e outros problemas comuns.

---

## 🛠️ Requisitos
- **Python 3.7** ou superior.
- Bibliotecas necessárias:
  - [`opencv-python`](https://pypi.org/project/opencv-python/)
  - [`numpy`](https://pypi.org/project/numpy/)
  - [`matplotlib`](https://pypi.org/project/matplotlib/)

---

## 📦 Instalação


### 1. Configure um ambiente virtual (opcional, mas recomendado)
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 2. Instale as dependências
```bash
pip install opencv-python numpy matplotlib
```

---

## ▶️ Uso
Para executar o script, basta rodar o seguinte comando e seguir as instruções no terminal:

```bash
python main.py
```

### 📥 Exemplo de Entrada:
- **Caminho da imagem:** `C:\Users\SeuNome\Imagens\foto.jpg`
- **Valor do limiar (threshold):** `127` (valor padrão) ou qualquer valor entre `0 e 255`.

---

## 🔍 Como Funciona
1. O script solicita o caminho completo do arquivo da imagem.
2. Permite configurar um valor de limiar para a binarização.
3. Processa a imagem:
   - Converte para tons de cinza.
   - Aplica binarização com base no limiar fornecido.
4. Exibe as imagens:
   - Original.
   - Convertida para escala de cinza.
   - Binarizada.
5. Pergunta ao usuário se deseja processar outra imagem.

---

## 🎨 Personalização
- Ajuste o **valor do limiar** para obter diferentes níveis de contraste na binarização.
- Modifique o script para incluir outras transformações, como filtros ou detecção de bordas.

---

## ⚠️ Possíveis Erros e Soluções
- **Caminho inválido:** Certifique-se de que o caminho da imagem está correto.
- **Formato não suportado:** Verifique se a imagem é compatível com o OpenCV.
- **Valor do limiar inválido:** O limiar deve ser um número entre `0 e 255`.

---

## 🛠️ Próximos Passos
- Implementar suporte para múltiplos métodos de binarização (como Otsu e adaptativo).
- Adicionar funcionalidade de processamento em lote para várias imagens de uma vez.
- Criar uma interface gráfica amigável.

---

## 🤝 Contribuições
Contribuições são bem-vindas! Para colaborar:
1. Abra um *issue* para sugerir melhorias ou relatar problemas.
2. Envie um *pull request* com suas alterações.


---

## 🏆 Agradecimentos
- Biblioteca **OpenCV** - processamento de imagens eficiente.  
- **Matplotlib** - visualização de gráficos e imagens.  
- Comunidade **Python** - inspiração e suporte contínuos.
