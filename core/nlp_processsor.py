import json

def analyze_trading_data(data):
    """
    Translates trading data into text insights.
    """
    insights = []
    for token in data.get("tokens", []):
        name = token.get("name", "Unknown Token")
        price = token.get("price", 0)
        volume = token.get("volume", 0)
        
        if volume > 1000000:
            insight = f"{name} is buzzing with high trading activity today."
        elif price > 100:
            insight = f"{name} shows strong value growth potential."
        else:
            insight = f"{name} is relatively stable in the market."

        insights.append(insight)
    return insights

if __name__ == "__main__":
    with open("../data/trading_data.json", "r") as f:
        data = json.load(f)
    insights = analyze_trading_data(data)
    print("\n".join(insights))
