## Overview
Turn image to text. Write a story based on that text. Read the story

## Functionality
+ Load local .jpg image
+ Generate text description of the image with [Salesforce/blip-image-captioning-large](https://huggingface.co/Salesforce/blip-image-captioning-large) model based HuggingFace pipeline
+ Generate more text (a story) based on the image description using [GPT2](https://huggingface.co/gpt2) model based HuggingFace pipeline
+ Convert story to .flac audio file with HuggingFace Inference API for [kan-bayashi_ljspeech_vits](https://huggingface.co/espnet/kan-bayashi_ljspeech_vits) model
