import requests
import json
from datetime import datetime, timezone

# ===== 配置 =====
APP_ID = "cli_a94703a307b91cd3"
APP_SECRET = "gfxa5p4l6X9hOZyV8rBiscQAolwOzJp7"
APP_TOKEN = "F31TbPACGaIWvNsF4LvcTeL4nDd"
TABLE_ID = "tblFaaFpCCLsKcCe"

# ===== 数据 =====
PARENT_SKU = "Pet-Feeder-116377"
KEYWORDS = "hanging chicken feeder, automatic chicken feeder, poultry feeder, hen feeder, farm feeder, self-filling feeder, refill chicken feeder, outdoor chicken feeder, gravity chicken feeder, chicken feed dispenser, poultry feed station, backyard chicken feeder, flock feeder, chook feeder, chook feed container, hen house feeder, hanging poultry feeder, large chicken feeder, plastic chicken feeder, no waste chicken feeder, chicken coop feeder, broiler feeder, turkey feeder, duck feeder, livestock feeder, poultry farming supplies, chook supplies, chicken keeping accessories, poultry equipment, backyard poultry, free range chicken equipment, hanging feed bucket, feeder for hens, chicken trough feeder, farm supplies australia, poultry care, automatic farm feeder, chicken farm accessories, chicken pen supplies, chicken coop accessories"
UPDATE_TIME_MS = int(datetime(2026, 4, 3, tzinfo=timezone.utc).timestamp() * 1000)
UPDATE_BY = "李梦"

def get_token():
      resp = requests.post(
                "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal",
                json={"app_id": APP_ID, "app_secret": APP_SECRET}
      )
      data = resp.json()
      print("Token response:", json.dumps(data, ensure_ascii=False))
      token = data.get("tenant_access_token")
      if not token:
                raise Exception("Failed to get token: " + str(data))
            return token

def insert_record(token):
      url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{APP_TOKEN}/tables/{TABLE_ID}/records"
    headers = {
              "Authorization": f"Bearer {token}",
              "Content-Type": "application/json"
    }
    payload = {
              "fields": {
                            "Parent SKU": PARENT_SKU,
                            "关键词": KEYWORDS,
                            "更新时间": UPDATE_TIME_MS,
                            "更新人员": UPDATE_BY
              }
    }
    resp = requests.post(url, headers=headers, json=payload)
    result = resp.json()
    print("Insert response:", json.dumps(result, ensure_ascii=False, indent=2))
    return result

if __name__ == "__main__":
      print(f"Writing record for SKU: {PARENT_SKU}")
    print(f"Keywords length: {len(KEYWORDS)} chars")
    token = get_token()
    result = insert_record(token)
    if result.get("code") == 0:
              print("SUCCESS! Record inserted.")
else:
        print(f"FAILED. Error code: {result.get('code')}, msg: {result.get('msg')}")
