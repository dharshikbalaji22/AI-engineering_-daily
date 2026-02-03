"""
Day 02 – AQI Scoring-Based AI System

This program models air quality risk using a
continuous scoring approach instead of rigid rules.
It bridges early AI expert systems and
machine learning-style reasoning.
"""

# Take AQI input
aqi = int(input("Enter AQI value: "))

# Normalize AQI to a 0–1 risk score
risk_score = aqi / 500

# Interpret the risk score
if risk_score <= 0.2:
    health_risk = "Low risk (Good air quality)"
elif risk_score <= 0.4:
    health_risk = "Moderate risk"
elif risk_score <= 0.6:
    health_risk = "High risk for sensitive groups"
elif risk_score <= 0.8:
    health_risk = "Very high health risk"
else:
    health_risk = "Severe health risk"

# Output results
print("AQI:", aqi)
print("Risk Score:", round(risk_score, 2))
print("Health Interpretation:", health_risk)
