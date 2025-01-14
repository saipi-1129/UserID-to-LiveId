import requests,json

url = "https://www.mirrativ.com/api/user/profile?user_id=8740114"

res = requests.get(url)

if res.status_code == 200:
    try:

        data = res.json()
        live_id = data["onlive"]["live_id"]

        print(live_id)
    except ValueError:
        print("レスポンスの解析中にエラーが発生しました。")
        
else:
    print(f"リクエストに失敗しました。ステータスコード: {res.status_code}")