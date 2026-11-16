# Cuts out the two bars, the text between them and the character just after the closing bar
string = input()
start = string.find("|", 0)
end = string.find("|", start + 1) + 1
if not(start == (end - 2)): string = string.replace(string[start:end+1], "")
else: string = string.replace("|", "")
print(string)
