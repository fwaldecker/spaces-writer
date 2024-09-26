import yt_dlp
import re


def extract_m3u8_url(twitter_spaces_url):
    """Extracts the .m3u8 URL from a Twitter Spaces link using yt-dlp."""
    ydl_opts = {
        'quiet': True,  # Suppress output
        'format': 'best',  # Get the best quality format
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            # Download the metadata for the Twitter Spaces URL
            info_dict = ydl.extract_info(twitter_spaces_url, download=False)
            formats = info_dict.get('formats', [])

            # Find the .m3u8 format in the list of available formats
            for format in formats:
                if 'm3u8' in format.get('protocol', ''):
                    m3u8_url = format.get('url')
                    return m3u8_url

            raise ValueError("Could not find .m3u8 URL in formats")
        except Exception as e:
            raise Exception(f"Error extracting .m3u8 URL: {str(e)}")
