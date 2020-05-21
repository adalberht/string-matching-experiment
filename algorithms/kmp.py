from typing import List, Optional

# Membuat tabel LSP (Longest Suffix Prefix) untuk string [pattern] yang diberikan.
def build_longest_suffix_prefix_table(pattern: str) -> List[int]:
   table: List[int] = [0]
   for i in range(1, len(pattern)):
       j = table[-1]
       while j > 0 and pattern[i] != pattern[j]:
           j = table[j - 1]
       if pattern[i] == pattern[j]:
           j += 1
       table.append(j)
   return table

# Mencari kemunculan-kemunculan string [pattern] pada string [text] dengan menggunakan algoritma Knuth-Morris-Pratt.
# Apabila [pattern] tidak ditemukan pada [text], fungsi ini akan mengembalikan list kosong.
# Apabila [pattern] ditemukan, fungsi ini akan mengembalikan list seluruh kemunculan [pattern] pada [text]
def kmp_match(pattern: str, text: str) -> Optional[List[int]]:
   lsp_table: List[int] = build_longest_suffix_prefix_table(pattern) # Konstruksi tabel LSP terlebih dahulu
   results, j = [], 0 # Inisialisasi variabel
   for i, c in enumerate(text):
       while j > 0 and c != pattern[j]:
           j = lsp_table[j - 1]  # Fallback dengan menggunakan lsp_table
       if c == pattern[j]:
           j += 1
           if j == len(pattern):
               results.append(i - j + 1)
               j = 0
   return results
