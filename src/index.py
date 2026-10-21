import webcam_functions, normalize_image_function

def show_banner():
    print("Imagem para Espectograma - IMESEC")

show_banner()

normalize_image_function.normalize_image(webcam_functions.capture_image())