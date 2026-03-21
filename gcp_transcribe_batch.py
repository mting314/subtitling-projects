import os

from google.api_core.client_options import ClientOptions

from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import cloud_speech

# PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
PROJECT_ID = "future-name-201021"

# PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
REGION = "us"

MAX_AUDIO_LENGTH_SECS = 8 * 60 * 60


def transcribe_batch_3(
audio_uri: str,
) -> cloud_speech.BatchRecognizeResults:
    """Transcribes an audio file from a Google Cloud Storage URI using the Chirp 3 model of Google Cloud Speech-to-Text v2 API.
    Args:
        audio_uri (str): The Google Cloud Storage URI of the input audio file.
            E.g., gs://[BUCKET]/[FILE]
    Returns:
        cloud_speech.RecognizeResponse: The response from the Speech-to-Text API containing
        the transcription results.
    """

    # Instantiates a client
    client = SpeechClient(
        client_options=ClientOptions(
            api_endpoint=f"{REGION}-speech.googleapis.com",
        )
    )

    config = cloud_speech.RecognitionConfig(
        auto_decoding_config=cloud_speech.AutoDetectDecodingConfig(),
        language_codes=["ja-JP", "en-US"],
        model="chirp_3",
        features=cloud_speech.RecognitionFeatures(
                    # enable_word_confidence=True,
                    enable_word_time_offsets=True,
                    enable_automatic_punctuation=True,
                ),
    )

    file_metadata = cloud_speech.BatchRecognizeFileMetadata(uri=audio_uri)

    request = cloud_speech.BatchRecognizeRequest(
        recognizer=f"projects/{PROJECT_ID}/locations/{REGION}/recognizers/_",
        config=config,
        files=[file_metadata],
        recognition_output_config=cloud_speech.RecognitionOutputConfig(
            inline_response_config=cloud_speech.InlineOutputConfig(),
        ),
    )

    # Transcribes the audio into text
    operation = client.batch_recognize(request=request)

    print("Waiting for operation to complete...")
    # response = operation.result(timeout=120)
    response = operation.result(timeout=3 * MAX_AUDIO_LENGTH_SECS)
    print(response)
    for result in response.results[audio_uri].transcript.results:
        print(f"Transcript: {result.alternatives[0].transcript}")

    return response.results[audio_uri].transcript



AUDIO_URI = "gs://subtitling-projects/audio-files/Colors of Pure Sense.opus"
print(transcribe_batch_3(AUDIO_URI))
print("Batch transcription completed.")