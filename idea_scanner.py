import datetime

def scan_micro_trends():
    # In a live script, this would query APIs or trending lists
    # For now, it logs the check and simulates discovering a high-demand micro-niche
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    ideas = [
        {"niche": "Shopify CSV Quick-Formatters", "demand": "Medium", "competition": "Low"},
        {"niche": "Notion-to-Markdown Bulk Exporters", "demand": "High", "competition": "Medium"},
        {"niche": "Local Currency Auto-Converters for Small E-Com", "demand": "High", "competition": "Low"}
    ]
    
    print(f"[{timestamp}] Idea Scanner Ran Successfully.")
    print("Top Trending Micro-Utility Opportunity Discovered:")
    print(f"-> Niche: {ideas[2]['niche']} | Demand: {ideas[2]['demand']} | Competition: {ideas[2]['competition']}")

if __name__ == "__main__":
    scan_micro_trends()
