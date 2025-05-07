reverse_conversion = {
"148635" : "A",
"14786545621" : "B",
"9874123" : "C",
"74178621" : "D",
"74123789456" : "E",
"74178945" : "F",
"987412563" : "G",
"741963456" : "H",
"852789123" : "I",
"7898521" : "J",
"7415953" : "K",
"32147" : "L",
"1475963" : "M",
"1475369" : "N",
"84268" : "O",
"741789654" : "P",
"4123698753" : "Q",
"7417895453" : "R",
"987456321" : "S",
"258789" : "T",
"7412369" : "U",
"74269" : "V",
"7415369" : "W",
"753951" : "X",
"75952" : "Y",
"7895123" : "Z" 
}
mini = 5

def decode_message(msg):
    start = 0
    end = mini
    ans = ""
    while end < len(msg) + 1:
        tmp = msg[start:end]
        if tmp in reverse_conversion:
            ans += reverse_conversion[tmp]
            start = end
            end += 5
        else:
            end += 1
    return ans

cipher = list(input("Enter the cipher to decode: ").split(" "))
start = 0
end = mini
plain_text = []
for msg in cipher:
    plain_text.append(decode_message(msg))

print(" ".join(plain_text))
