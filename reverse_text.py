"""
The code is not related to ProgContest problems which were introduced in README.md
I just try a string reversing problem (http://japanese.joelonsoftware.com/Articles/Interviewing.html) in Python
e.g. 
Input: "hello world"
Output: "dlrow olleh"
"""
str_list = list(input())
str_len = len(str_list)
for i in range(int(str_len / 2)):
    tmp_char = str_list[i]
    str_list[i] = str_list[str_len - i - 1]
    str_list[str_len - i - 1] = tmp_char

print("".join(str_list))