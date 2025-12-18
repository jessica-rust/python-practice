results = ["Mario", "Luigi"]

# adds names to the end of the list
results.append("Princess")
results.append("Yoshi")
results.append("Koopa Troopa")
results.append("Toad")

# .append() adds the list itself to results
results.append(["Bowser", "Donky Kong Jr."])
# .remove() removes the added list
results.remove(["Bowser", "Donky Kong Jr."])
# .extend() adds the items in the list to results
results.extend(["Bowser", "Donky Kong Jr."])

print("Results:", results)

results_2 = ['Mario', 'Luigi', 'Princess', 'Yoshi', 'Koopa Troopa', 'Toad', 'Bowser', 'Donky Kong Jr.']

results_2.remove("Bowser")
# .insert() adds Bowser in first place or the 0th index
results_2.insert(0,"Bowser")
# .reverse() filips the list around entirely
results_2.reverse()

print("Results_2:", results_2)


