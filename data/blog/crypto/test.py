c = "afZ_r9VYfScOeO_UL^RWUc"
p = "flag{"
# 已知：明文開頭是 flag{...
# 輸出密文的 ASCII 值
for i in c:
    a = ord(i)
    print(a, end=" ")
print("")
# 輸出明文的 ASCII 值
for i in p:
    a = ord(i)
    print(a, end=" ")

# Output:
# 97 102 90 95 114 57 
# 發現規律
plaintext = ""
j = 5
for i in c:
    plaintext += chr(ord(i) + j)
    j = j + 1
print(plaintext)