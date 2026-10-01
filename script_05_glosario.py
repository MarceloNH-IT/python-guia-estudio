print("--- Sistema de Consulta de Dominios ---")

# 1. MANEJO DE EXCEPCIONES (try / except / finally)
try:
    # Intentamos abrir un archivo en modo lectura ("r") que quizás no exista todavía
    with open(nombre_archivo, "r") as archivo:
        contenido = archivo.read()
        print("\nDominios registrados actualmente:")
        print(contenido)
        
except FileNotFoundError:
    # Si ocurre el error "FileNotFoundError" (el archivo no existe), lo capturamos aquí
    print(f"\n[!] Error: El archivo '{nombre_archivo}' no existe en el sistema.")
    print("[*] Creando un nuevo archivo de registro...")
    
    # 2. MANEJO DE ARCHIVOS (Modo escritura "w")
    # El bloque 'with' se encarga de aplicar close() automáticamente al terminar
    with open(nombre_archivo, "w") as archivo:
        archivo.write("AB123CD\n")
        archivo.write("EF456GH\n")
        archivo.write("KSD845\n")
        
    print("[+] Archivo creado y dominios de prueba guardados con éxito.")
    
finally:
    # Esto se ejecuta SIEMPRE, haya ocurrido un error o no
    print("\n--- Operación de lectura/escritura finalizada ---")
