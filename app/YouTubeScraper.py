import requests

def search_youtube_video_id(query, api_key):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": 1,
        "key": api_key
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        results = response.json().get("items")
        if results:
            return results[0]["id"]["videoId"]
        else:
            return None
    else:
        print("Erro na requisição:", response.status_code)
        return None
    

def get_youtube_comments(video_id, api_key, max_results=30):
    url = "https://www.googleapis.com/youtube/v3/commentThreads"
    params = {
        "part": "snippet",
        "videoId": video_id,
        "maxResults": max_results,
        "order": "time",
        "textFormat": "plainText",
        "key": api_key
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        comments_data = response.json().get("items", [])
        comments = []

        # Extrai o conteúdo de cada comentário
        for item in comments_data:
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            author = item["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]
            comments.append({"author": author, "comment": comment})

        return comments
    else:
        print("Erro na requisição:", response.status_code)
        return None