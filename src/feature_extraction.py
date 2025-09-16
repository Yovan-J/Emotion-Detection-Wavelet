import numpy as np
from scipy.signal import butter, filtfilt, find_peaks

def extract_gsr_features(gsr_signal, sampling_rate=4):
    """
    Extracts features from a GSR signal after decomposing it into tonic and phasic components.

    Args:
        gsr_signal (np.array): The denoised GSR signal.
        sampling_rate (int): The sampling rate of the signal.

    Returns:
        dict: A dictionary of extracted features.
    """
    # Design a low-pass Butterworth filter to get the tonic component.
    # A cutoff frequency of 0.5 Hz is common for separating tonic from phasic.
    nyquist = 0.5 * sampling_rate
    cutoff = 0.5 / nyquist
    b, a = butter(2, cutoff, btype='low', analog=False)
    
    # Filter the signal to get the slow-moving tonic component
    tonic_signal = filtfilt(b, a, gsr_signal)
    
    # The phasic signal is the original signal minus the tonic component
    phasic_signal = gsr_signal - tonic_signal

    # Find peaks in the phasic signal. These are the Skin Conductance Responses (SCRs).
    # A minimum height and distance can be used to avoid detecting noise as peaks.
    peaks, properties = find_peaks(phasic_signal, height=0.01, distance=sampling_rate)

    features = {
        'scr_count': len(peaks),
        'mean_scr_amplitude': np.mean(properties['peak_heights']) if len(peaks) > 0 else 0,
        'gsr_mean': np.mean(gsr_signal),
        'gsr_std': np.std(gsr_signal),
        'gsr_range': np.max(gsr_signal) - np.min(gsr_signal)
    }
    
    return features

def extract_hrv_features(bvp_signal, sampling_rate=64):
    """
    Extracts time-domain Heart Rate Variability (HRV) features from a BVP signal.

    Args:
        bvp_signal (np.array): The denoised BVP signal.
        sampling_rate (int): The sampling rate of the signal.

    Returns:
        dict: A dictionary of extracted HRV features.
    """
    # Find peaks (heartbeats) in the BVP signal
    peaks, _ = find_peaks(bvp_signal, distance=sampling_rate*0.5, height=np.mean(bvp_signal))
    
    # We need at least 3 peaks to calculate all features
    if len(peaks) < 3:
        return {
            'mean_hr': 0, 'rmssd': 0, 'sdnn': 0, 'pnn50': 0
        }

    # Calculate RR intervals in milliseconds (ms)
    rr_intervals = np.diff(peaks) * (1000 / sampling_rate)
    
    # Calculate differences between successive RR intervals
    diff_rr = np.diff(rr_intervals)

    features = {
        'mean_hr': 60000 / np.mean(rr_intervals),
        'rmssd': np.sqrt(np.mean(diff_rr**2)),
        'sdnn': np.std(rr_intervals),
        'pnn50': (np.sum(np.abs(diff_rr) > 50) / len(diff_rr)) * 100 if len(diff_rr) > 0 else 0
    }
    
    return features