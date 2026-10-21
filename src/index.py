import webcam_functions, normalize_image_function, image_to_audio

def show_banner():
    print("\033[32m" + """
    ██╗███╗   ███╗███████╗███████╗███████╗ ██████╗
    ██║████╗ ████║██╔════╝██╔════╝██╔════╝██╔════╝
    ██║██╔████╔██║█████╗  ███████╗█████╗  ██║     
    ██║██║╚██╔╝██║██╔══╝  ╚════██║██╔══╝  ██║     
    ██║██║ ╚═╝ ██║███████╗███████║███████╗╚██████╗
    ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝\n
    Imagem para Espectograma - IMESEC                                   
    \033[0m""")
    print("Pressione ENTER para tirar a foto")
    input()

show_banner()

img_path = webcam_functions.capture_image()
normalize_image_function.normalize_image(img_path)
image_to_audio.generate_wav_file(img_path)
