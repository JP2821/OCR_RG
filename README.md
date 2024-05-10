# Sistema de Verificação de CPF em Documentos de Identidade

Este sistema utiliza inteligência artificial para extrair informações de documentos de identidade, converter essas informações em um formato JSON e validar o CPF presente nos documentos.

## Funcionamento do Sistema

1. **Configuração da IA:** Utiliza o serviço Google GenerativeAI para criar uma instância de um modelo de IA treinado para processamento de imagens de documentos de identidade.

2. **Caracterização do Comportamento da IA:** Define um prompt de sistema para instruir a IA sobre a tarefa a ser realizada. Em seguida, fornece uma imagem de um documento de identidade como entrada para a IA.

3. **Processamento da Imagem:** Carrega a imagem do documento de identidade e realiza uma rotação de 90 graus para a esquerda para corrigir a orientação.

4. **Interrogando o Sistema:** Define um prompt do usuário para solicitar à IA que converta os dados do RG em um formato JSON especificado. Combina o prompt do sistema, a imagem processada e o prompt do usuário em uma entrada para a IA.

5. **Geração da Resposta:** A IA gera uma resposta que contém os dados do RG no formato JSON solicitado.

6. **Validação do CPF:** Extrai o CPF do JSON gerado pela IA e verifica se é válido de acordo com as regras de validação do CPF no Brasil.

## Pré-requisitos e Configuração

- É necessário ter uma conta válida para acessar o serviço Google GenerativeAI.
- O ambiente de execução deve ter as bibliotecas `google.generativeai`, `PIL`, `markdown` e `json` instaladas.

## Como Utilizar

1. Certifique-se de que todas as bibliotecas necessárias estão instaladas.
2. Forneça uma imagem de um documento de identidade para o sistema.
3. Aguarde a resposta do sistema, que incluirá os dados do documento de identidade no formato JSON.
4. O sistema validará automaticamente o CPF presente nos dados do documento e fornecerá uma mensagem indicando se o documento é válido ou não.

---

## Features 
1. Detecção de RG na imagem para posterior centralização e garantir a integridade dos dados [...]
2. Deixar o modelo dinâmico para que o usuário apenas insira o tipo de documento e a IA se comporte para extrair os dados com máxima precisão [ ]
3. Interface UI []
4. OCR de proposito geral []
