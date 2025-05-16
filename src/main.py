from visualizer import run_visualizer
from osc_input import start_osc_server, get_osc_spectrum

if __name__ == "__main__":
    start_osc_server()
    run_visualizer(get_osc_spectrum)
