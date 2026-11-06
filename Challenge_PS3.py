sent = str(input("Enter any sentence:"))
sent = sent.lower()

freq = {}

for char in sent:
    if char != " ":
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    # else:
    #     continue
for char, count in freq.items():
    print(char, ":", count)

            