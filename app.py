from flask import Flask, render_template, request
import requests

# Webアプリ作成
app = Flask(__name__, static_folder='./templates/images')

@app.route("/")
def top():
    userid = request.args.get('userid', '') or request.form.get('userid', '')

    if not userid:
        return render_template("index.html", names=False, userides=False, error="Live ID is required.")
    else:
        
        url = f"https://www.mirrativ.com/api/user/profile?user_id={userid}"

        res = requests.get(url)

        if res.status_code == 200:
            try:

                data = res.json()
                live_id = data["onlive"]["live_id"]
                name = data["name"]

                print(live_id)
                return render_template("index.html",live_id=live_id,name=name,error=None)
            except:
                print("レスポンスの解析中にエラーが発生したか、ユーザが配信していません。")
                return render_template("index.html",live_id=False,name=False,error="ユーザが配信していません。")
        else:
            print(f"リクエストに失敗しました。ステータスコード: {res.status_code}")
            return render_template("index.html",live_id=False,name=False,error="ユーザーIDが正しいか確認してから再度お試しください。")
    
    
    return render_template("index.html")
@app.route('/userid' ,methods=['POST'])
def search():
    userid = request.form['userid']
    print(f"[+] LiveId POST Success: {userid}")
    # POSTされたlive_idを使って再度fetch_online_users関数に処理を行わせる
    return top()



if __name__ == '__main__':  
    app.run(host="0.0.0.0", debug=True)



