from PIL import Image
import os

lista_imagens = os.listdir("imagens/")


for arquivo in lista_imagens:
	# abrir arquivo
	#imagem = Image.open("imagens/Nature-Free-PNG-Image.png").convert("RGB")
	imagem = Image.open(f"imagens/{arquivo}")

	# salvar arquivo em outro formato
	#imagem.save("Nature-Free-PNG-Image.jpg")
	imagem.save(f"tiff/{arquivo.replace('png', 'tiff')}")