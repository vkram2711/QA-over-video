import datetime
import whisper


def video_to_text(file_path):

    model = whisper.load_model('large')
    # save a timestamp before transcription
    t1 = datetime.datetime.now()
    print(f"started at {t1}")

    # do the transcription
    output = model.transcribe(file_path)
    print(output)
    # show time elapsed after transcription is complete.
    t2 = datetime.datetime.now()
    print(f"ended at {t2}")
    print(f"time elapsed: {t2 - t1}")
    segments = output['segments']

    text = ''
    for i in range(0, len(segments)):
      segment = segments[i]
      text += segment + '\n\n'

    # Specify the file path and name where you want to save the string
    file_path = "transcribed.txt"

    # Open the file in write mode ('w')
    with open(file_path, 'w') as file:
        file.write(text)

    print(f'Transcribed text saved to {file_path}')
