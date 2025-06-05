import speech_recognition as sr
from datetime import datetime
import os

def transcribe_meeting(output_file="transcript.txt", duration=60):
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("🎤 Listening... Press Ctrl+C to stop.")

        start_time = datetime.now()
        try:
            with open(output_file, "a") as f:
                while True:
                    print("⌛ Listening for the next phrase...")
                    audio = recognizer.listen(source, timeout=10, phrase_time_limit=duration)
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    try:
                        text = recognizer.recognize_google(audio)
                        entry = f"[{timestamp}] {text}\n"
                        print(f"📝 {entry}")
                        f.write(entry)
                    except sr.UnknownValueError:
                        print("❌ Could not understand audio.")
                    except sr.RequestError as e:
                        print(f"❌ API error: {e}")
        except KeyboardInterrupt:
            print("\n🛑 Transcription stopped by user.")

if __name__ == "__main__":
    output_filename = "meeting_transcript.txt"
    os.makedirs("transcripts", exist_ok=True)
    transcribe_meeting(output_file=os.path.join("transcripts", output_filename))
