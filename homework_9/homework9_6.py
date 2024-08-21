# Генераторы
def all_variants(text):
    for repeat in range(len(text)):
        for start in range(len(text) - repeat):
            for end in range(repeat + 1, len(text) + 1):
                if len(text[start:end]) == repeat + 1:
                    yield text[start:end]


a = all_variants("abcde")
for i in a:
    print(i)