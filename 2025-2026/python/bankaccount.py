print("--- Bank Accounts ---")
for person in [me, bestie, mom]:
    print(f"{person.owner}: ${person.balance}")

print("\n--- Smartphones ---")
# Printing out the Smartphones
for phone in [iphone, pixel, samsung]:
    print(f"{phone.brand} {phone.model} ({phone.color}, {phone.storage})")

