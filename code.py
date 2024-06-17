#!/usr/bin/env python3

def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()

    lines = sorted((int(line.split()[0]), line.split()[1]) for line in lines)

    message = []
    counter = 1
    sum_counter = 1

    for number, word in lines:
        if number == sum_counter:
            message.append(word)
            counter += 1
            sum_counter += counter

    return ' '.join(message)

print(decode('input.txt'))