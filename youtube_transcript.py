from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from datetime import datetime
import os

def get_transcript(video_url):
    try:
        # Extract video ID from URL
        video_id = video_url.split("v=")[1].split("&")[0]
        
        # Get transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['zh-CN'])
        
        # Format transcript to plain text
        formatter = TextFormatter()
        formatted_transcript = formatter.format_transcript(transcript)
        
        return formatted_transcript
        
    except Exception as e:
        return f"Error: {str(e)}"

def save_transcript(transcript):
    # Create 'transcripts' directory if it doesn't exist
    os.makedirs('transcripts', exist_ok=True)
    
    # Generate filename with current date (yyyyMMdd.txt)
    filename = datetime.now().strftime('%Y%m%d') + '.txt'
    filepath = os.path.join('transcripts', filename)
    
    # Save transcript to file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(transcript)
    
    return filepath

if __name__ == "__main__":
    # Example usage
    video_url = input("Enter YouTube video URL: ")
    transcript = get_transcript(video_url)
    
    if not transcript.startswith('Error'):
        filepath = save_transcript(transcript)
        print(f"\nTranscript saved to: {filepath}")
    
    print("\nTranscript:")
    print(transcript) 