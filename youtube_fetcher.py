# youtube_fetcher.py

import yt_dlp

def fetch_youtube_courses(query, max_results=3):
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'extract_flat': 'in_playlist',
        'default_search': 'ytsearch',
        'noplaylist': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(query, download=False)
            videos = info.get('entries', [])[:max_results]

            results = []
            for v in videos:
                results.append({
                    'title': v.get('title', ''),
                    'url': f"https://www.youtube.com/watch?v={v.get('id')}"
                })
            return results

    except Exception as e:
        print(f"[yt-dlp Error] {e}")
        return []
