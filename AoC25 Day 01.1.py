import csv
import time
import sys
import re

#Start Performance Counter
startTime = time.perf_counter()

def read_csv_file(file_path):
    data_list = []

    try:
        with open(file_path, mode = 'r', encoding = 'utf-8-sig') as csv_file:
            csv_reader = csv.reader(csv_file)

            for row in csv_reader:
                data_list.append(str(row)[2:-2])

        return data_list

    except FileNoteFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

csv_file_path = 'AoC25 Day 01.csv'
data = read_csv_file(csv_file_path)

def rotation_value(data_row):
    rotation_direction = 0
    rotation_value_total = 0
    rotation_value_net = 0

    #Determine direction of rotation
    if data_row[0]== 'L':
        rotation_direction = -1
    elif data_row[0] == 'R':
        rotation_direction = 1
    else:
        rotation_direction = 0

    #Get the total rotation value
    rotation_value_total = int(row[-(len(row)-1):])

    #Calculate the net change on the dial since 100 turns returns to the start
    rotation_value_net = (rotation_value_total % 100) * rotation_direction
    
    return rotation_value_net

def count_rotations(data_row):
    rotation_value_total = 0
    rotation_value_net = 0

    #Get the total rotation value
    rotation_value_total = int(row[-(len(row)-1):])

    full_rotations = rotation_value_total // 100
    return full_rotations

#Part 1
dial_position = 50
current_rotation = 0
counter = 0

for row in data:
    current_rotation = rotation_value(row)
    dial_position = (dial_position + current_rotation) % 100
    #print(dial_position)
    print(f"row = {row}, rotation_value = {current_rotation}, current dial_position = {dial_position}")
    if dial_position == 0:
        counter += 1
        
print(counter)

#Part 2
dial_position = 50
current_rotation = 0
counter = 0
bonus_rotations = 0

for row in data:
    bonus_rotations = count_rotations(row)
    counter += bonus_rotations

    current_rotation = rotation_value(row)
    if dial_position + current_rotation < 0 and dial_position > 0:
        counter += 1
    elif dial_position + current_rotation > 100:
        counter += 1

    dial_position = (dial_position + current_rotation) % 100

    #print(dial_position)
    print(f"row = {row}, rotation_value = {current_rotation}, current dial_position = {dial_position}")
    if dial_position == 0:
        counter += 1

print(counter)

#Print Performance Time
print(f"Time elapsed: {(time.perf_counter() - startTime)}s", file=sys.stderr)
