def solution(s, skip, index):
    def get_next_ord(ord):
        while True:
            ord = (ord - 96) % 26 + 97

            if chr(ord) not in skip:
                return ord

    encrypt_dict = {}

    for i in range(97, 123):
        j = get_next_ord(i)

        for _ in range(1, index):
            j = get_next_ord(j)

        encrypt_dict[chr(i)] = chr(j)

    result = ""

    for idx in range(len(s)):
        result += encrypt_dict[s[idx]]

    return result
