"""

Turn image to text. Write a story based on that text. Read the story

"""


from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
import os
import requests

IMG = "moscow.jpg"

load_dotenv(find_dotenv())

HF_TOKEN = os.getenv("HF_API_TOKEN")


# Image to text
def img2text(url):
    image_to_text = pipeline(
        "image-to-text", model="Salesforce/blip-image-captioning-large", device=1
    )
    text = image_to_text(url)[0]["generated_text"]
    return text


# Text to story
def text2story(text):
    text_to_story = pipeline("text-generation", model="gpt2", device=1)
    story = text_to_story(text, max_length=200, do_sample=True)[0]["generated_text"]
    return story


# Story to speech
# Use API this time
def story2speech(story):
    API_URL = (
        "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
    )
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    payloads = {"inputs": story}
    response = requests.post(API_URL, headers=headers, json=payloads)

    with open("audio.flac", "wb") as file:
        file.write(response.content)


text = img2text(IMG)
story = text2story(text)
print("\nText:" + text)
print("\nStory:" + story)
story2speech(story)
