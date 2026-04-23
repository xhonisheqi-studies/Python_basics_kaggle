# help(round)
# 


def least_difference(param1,param2,param3):
    diff_one = abs(param1 - param2)
    diff_two = abs(param2 - param3)
    diff_three = abs(param1 - param3)

    return(diff_one,diff_two,diff_three)

print(
    least_difference(1,100,20000),
    least_difference(1,191,10),
    least_difference(1,10,10),
    least_difference(5,6,7)
)