import requests
import json
from datetime import datetime

# 配置
APP_ID = "cli_a94703a307b91cd3"
APP_SECRET = "gfxa5p4l6X9hOZyV8rBiscQAolwOzJp7"
APP_TOKEN = "F31TbPACGaIWvNsF4LvcTeL4nDd"
TABLE_ID = "tblFaaFpCCLsKcCe"

# Step 1: 获取 tenant_access_token
def get_tenant_access_token():
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    payload = {"app_id": APP_ID, "app_secret": APP_SECRET}
    resp = requests.post(url, json=payload)
    data = resp.json()
    print("获取 token 响应:", json.dumps(data, ensure_ascii=False))
    return data.get("tenant_access_token")

# Step 2: 写入记录
def write_record(token):
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{APP_TOKEN}/tables/{TABLE_ID}/records"
    
    # 2026-04-03 转毫秒时间戳（UTC 00:00:00）
    dt = datetime(2026, 4, 3, 0, 0, 0)
    ts_ms = int(dt.timestamp() * 1000)
    print(f"更新时间毫秒时间戳: {ts_ms}")
    
    keywords = "hanging chicken feeder,automatic chicken feeder,poultry feeder hanging,chicken feeder refill,hen feeder,poultry farm feeder,gravity chicken feeder,hanging bird feeder farm,chook feeder,chicken food dispenser,automatic poultry feeder,hanging feeder for chickens,farm chicken feeder,refillable chicken feeder,outdoor chicken feeder,backyard chicken feeder,large chicken feeder,chicken feeding station,poultry waterer feeder,hen house feeder,coop feeder,chicken grain feeder,hanging grain dispenser,self-filling chicken feeder,flock feeder,bird feeder hanging outdoor,galvanized chicken feeder,plastic chicken feeder,chicken trough feeder,feeder for hens,poultry equipment,farm feeding equipment,gravity feeder poultry,chicken feeder holder,weather resistant chicken feeder,squirrel proof chicken feeder,rodent proof feeder,anti-spill chicken feeder,no waste chicken feeder,chicken feeder with hanger,easy clean chicken feeder,durable poultry feeder,large capacity chicken feeder,chicken feed storage feeder,hanging tube feeder,chicken feed dispenser automatic,poultry feed dispenser,free range chicken feeder,chicken feeder hook,feeder for small flock,hanging feeder outdoor,chicken care equipment,poultry farming supplies,chichen feeder,chook feedeer,chickn feeder,haning chicken feeder,automtic feeder chicken"
    
    fields = {
        "Parent SKU": "Pet-Feeder-116377",
        "关键词": keywords,
        "更新时间": ts_ms,
        "更新人员": "李梦"
    }
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    payload = {"fields": fields}
    print("\n写入字段:", json.dumps(fields, ensure_ascii=False, indent=2))
    
    resp = requests.post(url, headers=headers, json=payload)
    data = resp.json()
    print("\n写入记录响应:", json.dumps(data, ensure_ascii=False, indent=2))
    return data

if __name__ == "__main__":
    print("=== Step 1: 获取 tenant_access_token ===")
    token = get_tenant_access_token()
    if not token:
        print("获取 token 失败，退出")
        exit(1)
    print(f"Token 获取成功: {token[:20]}...")
    
    print("\n=== Step 2: 写入记录 ===")
    result = write_record(token)
