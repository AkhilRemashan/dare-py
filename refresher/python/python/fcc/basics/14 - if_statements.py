
is_male = True
is_tall = True

# Normal

# if is_male:
#     print("You ar a male")
# else:
#     print("You are not a male")

# OR Operator

# if is_male or is_tall:
# #     print("You ar a male or tall or both")
# # else:
# #     print("You neither male nor tall")

# AND Operator

# if is_male and is_tall:
#     print("You ar a tall male")
# else:
#     print("You neither male or tall or both")

# ELSEIF and not()

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_male):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but tall")
else:
    print("You are either not male and not tall")


