from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "クラウドでPythonが動いています"}
from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

# ★ オッズ取得用の関数（JRA-VAN API などに置き換える）
async def fetch_odds(race_id: str, minutes_before: int):
    # ここは実際のオッズ取得処理に置き換える
    # 今はテスト用のダミーデータ
    dummy_data = {
        "horses": [
            {"number": 3, "name": "サンプルホース", "odds": 5.0, "pop": 5},
            {"number": 7, "name": "テストホース", "odds": 12.0, "pop": 8},
        ]
    }
    return dummy_data


@app.get("/odds/simple-distortion")
async def simple_distortion(race_id: str, before: int, after: int):
    # ① before のオッズ取得
    odds_before = await fetch_odds(race_id, before)
    if not odds_before:
        raise HTTPException(status_code=404, detail="before odds not found")

    # ② after のオッズ取得
    odds_after = await fetch_odds(race_id, after)
    if not odds_after:
        raise HTTPException(status_code=404, detail="after odds not found")

    # ③ 馬ごとに比較
    result = []
    for hb in odds_before["horses"]:
        # after 側の同じ馬を探す
        ha = next((x for x in odds_after["horses"] if x["number"] == hb["number"]), None)
        if not ha:
            continue

        odds_before_val = hb["odds"]
        odds_after_val = ha["odds"]

        # 変動率
        change_rate = (odds_after_val - odds_before_val) / odds_before_val

        # 人気変動
        pop_change = hb["pop"] - ha["pop"]

        # 歪みスコア（簡易版）
        distortion_score = abs(change_rate) * 100 + abs(pop_change) * 10

        # ラベル判定
        if distortion_score >= 40:
            label = "強い歪み"
        elif distortion_score >= 20:
            label = "やや歪み"
        else:
            label = "通常"

        result.append({
            "number": hb["number"],
            "name": hb["name"],
            "odds_before": odds_before_val,
            "odds_after": odds_after_val,
            "pop_before": hb["pop"],
            "pop_after": ha["pop"],
            "odds_change_rate": round(change_rate, 3),
            "pop_change": pop_change,
            "distortion_score": round(distortion_score, 1),
            "label": label
        })

    return {
        "race_id": race_id,
        "before_minutes": before,
        "after_minutes": after,
        "horses": result
    }
