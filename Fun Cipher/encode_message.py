conversion = {
"A" : "148635",
"B" : "14786545621",
"C" : "9874123",
"D" : "74178621",
"E" : "74123789456",
"F" : "74178945",
"G" : "987412563",
"H" : "741963456",
"I" : "852789123",
"J" : "7898521",
"K" : "7415953",
"L" : "32147",
"M" : "1475963",
"N" : "1475369",
"O" : "84268",
"P" : "741789654",
"Q" : "4123698753",
"R" : "7417895453",
"S" : "987456321",
"T" : "258789",
"U" : "7412369",
"V" : "74269",
"W" : "7415369",
"X" : "753951",
"Y" : "75952",
"Z" : "7895123"
}

def encode_message(word):
    ans = ""
    for ch in word:
        ans += conversion[ch.upper()]
    return ans

message = list(input("Input the message to decode: ").split(" "))
cipher = []
for word in message:
    cipher.append(encode_message(word))

print(" ".join(cipher))
