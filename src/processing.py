import numpy as np
import pywt
from scipy.signal import find_peaks

def wavelet_denoise(signal, wavelet='sym8', level=1):
    """
    Performs wavelet denoising on a 1D signal.
    """
    # --- FIX 1: Handle short signals ---
    # If the signal is too short for decomposition, return it as is.
    if len(signal) < 2:
        return signal

    # Decompose to get the wavelet coefficients
    coeff = pywt.wavedec(signal, wavelet, mode="per")
    
    # Calculate a universal threshold
    sigma = np.median(np.abs(coeff[-level])) / 0.6745
    threshold = sigma * np.sqrt(2 * np.log(len(signal)))
    
    # Threshold the detail coefficients
    new_coeff = [coeff[0]] + [pywt.threshold(c, value=threshold, mode='soft') for c in coeff[1:]]
        
    # Reconstruct the signal
    return pywt.waverec(new_coeff, wavelet, mode="per")

def extract_rmssd_from_bvp(bvp_signal, sampling_rate=64):
    """
    Finds peaks in a BVP signal and calculates the RMSSD HRV feature.
    """
    # Find peaks in the BVP signal to calculate RR intervals
    peaks, _ = find_peaks(bvp_signal, distance=sampling_rate*0.5, height=np.mean(bvp_signal))
    
    # --- FIX 2: More robust check for RMSSD calculation ---
    # Need at least 2 RR intervals to calculate the difference between them.
    # This requires at least 3 detected peaks.
    if len(peaks) < 3:
        return 0.0

    # Calculate RR intervals in milliseconds
    rr_intervals = np.diff(peaks) * (1000 / sampling_rate)
    
    # Calculate RMSSD
    diff_rr = np.diff(rr_intervals)
    rmssd = np.sqrt(np.mean(diff_rr**2))
    
    return rmssd