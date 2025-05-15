import sounddevice as sd
import numpy as np

def get_spectrum(num_bands=16, buffer_size=1024, samplerate=44100):
    """Capture audio and return magnitude values split into frequency bands."""
    # Record audio buffer
    audio_data = sd.rec(buffer_size, samplerate=samplerate, channels=1, dtype='float32')
    sd.wait()

    # Flatten to 1D array
    samples = audio_data.flatten()

    # Apply Hamming window to reduce spectral leakage (optional but improves quality)
    samples *= np.hamming(len(samples))

    # Perform FFT and get magnitude
    spectrum = np.abs(np.fft.fft(samples))
    spectrum = spectrum[:len(spectrum)//2]  # Keep only positive frequencies

    # Split into frequency bands
    band_size = len(spectrum) // num_bands
    bands = []
    for i in range(num_bands):
        start = i * band_size
        end = start + band_size
        band_value = np.mean(spectrum[start:end])
        bands.append(band_value)

    return bands
