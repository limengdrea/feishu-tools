import requests
import json

APP_ID     = "cli_a94703a307b91cd3"
APP_SECRET = "gfxa5p4l6X9hOZyV8rBiscQAolwOzJp7"
APP_TOKEN  = "F31TbPACGaIWvNsF4LvcTeL4nDd"
TABLE_ID   = "tblFaaFpCCLsKcCe"

# Step 1: Get tenant_access_token
print("=== Step 1: Get tenant_access_token ===")
token_resp = requests.post(
    "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal",
    json={"app_id": APP_ID, "app_secret": APP_SECRET},
)
token_data = token_resp.json()
print(json.dumps(token_data, ensure_ascii=False, indent=2))

token = token_data.get("tenant_access_token")
if not token:
    raise SystemExit("Failed to get tenant_access_token")

# Step 2: Insert record
print("\n=== Step 2: Insert record ===")
fields = {
    "Parent SKU": "Pet-Feeder-116377",
    "关键词": (
        "hanging chicken feeder, automatic chicken feeder, poultry feeder, "
        "hen feeder, farm feeder, self-filling feeder, refill chicken feeder, "
        "outdoor chicken feeder, gravity chicken feeder, chicken feed dispenser, "
        "poultry feed station, backyard chicken feeder, flock feeder, chook feeder, "
        "chook feed container, hen house feeder, hanging poultry feeder, "
        "large chicken feeder, plastic chicken feeder, no waste chicken feeder, "
        "chicken coop feeder, broiler feeder, turkey feeder, duck feeder, "
        "livestock feeder, poultry farming supplies, chook supplies, "
        "chicken keeping accessories, poultry equipment, backyard poultry, "
        "free range chicken equipment, hanging feed bucket, feeder for hens, "
        "chicken trough feeder, farm supplies australia, poultry care, "
        "automatic farm feeder, chicken farm accessories, chicken pen supplies, "
        "chicken coop accessories"
    ),
    "更新时间": 1743638400000,
    "更新人员": "李梦",
}

resp = requests.post(
    f"https://open.feishu.cn/open-apis/bitable/v1/apps/{APP_TOKEN}/tables/{TABLE_ID}/records",
    headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
    json={"fields": fields},
)
print(json.dumps(resp.json(), ensure_ascii=False, indent=2))
