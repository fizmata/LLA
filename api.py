# This module handles API requests and responses

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        # print("Transcript: {}".format(result.alternatives[0].transcript))
        # print("Confidence: {}".format(result.alternatives[0].confidence))
        return ("Transcript: {}".format(result.alternatives[0].transcript))