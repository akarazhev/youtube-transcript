import argparse


class YoutubeParser:

    def __init__(self, channel_id, api_key):
        self.channel_id = channel_id
        self.api_key = api_key

    def get_videos(self):
        pass

    def get_transcript(self):
        pass


def write_to_file(transcript, file_path):
    pass


def main():
    parser = argparse.ArgumentParser(description="Fetch and save YouTube video transcripts from the channel.")
    parser.add_argument("channel_id", help="YouTube Channel Id")
    parser.add_argument("api_key", help="YouTube API Key")


if __name__ == "__main__":
    main()
