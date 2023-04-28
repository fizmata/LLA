# LLA

Setup info can be found in `./Instructions.md`
## Language Learning Assistant project for Computer Programming (LTAT.03.001)

### initial description

Libraries: wit.ai, Python-sounddevice, tkinter or pysimplegui

Description: The idea is to develop a language learning assistant that helps users practice speaking and listening skills in a foreign language. The application should allow users to record their voice, transcribe the audio using wit.ai, and compare the transcription with a correct answer. Users can track their progress and receive feedback on their pronunciation and fluency.

Goal: I personally use Duolingo for practising new languages, however, Duolingo does not have the option to record your voice and get feedback on your pronunciation. So this might provide value, especially to new language learners aiming to improve their pronunciation.

### Changes

Replaced wit.ai with google's speech-to-text api as wit was not intuitive to figure out.

Aplication only does transcribtion at least for now.


### Originality of the Code

`main.py` was fully written by me
`recorder.py` while copied from documentation was hevily modified to fit my usecase
`api.py` is essentially direct copy of google's example with minor modifications, it can be viewed [here](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/HEAD/speech/snippets/transcribe_async_file.py)

### Limitations and Improvements

Current solution supports only 10 seconds of recording and UI is very limited.

For future, I could improve the UI functionality:

- record/stop recording functions instead of time limit
- other quaility of life updates like instant feedback
- maybe even phrases for user to practice

Improve code readability:

- currently tkinter code is a bit hacky, I would like to avoid 3 line lambda function I have right now

Would be nice to have some tests for API too,
