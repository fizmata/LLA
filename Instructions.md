## Setup to run the code

*Disclamer: This documentation is not tested and is provided as best effort*

requred python modules can be found in `requirements.txt`, they can be automatically installed by running

```
pip install -r requirements.txt
```

I also encountered problem with that was solved by installing `libportaudio2`

this can easily be done on debian based systems via command:

```
apt install libportaudio2

```

For authentication with google API you'll need variable **GOOGLE_APPLICATION_CREDENTIALS** which point to the GCP Service Account key, information regarding how to set that up can be found [here](https://cloud.google.com/speech-to-text/docs/before-you-begin#create_a_service_account)

To run the project run main.py

