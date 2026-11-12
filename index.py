# ================= SET QUESTIONS =================

# 1. Add Element
s = {1, 2, 3}
s.add(4)
print(s)

# 2. Remove Element
s = {1, 2, 3}
s.discard(2)
print(s)

# 3. Union
a, b = {1, 2}, {2, 3}
print(a | b)

# 4. Intersection
print(a & b)

# 5. Difference
a, b = {1, 2, 3}, {2, 3}
print(a - b)

# 6. Check Subset
print({1, 2}.issubset({1, 2, 3}))

# 7. Set Length
s = {1, 2, 3}
print(len(s))

# 8. Clear Set
s.clear()
print(s)

# 9. Symmetric Difference
a, b = {1, 2, 3}, {2, 3, 4}
print(a ^ b)

# 10. Convert List to Set
lst = [1, 2, 2, 3]
print(set(lst))


# ============== DICTIONARY QUESTIONS ==============

# 11. Create Dictionary from Two Lists
keys = ["a", "b"]
values = [1, 2]
print(dict(zip(keys, values)))

# 12. Update Dictionary Value
d = {"a": 1}
d["a"] = 2
print(d)

# 13. Remove Key
d = {"a": 1, "b": 2}
d.pop("b")
print(d)

# 14. Check Key Existence
d = {"x": 1}
print("x" in d)

# 15. Iterate Dictionary
d = {"a": 10, "b": 20}
for k, v in d.items():
    print(k, v)

# 16. Dictionary Length
d = {"x": 1, "y": 2}
print(len(d))

# 17. Merge Dictionaries
d1 = {"a": 1}
d2 = {"b": 2}
print({**d1, **d2})

# 18. Get Value with Default
d = {"a": 1}
print(d.get("b", 0))

# 19. Count Frequency
lst = [1, 2, 2, 3]
freq = {}
for i in lst:
    freq[i] = freq.get(i, 0) + 1
print(freq)

# 20. Invert Dictionary
d = {"a": 1, "b": 2}
print({v: k for k, v in d.items()})

# 21. Key with Maximum Value
d = {"a": 10, "b": 20, "c": 15}
print(max(d, key=d.get))

# 22. Sort Dictionary by Values
d = {"a": 3, "b": 1, "c": 2}
print(sorted(d.items(), key=lambda x: x[1]))

# 23. Dictionary of Squares
print({i: i**2 for i in range(1, 4)})


# 24. Filter Dictionary by Value
d = {"a": 10, "b": 5, "c": 15}
print({k: v for k, v in d.items() if v > 10})

# 25. Combine Values of Duplicate Keys
d1 = {"a": 1, "b": 2}
d2 = {"a": 3, "c": 4}

result = d1.copy()
for k, v in d2.items():
    result[k] = result.get(k, 0) + v

print(result)


# 26. Count Word Frequency in Sentence
text = "apple banana apple"
freq = {}

for word in text.split():
    freq[word] = freq.get(word, 0) + 1

print(freq)


# 27. Remove Duplicate Values from Dictionary
d = {"a": 1, "b": 2, "c": 1}

result = {}
for k, v in d.items():
    if v not in result.values():
        result[k] = v

print(result)


# 28. Find Common Keys in Two Dictionaries
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

result = list(d1.keys() & d2.keys())
print(result)


# 29. Swap Keys and Values Safely
d = {"x": 1, "y": 2}

result = {v: k for k, v in d.items()}
print(result)


# 30. Delete Items by Value
d = {"a": 1, "b": 2, "c": 1}

result = {k: v for k, v in d.items() if v != 1}
print(result)