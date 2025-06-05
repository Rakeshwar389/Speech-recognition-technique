import speech_recognition as sr
import whisper

def recognize_with_whisper(audio_path, language="en"):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path, language=language)
    return result['text']

def recognize_with_google(audio_path, language="en-US"):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio, language=language)
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError:
        return "Google API error"
