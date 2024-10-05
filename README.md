# YouTube Transcript

YouTube Transcript helps to get transcripts of YouTube videos, tokenize the transcripts, and generate a summary of 
the transcripts using the Natural Language Toolkit by saving results to text files. It also allows you to get transcripts 
from a channel.  

## Installation

Dependencies to install:

```bash
pip install pytube3 youtube-transcript-api spacy
```

And spacy model:

```bash
python -m spacy download en_core_web_md
```

## Usage

Example how to receive a transcript with summary from a video:

```bash
python youtube-transcript.py "https://www.youtube.com/watch?v=VIDEO_ID&ab_channel=CHANNEL_ID" LANG LOCAL_DIR/transcript.txt LOCAL_DIR/summary.txt
```

Example how to receive a transcripts from a video channel:

```bash
python youtube-channel-transcript.py API_KEY CHANNEL_ID LANG LOCAL_DIR
```