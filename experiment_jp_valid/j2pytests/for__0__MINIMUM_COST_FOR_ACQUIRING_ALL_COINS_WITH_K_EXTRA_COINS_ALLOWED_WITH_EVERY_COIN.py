# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
import math

def f_gold ( coin , n , k ) :
    coin.sort ( )
    coins_needed = math.ceil ( 1.0 * n // ( k + 1 ) ) ;
    ans = 0
    for i in range ( coins_needed - 1 + 1 ) :
        ans += coin [ i ]
    return ans


#TOFILL
def f_filled (coin, n, k):
    """ generated source for method minCost """
    Arrays.sort(coin)
    coins_needed = (Math.ceil(1.0 * n / (k + 1)))
    ans = 0
    return ans



if __name__ == '__main__':
    param = [
    ([2, 4, 5, 9, 10, 10, 11, 14, 15, 19, 21, 22, 29, 36, 36, 38, 39, 39, 39, 41, 41, 42, 45, 45, 48, 55, 56, 57, 64, 66, 66, 66, 66, 69, 74, 76, 80, 81, 82, 82, 85, 87, 95, 95],33,27,),
    ([-6, -52, 20, -98, -10, 48, 36, 66, -88, 94, 68, 16],6,10,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],16,16,),
    ([91, 62, 29, 49, 6, 11, 10, 43, 78, 35, 32, 5, 1, 48, 15, 24, 4, 71],13,17,),
    ([-98, -92, -88, -84, -82, -78, -74, -74, -68, -62, -62, -56, -56, -50, -46, -44, -26, -18, -14, -8, -8, -6, 8, 16, 20, 20, 22, 26, 36, 42, 44, 44, 52, 60, 66, 68, 68, 70, 76, 84],25,34,),
    ([1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0],32,32,),
    ([5, 12, 38, 39, 52, 54, 62, 81, 87, 93],6,8,),
    ([86, -18, -32, 70, 40, -76, -8, 8, -84, -10, 92, 94, -18, -12, -26, -40, -74, 60, 16, -70, 44, -32, 40, -24, 0, 4],25,20,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],37,29,),
    ([86, 62, 98, 97, 61, 31, 23, 56, 63, 72, 44, 74, 58, 97],12,13,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))