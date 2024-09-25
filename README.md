# youtube-transcript

YouTube Transcript helps to get transcripts of YouTube videos, tokenize the transcripts, and generate a summary of 
the transcripts using the Natural Language Toolkit.  

Dependencies to install:

```bash
pip install pytube3 youtube-transcript-api spacy
python -m spacy download en_core_web_md
python -m spacy download ru_core_news_md
```

Example usage:

```bash
python youtube-transcript.py "https://www.youtube.com/watch?v=EpipswT-LuE&ab_channel=TED" en out/transcript.txt out/summary.txt
```