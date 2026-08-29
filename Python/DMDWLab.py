from itertools import combinations
transactions = [
    ['Milk', 'Bread', 'Cookie'],
    ['Bread', 'Butter', 'Cookie'],
    ['Milk', 'Butter', 'Chocolate'],
    ['Milk', 'Bread', 'Cookie'],
    ['Milk', 'Bread', 'Cookie']
]
min_support = 2
item_counts = {}
for t in transactions:
  for item in t:
    item_counts[item] = item_counts.get(item, 0) + 1
print("Item Counts:", item_counts)
frequent_items = {item: count for item, count in item_counts.items() if count >= min_support}
print("Frequent 1- Itemsets:", frequent_items)
pair_counts = {}
for t in transactions:
  for pair in combinations(t, 2):
    pair = tuple(sorted(pair))
    pair_counts[pair] = pair_counts.get(pair, 0) + 1
frequent_pairs = {pair: count for pair, count in pair_counts.items() if count >= min_support}
print("Frequent 2- Itemsets:", frequent_pairs)
trio_counts = {}
for t in transactions:
  for trio in combinations(t, 3):
    trio = tuple(sorted(trio))
    trio_counts[trio] = trio_counts.get(trio, 0) + 1
frequent_trios = {trio: count for trio, count in trio_counts.items() if count >= min_support}
print("Frequent 3- Itemsets:", frequent_trios)
rules = []
for pair, support_AB in frequent_pairs.items():
  A, B = pair
  confidence_A_to_B = support_AB / item_counts[A]
  confidence_B_to_A = support_AB / item_counts[B]
  if confidence_A_to_B >= 0.5:
    rules.append((A, B, confidence_A_to_B))
  if confidence_B_to_A >= 0.5:
    rules.append((B, A, confidence_B_to_A))
for trio, support_ABC in frequent_trios.items():
  A, B, C = trio
  confidence_AB_to_C = support_ABC / frequent_pairs.get((A, B), 1)
  if confidence_AB_to_C >= 0.5:
    rules.append((f"{A} & {B}",C, confidence_AB_to_C))
  confidence_AC_to_B = support_ABC / frequent_pairs.get((A, C), 1)
  if confidence_AC_to_B >= 0.5:
    rules.append((f"{A} & {C}",B, confidence_AC_to_B))
  confidence_BC_to_A = support_ABC / frequent_pairs.get((B, C), 1)
  if confidence_BC_to_A >= 0.5:
    rules.append((f"{B} & {C}",A, confidence_BC_to_A))
print("\nAssociation Rules")
for rule in rules:
  print(f"If a Customer buys {rule[0]}, they are likely to buy {rule[1]} (Confidence: {rule[2]:.2f})")