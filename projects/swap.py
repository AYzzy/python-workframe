# def first_string():
#     return 'abc'
#
#
# def second_string():
#     return 'xyz'
#
#
# def swap_the_last_index_from_first_string():
#     new_string = second_string()[2::-2] + first_string()[-1:]
#     return new_string
#
#
# def swap_the_last_index_from_second_string():
#     new_string2 = first_string() + second_string()[-1]
#     return new_string2
#
#
# def remove_the_third_index_from_new_string(new_string='abcz'):
#     temp = new_string[len(new_string) - 2::2]
#

def swap1():
    return 'abc'

def swap2():
    return 'xyz'
def main():
    answer1 = swap1[0] + swap1[1] + swap2[2]
    answer2 = swap2[0] + swap2[1] + swap1[2]
    return answer1, answer2