import csv
import time
import sys
import re

#Start Performance Counter
startTime = time.perf_counter()

data = '194-253,81430782-81451118,7709443-7841298,28377-38007,6841236050-6841305978,2222204551-2222236166,2623-4197,318169-385942,9827-16119,580816-616131,646982-683917,147-181,90-120,3545483464-3545590623,4304-5747,246071-314284,8484833630-8484865127,743942-795868,42-53,1435-2086,50480-60875,16232012-16441905,94275676-94433683,61509567-61686956,3872051-4002614,6918792899-6918944930,77312-106847,282-387,829099-1016957,288251787-288311732,6271381-6313272,9877430-10095488,59-87,161112-224439,851833788-851871307,6638265-6688423,434-624,1-20,26-40,6700-9791,990-1307,73673424-73819233'
test_data = '11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'
ranges = test_data.split(',')

def check_odd_length(range_l, range_r):
    check_val = True
    if len(range_l) == len(range_r):
        if len(range_r) % 2 == 1:
            check_val = False

    return check_val

def adjust_ranges(raw_range):
    range_l_adj = int(raw_range[0])
    range_r_adj = int(raw_range[1])

    if len(raw_range[0]) % 2 == 1:
        range_l_adj = 10 ** (len(raw_range[0]))

    if len(raw_range[1]) % 2 == 1:
        range_r_adj = (10 ** (len(raw_range[1])-1)) - 1

    adj_range = [range_l_adj, range_r_adj]
    return adj_range

def check_count(adj_range):
    char_count_l = int(len(str(adj_range[0])) / 2)
    char_count_r = int(len(str(adj_range[1])) / 2)

    check_l = int(str(adj_range[0])[:char_count_l])
    check_r = int(str(adj_range[1])[:char_count_r])
    
    return [check_l, check_r - check_l + 1]

def get_double_num(single_num):

    return single_num + (single_num * (10 ** (len(str(single_num)))))

#Part 1
print(ranges)
total_sum = 0

for str_range in ranges:
    rangevals = str_range.split('-')
    if check_odd_length(rangevals[0], rangevals[1]) == False:
        print(f"Failed Odd Length Check {rangevals}")
    else:
        adjusted_vals = adjust_ranges(rangevals)
        #print(str_range, adjusted_vals)
        loop_settings = check_count(adjusted_vals)
        for i in range(loop_settings[1]):
            double_num = get_double_num(loop_settings[0] + i)
            #print(loop_settings[0]+i, double_num)
            if double_num >= adjusted_vals[0] and double_num <= adjusted_vals[1]:
                total_sum += double_num
                #print(loop_settings[0]+i, double_num, total_sum, adjusted_vals)
                
            else:
                print(f"Checked num outside bounds {double_num}")
                
print(total_sum)

#Part 2

#Print Performance Time
print(f"Time elapsed: {(time.perf_counter() - startTime)}s", file=sys.stderr)
