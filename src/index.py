import webcam_functions, normalize_image_function, image_to_audio

def show_banner():
    print("Imagem para Espectograma - IMESEC")

show_banner()

img_path = webcam_functions.capture_image()
normalize_image_function.normalize_image(img_path)
image_to_audio.generate_wav_file(img_path)
