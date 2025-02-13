from flask import Flask, jsonify, request, Response
import pandas as pd
import requests
from services import get_platforms, get_accounts, get_fields, get_insights
from reports import generate_report, generate_summary

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "name": "Lorenzo Lopes Pastuch",
        "email": "lorenzopastuch@gmail.com",
        "linkedin": "https://www.linkedin.com/in/lorenzo-lopes-pastuch-9867011b6/"
    })

@app.route("/geral", methods=["GET"])
def general_report():
    platforms = get_platforms()
    all_data = []
    for platform in platforms:
        platform_value = platform["value"]
        accounts = get_accounts(platform_value)
        fields = get_fields(platform_value)
        for account in accounts:
            insights = get_insights(platform_value, account["id"], account["token"], fields)
            for insight in insights:
                insight["account_name"] = account["name"]
                insight["platform"] = platform["text"]
            all_data.extend(insights)
    csv_data = generate_report(all_data)
    return Response(csv_data, mimetype="text/csv")

@app.route("/geral/resumo", methods=["GET"])
def general_summary():
    platforms = get_platforms()
    all_data = []
    for platform in platforms:
        platform_value = platform["value"]
        accounts = get_accounts(platform_value)
        fields = get_fields(platform_value)
        for account in accounts:
            insights = get_insights(platform_value, account["id"], account["token"], fields)
            for insight in insights:
                insight["account_name"] = account["name"]
                insight["platform"] = platform["text"]
            all_data.extend(insights)
    csv_data = generate_summary(all_data, "platform")
    return Response(csv_data, mimetype="text/csv", headers={"Content-Disposition": "attachment; filename=geral_resumo.csv"})

@app.route("/<string:platform>", methods=["GET"])
def platform_report(platform):
    accounts = get_accounts(platform)
    fields = get_fields(platform)
    all_data = []
    for account in accounts:
        insights = get_insights(platform, account["id"], account["token"], fields)
        for insight in insights:
            insight["account_name"] = account["name"]
        all_data.extend(insights)
    csv_data = generate_report(all_data)
    return Response(csv_data, mimetype="text/csv")

@app.route("/<string:platform>/resumo", methods=["GET"])
def platform_summary(platform):
    accounts = get_accounts(platform)
    fields = get_fields(platform)
    all_data = []
    for account in accounts:
        insights = get_insights(platform, account["id"], account["token"], fields)
        for insight in insights:
            insight["account_name"] = account["name"]
        all_data.extend(insights)
    csv_data = generate_summary(all_data, "account_name")
    return Response(csv_data, mimetype="text/csv", headers={"Content-Disposition": f"attachment; filename={platform}_resumo.csv"})

if __name__ == "__main__":
    app.run(debug=True)
