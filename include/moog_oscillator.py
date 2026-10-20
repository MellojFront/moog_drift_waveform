import numpy as np
import config as cfg


def gen_moog_sawtooth():
    temp = cfg.ENVIRONMENT["room_temp_c"]
    warmup = cfg.ENVIRONMENT["synth_warmup_min"]
    sample_rate = cfg.MOOG_SETTINGS["sample_rate"]
    freq = cfg.MOOG_SETTINGS["base_freq"]
    power_noise = cfg.ENVIRONMENT["power_noise"]
    sat = cfg.MOOG_SETTINGS["ladder_saturation"]
    
    duration = 1.0 / freq
    
    drift_factor = (temp / 20.0) * (1.0 / (warmup + 1))
    
    total_samples = int(sample_rate * duration)
    
    time = np.linspace(0, duration, total_samples, endpoint=False)
    
    #ideal_phase = 2 * np.pi * freq * time
    ideal_phase = 2 * np.pi * freq * time
    
    analog_phase_drift = np.sin(2 * np.pi * 5 * time) * (drift_factor * 0.1)
    
    if power_noise:
        rng = np.random.default_rng(42)
        jitter = rng.uniform(-0.02, 0.02, size=total_samples) * drift_factor
        analog_phase_drift += jitter
        
        
    real_phase = ideal_phase + analog_phase_drift

    raw_saw = 2.0 * (real_phase / (2 * np.pi) - np.floor(real_phase / (2 * np.pi) + 0.5))
    
    moog_wave = np.tanh(-raw_saw * sat)
    
    moog_wave = moog_wave / np.max(np.abs(moog_wave))

    
    return time, moog_wave