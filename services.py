import requests

BASE_URL = "https://sidebar.stract.to"
TOKEN = "ProcessoSeletivoStract2025"

FIELD_MAPPING = {
    "ad_name": "Ad Name",
    "adName": "Ad Name",
    "ctr_unique": "Unique Clickthrough Rate",
    "uniqueCTR": "Unique Clickthrough Rate",
    "ctr": "Clickthrough Rate",
    "cpc": "Cost per Click",
    "cost_per_click": "Cost per Click",
    "clicks": "Clicks",
    "impressions": "Impressions",
    "spend": "Spend",
    "cost": "Spend",
    "global_objective": "Objective",
    "objective": "Objective",
    "effective_status": "Status",
    "status": "Status",
    "country": "Country",
    "region": "Country"
}

def fetch_paginated_data(url, key):
    all_data = []
    page = 1
    while True:
        response = requests.get(f"{url}&page={page}", headers={"Authorization": f"Bearer {TOKEN}"})
        if response.status_code != 200:
            break
        data = response.json()
        all_data.extend(data.get(key, []))
        pagination = data.get("pagination", {})
        if pagination.get("current", 1) >= pagination.get("total", 1):
            break
        page += 1
    return all_data

def get_platforms():
    response = requests.get(f"{BASE_URL}/api/platforms", headers={"Authorization": f"Bearer {TOKEN}"})
    if response.status_code == 200:
        return response.json().get("platforms", [])
    return []

def get_accounts(platform):
    return fetch_paginated_data(f"{BASE_URL}/api/accounts?platform={platform}", "accounts")

def get_fields(platform):
    fields = fetch_paginated_data(f"{BASE_URL}/api/fields?platform={platform}", "fields")
    return {f["value"]: FIELD_MAPPING.get(f["value"], f["text"]) for f in fields}

def get_insights(platform, account_id, token, fields):
    fields_str = ",".join(fields.keys())
    insights = fetch_paginated_data(f"{BASE_URL}/api/insights?platform={platform}&account={account_id}&token={token}&fields={fields_str}", "insights")
    standardized_insights = []
    for insight in insights:
        standardized_entry = {fields.get(k, k): v for k, v in insight.items()}
        if platform == "ga4":
            standardized_entry["Cost per Click"] = standardized_entry["Spend"] / standardized_entry["Clicks"] if standardized_entry["Clicks"] else 0
        standardized_insights.append(standardized_entry)
    return standardized_insights
