mi_archivo = open("filename.txt", "a+")
mi_archivo.write("This has been written to a file")
mi_archivo.close()

mi_archivo = open("filename.txt","r")
print(mi_archivo.read())
mi_archivo.close()
