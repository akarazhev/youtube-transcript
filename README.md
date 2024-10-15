# YouTube Transcript and Summary Tool

## Description

This script fetches the transcript of a YouTube video and generates a summary of the content. It can save both the full 
transcript and the summary to specified text files.

## Features

- **Transcript Retrieval**: Extracts the transcript from a YouTube video using the YouTube Transcript API.
- **Summarization**: Generates a summary of the transcript using natural language processing with spaCy.
- **File Output**: Saves both the transcript and the summary to user-defined file paths.

## Requirements

- **Python** 3.x

### Python Packages

The required packages are listed in `requirements.txt`. They include:

- `pytube`
- `youtube-transcript-api`
- `spacy`
- `en_core_web_md` spaCy language model

### Installation

1. **Clone the Repository** (or download the script directly):

   ```bash
   git clone https://github.com/akarazhev/youtube-transcript.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd youtube-transcript
   ```

3. **Create a Virtual Environment** (optional but recommended):

   ```bash
   python3 -m venv venv
   ```

   Activate the virtual environment:

    - On macOS/Linux:

      ```bash
      source venv/bin/activate
      ```

    - On Windows:

      ```bash
      venv\Scripts\activate
      ```

4. **Install the Required Packages**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

The script is run via the command line and requires a YouTube video URL. Optionally, you can provide paths to save the 
transcript and summary.

### Command Syntax

```bash
python youtube-transcript.py <YouTube_URL> [--transcript <Transcript_Output_Path>] [--summary <Summary_Output_Path>]
```

### Example

```bash
python youtube-transcript.py "https://www.youtube.com/watch?v=VIDEO_ID" --transcript transcript.txt --summary summary.txt
```

This command will:

- Fetch the transcript of the YouTube video at the given URL.
- Save the full transcript to `transcript.txt` (if the --transcript option is provided).
- Generate a summary of the transcript.
- Save the summary to `summary.txt` (if the --summary option is provided).

### Optional Parameters
- `--transcript <Transcript_Output_Path>`: The file path where the transcript will be saved. If not provided, the 
- transcript will be printed to the console.
- `--summary <Summary_Output_Path>`: The file path where the summary will be saved. If not provided, the summary will 
- be printed to the console.

### Help

For more information on the script's usage:

```bash
python youtube-transcript.py --help
```