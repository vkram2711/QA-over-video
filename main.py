import os

import audio_utils

import whisper_utils

if __name__ == '__main__':
    os.environ['OPENAI_API_KEY'] = input('Please enter your OpenAI API key: ')
    proceed = 'YES'
    audio_url = input('Enter Video url(if you want to use the one that was loaded before just hit enter): ')
    if audio_url != '':
        audio_utils.download_audio(audio_url)
        proceed = input('Check output.audio.mp3 file for correctness if you want to continue print YES: ')
    if proceed == 'YES' and audio_url != '':
        proceed = input('Do you want to generate text file from the audio or use old one for QA, if positive type YES: ')
        if proceed == 'YES':
            print('Starting listening file, it may take long time(somewhere around the file length itself\n')
            whisper_utils.video_to_text('output_audio.mp3')
            print('Text was generated, please check it and correct any typos to increase accuracy of QA ')

    proceed = input('Hit enter when you satisfied with text file to launch QA ')
    print("\n\nStarting generating embeddings \n\n\n")
    import qa
    qa.generate_embeddings("output_text.txt")
    print("\n\nEmbeddings generated ready to answer questions \n\n\n")
    while True:
        question = input("Type in a question: ")
        print(f"Answer: {qa.answer_question(question)} \n\n")

