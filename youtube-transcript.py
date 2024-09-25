from heapq import nlargest
from string import punctuation

import argparse
import spacy
import os
from pytube import extract
from spacy.lang.en.stop_words import STOP_WORDS
from youtube_transcript_api import YouTubeTranscriptApi


class YoutubeParser:

    def __init__(self, url, lang):
        self.url = url
        self.lang = lang

    def extract_video_id(self):
        """
        Extract the video ID from the YouTube URL.
        """
        video_id = extract.video_id(self.url)
        if video_id:
            return video_id
        else:
            raise ValueError("Invalid YouTube URL provided.")

    def get_transcript_html(self):
        """
        Get transcript HTML from YouTube.
        """
        text = ""
        for elem in YouTubeTranscriptApi.get_transcript(self.extract_video_id(), languages=[self.lang]):
            text = text + " " + elem["text"]

        return text

    def fetch_transcript(self):
        """
        Fetch the transcript from YouTube.
        """
        transcript = self.get_transcript_html()
        return transcript

    def fetch_summary(self):
        """
        Fetch the summary from YouTube.
        """
        nlp = spacy.load('en_core_web_md' if self.lang == 'en' else 'ru_core_news_md')
        document = nlp(self.get_transcript_html())
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
        return summary


def write_to_file(transcript, file_path):
    """
    Write the transcript to a specified file path.
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(transcript)
    except IOError as e:
        print(f"Error writing to file: {e}")


def main():
    parser = argparse.ArgumentParser(description="Fetch and save YouTube video transcripts and make summaries.")
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument("lang", help="Language of the transcript")
    parser.add_argument("transcript", help="Path to save the transcript")
    parser.add_argument("summary", help="Path to save the summary")

    args = parser.parse_args()
    youtube_parser = YoutubeParser(args.url, args.lang)

    try:
        transcript = youtube_parser.fetch_transcript()
        if transcript:
            write_to_file(transcript, args.transcript)
            print(f"Transcript saved to: {args.transcript}")
        else:
            print("Failed to retrieve transcript.")

        summary = youtube_parser.fetch_summary()
        if summary:
            write_to_file(summary, args.summary)
            print(f"Summary saved to: {args.summary}")
        else:
            print("Failed to retrieve summary.")

    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()
