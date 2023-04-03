import openai

API_KEY = "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"
openai.api_key = API_KEY

f = open("test.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", f)
print(transcript["text"])