# 🚀 Automação de Cadastro de Informações com PyAutoGUI

Este projeto é um script em Python que **automação** o processo de login em um site e o **cadastro de informações** utilizando a biblioteca **PyAutoGUI**. O script lê dados de um arquivo CSV e os insere em campos específicos na interface do usuário.

## 📋 Requisitos

Antes de executar o script, verifique se você tem as seguintes bibliotecas instaladas:

```bash
- pyautogui
- pandas
- opencv-python (para suporte à função `locateOnScreen` com confiança)
```

Você pode instalar as bibliotecas necessárias usando pip:

- `pip install pyautogui pandas opencv-python`

## 🔍 Estrutura do Código
O script realiza as seguintes etapas:

- Acessar o Site:

O script abre o Google Chrome e navega até a URL especificada.

- Login:

Localiza o botão de login na tela e insere as credenciais do usuário (nome de usuário e senha).

- Cadastro de Informações:

Lê os dados de um arquivo CSV (produtos.csv) e preenche os campos do formulário com os dados.
## ⚙️ Como Usar
Prepare seu Ambiente:

  - Certifique-se de que o Chrome esteja instalado e acessível pelo sistema.
  - Coloque os arquivos de imagem (botaoEmail.png e primeiro_item.png) na pasta correta e certifique-se de que eles correspondam aos elementos na interface do usuário.
  - Crie um arquivo CSV chamado produtos.csv com as seguintes colunas:
    - codigo, marca, tipo, categoria, preco_unitario, custo, obs
  - Execute o script em um ambiente Python onde as bibliotecas necessárias estão instaladas.

## 📝 Observações
As coordenadas dos elementos a serem clicados são definidas pelas imagens. Se os elementos na tela mudarem, pode ser necessário atualizar as imagens.
O valor de confidence nas funções locateOnScreen pode ser ajustado conforme necessário. Valores mais altos significam maior precisão na detecção de imagens.
Certifique-se de que a janela do Chrome esteja visível e que os elementos estejam carregados antes de executar o script.
