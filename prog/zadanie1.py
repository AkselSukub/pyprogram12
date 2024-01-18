#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def print_reverse_sequence():
    num = int(input("Введите число: "))
    if num != 0:
        print_reverse_sequence()
    print(num)

print_reverse_sequence()