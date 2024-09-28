
# Voice Recognization Assistant

Inspired by Google Home and Amazon Alexa, the goal of this project was to create a more user-customizable voice assistant that could more accurately simulate a music player in terms of playing a song given by users, storing favorites in a playlist, and having the ability to play songs randomly from a playlist or in order.

## Program Explanation

#### Speech-to-Text

To convert users' voices into text, the `speech_recognition` library was utilized. The program selects the microphone and listens for audio input, attempting to transcribe the captured audio into text using Google’s speech recognition service. If an error occurs during the conversion process, the program indicates that an error has taken place.

#### Text-to-Speech

In order for the program to respond to user commands, a text-to-speech model was set up using IBM Watson's Text to Speech library. Note: The API key for this must be set up on their website. The function retrieves the program's reply and converts it into a .wav file using a text-to-speech synthesizer, which vocalizes the program's response. The file is then played for the user and subsequently deleted.

#### Components of NLP ChatBot

Transformers library offers pre-trained models for a variety of natural language processing tasks. In this instance, it utilizes the DialoGPT model, which is specifically designed for generating conversational responses.
The chatbot operates in a continuous loop, where it listens for user input, processes that input, and generates a response. Specifically, the program utilizes the DialoGPT-medium model, which is fine-tuned for generating dialogue and can produce coherent responses based on user interactions. The recognized text is encapsulated in a Conversation object, which is subsequently passed to the NLP pipeline. The model processes the input and generates a response, which is then extracted from the model's output and refined to retain only the relevant text.




