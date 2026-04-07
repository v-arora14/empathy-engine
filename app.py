import pyttsx3
from textblob import TextBlob

def detect_emotion(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0.2:
        return "happy", polarity
    elif polarity < -0.2:
        return "sad", polarity
    else:
        return "neutral", polarity

def set_voice_properties(engine, emotion, intensity):
    if emotion == "happy":
        engine.setProperty('rate', 180 + int(intensity * 50))
        engine.setProperty('volume', 1.0)

    elif emotion == "sad":
        engine.setProperty('rate', 120 + int(intensity * 30))
        engine.setProperty('volume', 0.6)

    else:
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 0.8)

def text_to_speech(text, emotion, intensity):
    engine = pyttsx3.init()

    set_voice_properties(engine, emotion, intensity)

    output_file = "output.wav"
    engine.save_to_file(text, output_file)
    engine.runAndWait()

    return output_file

def main():
    text = input("Enter your text: ")

    emotion, intensity = detect_emotion(text)

    print("Detected Emotion:", emotion)
    print("Intensity:", round(intensity, 2))

    file = text_to_speech(text, emotion, abs(intensity))

    print("Audio saved as:", file)

if __name__ == "__main__":
    main()