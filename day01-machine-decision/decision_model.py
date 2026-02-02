"""
Day 01 – Rule-Based Decision System

This program demonstrates how early AI systems
made decisions using explicit rules instead of learning.
"""

# Day 01: Rule-based decision system
# This simulates how a machine makes decisions using logic

temperature = 35  # Celsius
humidity = 70     # Percentage

if temperature > 30 and humidity > 60:
    decision = "Turn ON air conditioning"
elif temperature > 30:
    decision = "Turn ON fan"
else:
    decision = "No cooling required"

print("Temperature:", temperature)
print("Humidity:", humidity)
print("System Decision:", decision)

print("\nExplanation:")
print("The system prioritizes high temperature and humidity together,")
print("showing how rules encode decision-making logic.")
