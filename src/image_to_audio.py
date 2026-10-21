import numpy as np
from PIL import Image
from scipy.io.wavfile import write

def generate_wav_file(img_path, output_path="test.wav", duracao_seg=6.0, sampling_rate=44100):
    img_pil = Image.open(img_path)
    
    samples = int(sampling_rate * duracao_seg)
    altura_freqs = 480
    
    img_resized = img_pil.resize((samples, altura_freqs), Image.Resampling.BILINEAR)
    img_matriz = np.array(img_resized, dtype=np.float64) / 255.0

    freqs = np.linspace(1000, 8000, altura_freqs)
    x = np.linspace(0, duracao_seg, samples, endpoint=False)

    np.random.seed(42)
    fases_iniciais = np.random.uniform(0, 2 * np.pi, size=(altura_freqs, 1))

    fase = 2 * np.pi * freqs[:, np.newaxis] * x + fases_iniciais
    ondas = np.sin(fase)

    y = (img_matriz * ondas).sum(axis=0)

    max_val = np.max(np.abs(y))
    if max_val > 0:
        y = y / max_val

    audio_16bit = (y * 32767).astype(np.int16)
    write(output_path, sampling_rate, audio_16bit)

    print(f"[+] Arquivo {output_path} gerado com sucesso!")

if __name__ == "__main__":
    generate_wav_file("sua_imagem.png")