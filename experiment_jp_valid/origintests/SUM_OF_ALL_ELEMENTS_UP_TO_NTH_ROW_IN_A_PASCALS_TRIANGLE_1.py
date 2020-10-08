# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( n ) :
    sum = 0
    sum = 1 << n ;
    return ( sum - 1 )


#TOFILL
def f_filled ( n ) :
    sum = 0
    sum = 1 << n
    return ( sum - 1 )


if __name__ == '__main__':
    param = [
    (53,),
    (3,),
    (28,),
    (44,),
    (84,),
    (83,),
    (46,),
    (3,),
    (16,),
    (89,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))