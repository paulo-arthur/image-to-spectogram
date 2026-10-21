# img2spec

CLI em Python que converte imagens em arquivos de áudio `.wav` onde a imagem original é revelada ao abrir o áudio em um analisador de espectro (como Audacity ou Sonic Visualiser).

Desenvolvido para ser usado como desafio visual de esteganografia/CTF no estande do **IMESEC** durante a Semana de Ciência e Tecnologia.

---

## Como funciona

O script faz a síntese aditiva de frequências senoidais com base nos pixels da imagem:

1. **Eixo Y (Frequência):** As 480 linhas da imagem são mapeadas linearmente na faixa de 1000 Hz (grave) a 8000 Hz (agudo).
2. **Eixo X (Tempo):** A imagem é redimensionada via interpolação bilinear ao longo do tempo total de áudio (padrão de 6 segundos em 44.1 kHz).
3. **Desincronização de Fase:** Aplica fases iniciais aleatórias ($\phi \in [0, 2\pi)$) para cada frequência, eliminando o batimento de fase (interferência construtiva) que gera artefatos de linhas verticais no espectrograma.
4. **Amplitude:** O brilho do pixel ($0.0$ a $1.0$) controla o volume da frequência naquele exato instante.

---

## Pré-requisitos

- Python 3.8+
- `numpy`
- `Pillow`
- `scipy`

Instalação das dependências:

```bash
pip install numpy pillow scipy