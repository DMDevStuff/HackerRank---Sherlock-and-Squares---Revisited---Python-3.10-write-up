##    https://www.hackerrank.com/challenges/sherlock-and-squares/problem

##    Watson likes to challenge Sherlock's math ability. He will provide a
##    starting and ending value that describe a range of integers, inclusive
##    of the endpoints. Sherlock must determine the number of square integers
##    within that range.

##### ##### ##### #####

#   changed given variable names

#   a => start_int
#   b => end_int

##### ##### ##### #####

#   O(1)
#   The Idea:
#       The root of any integer found in a given range of integers a through b,
#       will by definition be >= the square root of a,
#       and <= the square root of b.
#       Therefore the number of integer roots found will be the absolute
#       difference between the last integer root and the first integer root, plus one.

#   Algo:
#       1. Find the square root of start_int.
#       2. Round the result from step one up.
#           If start_int is a perfect square then nothing changes.
#           If start_int is not a perfect square then rounding up
#           finds the first integer root (which is what we are looking for).
#       3. Find the square root of end_int.
#       4. Round the result from step three down.
#           If end_int is a perfect square then nothing changes.
#           if end_int is not a perfect square then rounding down
#           finds the last integer root (which is what we are looking for.)
#       5. Return last integer root - first integer root + 1

def squares(start_int, end_int):
    
    first_root = math.ceil(math.sqrt(start_int))
    last_root = math.floor(math.sqrt(end_int))
    
    return last_root - first_root + 1
