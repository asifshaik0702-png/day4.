# Cyber Activity Risk Analyzer
# Register Number: 468


D = 468 % 10
print("Register Digit (D):", D)


activity_scores = [10, 45, 78, 120, -5, 30, 99, 150]


low_risk = []
medium_risk = []
high_risk = []
critical_risk = []

# Counters
valid_entries = 0
ignored_entries = 0
removed_due_to_personalization = 0


for score in activity_scores:

    if score < 0:
        ignored_entries = ignored_entries + 1

    else:
        valid_entries = valid_entries + 1

        if score >= 0 and score <= 30:
            low_risk = low_risk + [score]

        elif score >= 31 and score <= 60:
            medium_risk = medium_risk + [score]

        elif score >= 61 and score <= 100:
            high_risk = high_risk + [score]

        else:
            critical_risk = critical_risk + [score]


print("\nBefore Personalized Filtering:")
print("Low Risk:", low_risk)
print("Medium Risk:", medium_risk)
print("High Risk:", high_risk)
print("Critical Risk:", critical_risk)

if D % 2 == 0:
    removed_due_to_personalization = len(low_risk)
    low_risk = []

else:

    removed_due_to_personalization = len(critical_risk)
    critical_risk = []


print("\nAfter Personalized Filtering:")
print("Low Risk:", low_risk)
print("Medium Risk:", medium_risk)
print("High Risk:", high_risk)
print("Critical Risk:", critical_risk)

print("\nFinal Security Report:")
print("Total Valid Entries:", valid_entries)
print("Ignored Entries:", ignored_entries)
print("Removed Due to Personalization:", removed_due_to_personalization)
