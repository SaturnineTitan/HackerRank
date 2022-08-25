regex_integer_in_range = r"^[1-9][\d]{5}$"	# Check range of given integer 

regex_alternating_repetitive_digit_pair = r"(?=(\d)\d\1)" # solution 1

regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)" # solution 2
