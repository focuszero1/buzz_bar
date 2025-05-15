from visualizer import run_visualizer
from audio_input import get_spectrum

def get_current_spectrum():
    return get_spectrum()

if __name__ == "__main__":
    run_visualizer(get_current_spectrum)
