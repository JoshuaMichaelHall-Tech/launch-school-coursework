char_sequence = 'TXkgaG92ZXJjcmFmdCBpcyBmdWxsIG9mIGVlbHMu'
char_list = list(char_sequence)
result = False
for char in char_list:
    if char == 'x':
        result = True
print(result)

print('x' in char_sequence)
