#!/usr/bin/env python3


def solve():
    '''Tính số nghiệm của bài toán lớp 3

    Với các biến a,b,c,d,e,f,g,h,i là các số nằm trong khoảng 1-9 (các biến có
    thể có giá trị giống nhau), dạng biểu thức:

      a + 13 * b / c + d + 12 * e – f – 11 + g * h / i – 10 = 66

    Bài toán lớp 3 có số đáp án khổng lồ
    (http://www.familug.org/2015/05/codegolf-giai-bai-toan-lop-3-co-so.html)
    by *****ducnv5*****
    '''

    first_half = []
    full_result = []
    for sum1 in range(5, 87):
        len1 = len([[a, e, d, f]
                    for a in range(1, 10)
                    for d in range(1, 10)
                    for e in range(1, 10)
                    for f in range(1, 10)
                    if a + d + 12 * e - f == sum1])

        if len1 > 0:
            first_half.append([sum1, len1])
    for sum1, len1 in first_half:
        len2 = len([[b, c, g, h, i]
                    for b in range(1, 10)
                    for c in range(1, 10)
                    for g in range(1, 10)
                    for h in range(1, 10)
                    for i in range(1, 10)
                    if c*i*sum1 + i*13*b +
                    c*g*h == 87*c*i])
        if len2 > 0:
            full_result.append([sum1, len1*len2])

    result = sum([i[1] for i in full_result])
    return result


def main():
    print(solve())


if __name__ == "__main__":
    main()
