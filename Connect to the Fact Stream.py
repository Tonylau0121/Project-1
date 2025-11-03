import requests

def get_random_fact():
    # API 網址（回傳英文版的隨機事實）
    url = "https://uselessfacts.jsph.pl/random.json?language=en"

    try:
        # 向 API 發送 GET 請求
        response = requests.get(url)
        response.raise_for_status()  # 若出現錯誤代碼（例如 404、500）會拋出例外

        # 解析回傳的 JSON 資料
        data = response.json()

        # 印出事實內容
        print("💡 隨機冷知識：")
        print(data["text"])

    except requests.exceptions.RequestException as e:
        print("⚠️ 連線或請求發生錯誤：", e)

# 主程式執行
if __name__ == "__main__":
    get_random_fact()
