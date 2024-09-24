# pip install pytube3 youtube-transcript-api spacy
# python -m spacy download en_core_web_lg
# python -m spacy download ru_core_news_lg
from pytube import extract
from heapq import nlargest
from youtube_transcript_api import YouTubeTranscriptApi
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

url = 'https://www.youtube.com/watch?v=_uMIt3GPcOQ'
video_id = extract.video_id(url)

transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
text = ""
for elem in transcript:
    text = text + " " + elem["text"]

nlp = spacy.load('en_core_web_lg')
document = nlp(text)
for sentence in document.sents:
    print(sentence.text)

tokens = [token.text for token in document]

word_frequencies = {}
for word in document:
    text = word.text.lower()
    if text not in list(STOP_WORDS) and text not in punctuation:
        if word.text not in word_frequencies.keys():
            word_frequencies[word.text] = 1
        else:
            word_frequencies[word.text] += 1

max_frequency = max(word_frequencies.values())
for word in word_frequencies.keys():
    word_frequencies[word] = word_frequencies[word] / max_frequency

sentence_tokens = [sentence for sentence in document.sents]
sentence_score = {}
for sentence in sentence_tokens:
    for word in sentence:
        if word.text.lower() in word_frequencies.keys():
            if sentence not in sentence_score.keys():
                sentence_score[sentence] = word_frequencies[word.text.lower()]
            else:
                sentence_score[sentence] += word_frequencies[word.text.lower()]

select_length = int(len(sentence_tokens) * 0.3)
summary = nlargest(select_length, sentence_score, key=sentence_score.get)
final_summary = [word.text for word in summary]
summary = ' '.join(final_summary)
