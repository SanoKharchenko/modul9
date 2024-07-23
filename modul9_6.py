def all_variants(text):
    for len_ in range(len(text)):
        for j in range(len(text) - len_):
            yield text[j:j + len_ + 1]


a = all_variants("abc")
for i in a:
    print(i)
