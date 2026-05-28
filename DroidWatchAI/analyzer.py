keywords = {
    "sms":"HIGH",
    "accessibility":"CRITICAL",
    "background":"MEDIUM",
    "service":"MEDIUM",
    "permission":"LOW",
    "network":"HIGH"
}

with open("logs.txt","r",errors="ignore") as file:
    logs=file.readlines()

alerts=[]

for line in logs:
    for keyword,risk in keywords.items():
        if keyword.lower() in line.lower():
            alerts.append((risk,line.strip()))

print("\n===== DROIDWATCH AI REPORT =====\n")

for risk,alert in alerts[:50]:
    print(f"[{risk}] {alert}")

print("\nTotal Suspicious Events:",len(alerts))