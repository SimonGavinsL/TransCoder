# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
import math

def f_gold ( a , n ) :
    return ( - 1 + int ( math.sqrt ( 1 + ( 8 * n ) ) ) ) // 2


#TOFILL
def f_filled ( a , n ) :
    return int ( math.floor ( ( - 1 + math.sqrt ( 1 + ( 8 * n ) ) ) ) / 2 )


if __name__ == '__main__':
    param = [
    ([1, 2, 2, 3, 5, 6, 7, 8, 8, 12, 15, 16, 18, 18, 20, 21, 21, 22, 22, 24, 24, 25, 30, 35, 42, 49, 52, 55, 55, 63, 68, 70, 72, 73, 77, 80, 83, 87, 87, 88, 88, 94, 95, 97],22,),
    ([48, -72, 84, -24, 28, 94, 36, 28, 32, 66, -62, 64, 6, -68, -12, 46, 4, 98, 18, 86, -60, 76, 14, 98],12,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],25,),
    ([11, 16, 84, 8, 86, 44, 79, 11, 73, 12, 29, 62, 22, 44, 28, 8, 48, 92, 73, 63, 59, 44, 95, 66],14,),
    ([-94, -94, -92, -88, -86, -82, -80, -80, -78, -76, -56, -56, -50, -44, -42, -36, -36, -32, -32, -26, -14, -12, -6, 12, 24, 28, 34, 38, 42, 42, 46, 50, 56, 62, 62, 74, 84, 92, 94],19,),
    ([0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0],24,),
    ([2, 2, 3, 3, 3, 4, 5, 13, 16, 18, 21, 22, 27, 28, 32, 34, 36, 37, 41, 42, 43, 51, 52, 52, 54, 54, 61, 65, 67, 67, 68, 71, 75, 77, 77, 78, 80, 81, 81, 84, 86, 90, 90, 93, 93, 94, 99, 99],31,),
    ([54, -86],1,),
    ([0, 1],1,),
    ([5, 54, 49, 80, 56, 62, 31, 49, 60, 19, 45, 94, 33, 46, 32],8,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))