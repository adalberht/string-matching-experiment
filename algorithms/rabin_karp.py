# Referensi:
# Implementasi pseudocode algoritma Rabin-Karp berdasarkan buku
# Introduction to Algorithms (CLRS)
def rabin_karp_match(pattern, text, d = 10, q = 13): 
    m = len(pattern) 
    n = len(text) 
    i = 0
    j = 0
    p = 0 
    t = 0 
    h = 1

    result = []
    for i in range(m-1): 
        h = (h*d)%q 

    for i in range(m): 
        p = (d*p + ord(pattern[i]))%q 
        t = (d*t + ord(text[i]))%q 

    for i in range(n-m+1): 
        if p==t: 
            for j in range(m): 
                if text[i+j] != pattern[j]: 
                    break

            j+=1
            if j==m: 
                result.append(i)

        if i < n-m: 
            t = (d*(t-ord(text[i])*h) + ord(text[i+m]))%q 

            if t < 0: 
                t = t+q 

    return result
