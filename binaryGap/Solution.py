def solution(n):
    bin_list = list("{0:b}".format(n).strip(' '))
    max_zeros = 0

    for b in range(len(bin_list)-1):
        if bin_list[b] == '1' and bin_list[b + 1] == '0':
            zeros = 1
            for c in range(b+2, len(bin_list)):
                if bin_list[c] == '0':
                    zeros = zeros + 1
                else:
                    if max_zeros < zeros and bin_list[c] == '1':
                        max_zeros = zeros
                    break
    return max_zeros


class Solution:
    pass
