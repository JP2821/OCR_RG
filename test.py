import google.generativeai as gemini
from PIL import Image, ImageEnhance
import markdown
import json

def validationCpf(cpf):
  # Remover caracteres não numéricos
  cpf = ''.join(filter(str.isdigit, cpf))

  # Verificar se o CPF tem 11 dígitos
  if len(cpf) != 11:
      return False

  # Calcular o primeiro dígito verificador
  soma = 0
  for i in range(9):
      soma += int(cpf[i]) * (10 - i)
  digito1 = 11 - (soma % 11)
  if digito1 > 9:
      digito1 = 0

  # Verificar o primeiro dígito verificador
  if int(cpf[9]) != digito1:
      return False

  # Calcular o segundo dígito verificador
  soma = 0
  for i in range(10):
      soma += int(cpf[i]) * (11 - i)
  digito2 = 11 - (soma % 11)
  if digito2 > 9:
      digito2 = 0

  # Verificar o segundo dígito verificador
  if int(cpf[10]) != digito2:
      return False

  # Se passou por todas as verificações, o CPF é válido
  return True   

gemini.configure(api_key='AIzaSyD29yMiwFi_8JJKFnJGCgRGneCP2y50WRg')

MODEL_CONFIG = {
    "temperature": 0.2,
    "top_p": 1,
    "top_k": 32,
    "max_output_tokens": 4096
}

model = gemini.GenerativeModel('gemini-pro-vision',generation_config=MODEL_CONFIG)

# parte do sistema responsavel por caracterizar o comportamento da IA
system_prompt = "Você é um especialista em compreender RGs. Imagens de entrada na forma de RGs serão fornecidos a você, sua tarefa é responder a perguntas com base no conteúdo da imagem de entrada"

# Carregar a imagem
image = Image.open('RG_4.jpg')

# Rotacionar a imagem em 90 graus para a esquerda
image_pil = image.rotate(90, expand=True)

#Pergunta ao sistema, em breve deixar dinamico, como entrada do usuário
user_prompt = "Converta os dados do RG em formato json com tags json na seguinte configuração: {nome:, filiacao: {pai: ,mae: },naturalidade:,data_nascimento: ,rg: ,data_expedicao:,cpf:,municipio_nascimento:,cartorio:}, conforme necessário para os dados na imagem"

input_prompt = [system_prompt,image_pil,user_prompt]

response = model.generate_content(input_prompt)

print(response.text)

pre_process_response = response.text

pre_process_response = pre_process_response.strip()

pre_process_response =pre_process_response.replace('```json', '').replace('```', '')

json_data = json.loads(pre_process_response)

result = validationCpf(json_data['cpf'])
 
if result:
    print(f'CPF válido, segue as informações do documento: {json_data}')
else:
    print('Documento inválido, por favor insira um documento cujo o CPF seja válido!')
