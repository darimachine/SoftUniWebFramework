MALE = 'Male'
FEMALE = 'Female'
DO_NOT_SHOW = 'Do not show'
GENDERS = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]
value_max= max(len(gender) for gender,gen in GENDERS)
print(value_max)