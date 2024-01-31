from utils.generation import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from IPython.display import Audio

# download and load all models
preload_models()

# generate audio from text
text_prompt = """
これ新しい読み上げAIだよ
"""
audio_array = generate_audio(text_prompt)

# save audio to disk
write_wav("test.wav", SAMPLE_RATE, audio_array)