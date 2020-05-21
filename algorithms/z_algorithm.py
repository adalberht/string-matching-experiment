# Referensi:
# Implementasi algoritma Z berdasarkan referensi paper [2] dan [6]

from typing import List, Optional

def konstruksi_z_values(S: str):
    n = len(S)
    Z = [0 for _ in range(n)]
    L, R = 0, 0
    for k in range(1, n):
        if k > R:
            L, R = k, k
            while R < n and S[R-L] == S[R]: R += 1
            Z[k] = R - L
            R -= 1
        else:
            k_aksen = k - L
            if (Z[k_aksen] < R - k + 1):
                Z[k] = Z[k_aksen]
            else:
                L = k
                while R < n and S[R-L] == S[R]: R += 1
                Z[k] = R - L
                R -= 1
    return Z


def z_match(pattern: str, text: str) -> List[int]:
    S = pattern + '$' + text
    Z = konstruksi_z_values(S)
    return [
        i - len(pattern) - 1 for i in range(len(pattern) + 1, len(S)) if Z[i] == len(pattern)
    ]
