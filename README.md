# QA-over-video
Simple Python script for answering question about video using Whisper and GPT. 

To run, download the files and install requirements using:

```pip install -r requirements.txt```

Run with:
```python main.py```

Provide the OpenAI API key and URL link for the video. Audio from the video will be saved as output_audio.mp3 and then, using Whisper, transcribed into output_text.txt. Afterwards code will generate embeddings for answering questions using GPT
