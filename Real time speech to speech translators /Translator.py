import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
import tempfile
import playsound

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Speak now...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"📝 Recognized: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand audio.")
    except sr.RequestError:
        print("❌ Could not request results from Google Speech Recognition.")
    return None

def translate_text(text, dest_lang="es"):
    translator = Translator()
    try:
        translated = translator.translate(text, dest=dest_lang)
        print(f"🌍 Translated: {translated.text}")
        return translated.text
    except Exception as e:
        print(f"❌ Translation failed: {e}")
        return None

def speak_text(text, lang="es"):
    try:
        tts = gTTS(text=text, lang=lang)
        with tempfile.NamedTemporaryFile(delete=True, suffix=".mp3") as fp:
            tts.save(fp.name)
            playsound.playsound(fp.name)
    except Exception as e:
        print(f"❌ Speech synthesis failed: {e}")

def main():
    print("🔁 Real-Time Speech Translator (CTRL+C to exit)")
    target_lang = "es"  # Change to your preferred language code (e.g., "fr", "de")
    
    while True:
        original = recognize_speech()
        if original:
            translated = translate_text(original, dest_lang=target_lang)
            if translated:
                speak_text(translated, lang=target_lang)

if __name__ == "__main__":
    main()
