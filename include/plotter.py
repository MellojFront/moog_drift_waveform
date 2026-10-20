import matplotlib.pyplot as mplt
import moog_oscillator as osc

def oscilloscope():
    time, wave = osc.gen_moog_sawtooth()
    
    mplt.figure(figsize=(12, 6))
    mplt.plot(time * 1000, wave, label='Moog Analog Waveform', color='#00F0FF', linewidth=2)
    mplt.title('Moog Osc Analysis (ADS)', fontsize=14, color='white')
    mplt.xlabel('Time(ms)', color='gray')
    mplt.ylabel('Amp', color='gray')
    mplt.grid(True, color='#333333', linestyle=':')
    mplt.legend(facecolor='#222222', edgecolor='none', labelcolor='white')
    
    mplt.gcf().set_facecolor('#111111')
    mplt.gca().set_facecolor('#181818')
    mplt.gca().tick_params(colors='gray')
    
    mplt.show()
    
if __name__ == "__main__":
    oscilloscope()