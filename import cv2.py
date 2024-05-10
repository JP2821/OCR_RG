import cv2
import numpy as np
import pytesseract
from PIL import Image, ImageEnhance
import tempfile

# Função para extrair texto da imagem do RG
def extract_text_from_rg(image_path):
    # Carregar a imagem
    image = cv2.imread(image_path)

    # Converter a imagem para escala de cinza
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Binarizar a imagem usando thresholding
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Encontrar contornos na imagem binarizada
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Encontrar o maior contorno (presumindo que seja o retângulo preto que circunda o RG)
    largest_contour = max(contours, key=cv2.contourArea)

    # Criar uma máscara preta do mesmo tamanho que a imagem
    mask = np.zeros_like(gray)

    # Desenhar o contorno preenchido com branco na máscara
    cv2.drawContours(mask, [largest_contour], -1, (255, 255, 255), thickness=cv2.FILLED)

    # Aplicar a máscara na imagem original para obter apenas a região do retângulo preto
    cropped_image = cv2.bitwise_and(image, image, mask=mask)

    # Converter para escala de cinza
    cropped_gray = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)

    # Criar um arquivo temporário para salvar a imagem
    with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as temp_img:
        temp_img_path = temp_img.name
        # Salvar a região recortada para visualização
        cv2.imwrite(temp_img_path, cropped_gray)

    # Abrir a imagem recortada com PIL
    image_pil = Image.open(temp_img_path)

    # Rotacionar a imagem em 90 graus para a esquerda
    image_pil = image_pil.rotate(90, expand=True)

    # Converter a imagem para escala de cinza
    image_pil = image_pil.convert('L')

    # Aplicar aumento de contraste
    enhancer = ImageEnhance.Contrast(image_pil)
    image_pil = enhancer.enhance(25)

    image_pil.show()

    # Configuração do Tesseract
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

    # Extrair texto da imagem
    extracted_text = pytesseract.image_to_string(image_pil, lang='por')

    # Dividir o texto extraído em linhas
    lines = extracted_text.split('\n')

    # Iterar sobre cada linha para remover os caracteres '<' e '>'
    for i, line in enumerate(lines):
        lines[i] = ''.join(filter(lambda x: not x.islower(), line.replace('<', '').replace('>', '').replace('€', '').replace('*', '').replace('“', '').replace('"', '').replace('. ', '').replace(' .', '').strip()))

    # Exibir o dicionário
    print(lines)

    # Retornar o texto extraído
    return lines

# Caminho da imagem do RG
image_path = 'RG_2.jpg'

# Extrair texto da imagem do RG
extracted_text = extract_text_from_rg(image_path)

# Exibir o texto extraído
print(extracted_text)
