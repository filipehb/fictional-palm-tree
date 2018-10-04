#Tesseract Exec
pytesseract.pytesseract.tesseract_cmd = ''

from PIL import Image
import pytesseract as pyt
import cv2
import os

if __name__ == "__main__":
    
    #carrega a imagem colorida
    imagem = cv2.imread("texto.png")
    
    #salva a imagem em um arquivo temporário do Windows para aplicar OCR
    filenameImagem = "{}.png".format(os.getpid())
    cv2.imwrite(filenameImagem, imagem)
    
    #carrega a imagem usando a biblioteca PIL/Pillow e aplica OCR
    texto = pyt.image_to_string(Image.open(filenameImagem))

    #deleta arquivo temporário
    os.remove(filenameImagem)
    
    print("Texto: " + texto)