import requests
import json
from datetime import datetime, timezone

APP_ID = "cli_a94703a307b91cd3"
APP_SECRET = "gfxa5p4l6X9hOZyV8rBiscQAolwOzJp7"
APP_TOKEN = "F31TbPACGaIWvNsF4LvcTeL4nDd"
TABLE_ID = "tblFaaFpCCLsKcCe"

# Step 1: Get token
token_resp = requests.post(
    "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal",
    json={"app_id": APP_ID, "app_secret": APP_SECRET}
)
token_data = token_resp.json()
print("Token response:", json.dumps(token_data, ensure_ascii=False))

token = token_data.get("tenant_access_token")
if not token:
    print("Failed to get token")
    exit(1)

# Step 2: Insert record
keywords = "hanging chicken feeder, automatic chicken feeder, poultry feeder, hen feeder, farm feeder, self-filling feeder, refill chicken feeder, outdoor chicken feeder, gravity chicken feeder, chicken feed dispenser, poultry feed station, backyard chicken feeder, flock feeder, chook feeder, chook feed container, hen house feeder, hanging poultry feeder, large chicken feeder, plastic chicken feeder, no waste chicken feeder, chicken coop feeder, broiler feeder, turkey feeder, duck feeder, livestock feeder, poultry farming supplies, chook supplies, chicken keeping accessories, poultry equipment, backyard poultry, free range chicken equipment, hanging feed bucket, feeder for hens, chicken trough feeder, farm supplies australia, poultry care, automatic farm feeder, chicken farm accessories, chicken pen supplies, chicken coop accessories"

ts_ms = int(datetime(2026, 4, 3, tzinfo=timezone.utc).timestamp() * 1000)

resp = requests.post(
    f"https://open.feishu.cn/open-apis/bitable/v1/apps/{APP_TOKEN}/tables/{TABLE_ID}/records",
    headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
    json={
        "fields": {
            "Parent SKU": "Pet-Feeder-116377",
            "关键词": keywords,
            "更新时间": ts_ms,
            "更新人员": "李梦"
        }
    }
)

result = resp.json()
print("Insert response:", json.dumps(result, ensure_ascii=False, indent=2))
