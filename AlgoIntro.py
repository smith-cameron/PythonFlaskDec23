
# < Create a function that receives an integer and prints/return how many digits it is.
# >  What if...
#// ? - Its negative or positive?
#// ? - Its Zero?
# ? - Is it DRY(what is dry)?
# Stretch Goals
# todo - Refactor for range()
# todo - Refactor using strings
# todo - Refactor using basic conditionals

#! RIOT:

#! R: Restate the problem being solved
#! I: Input (what is the expected input?)
#! O: Output (what is the expected output?)
#! T: Test cases (walk through test cases)

# < when in doubt... print() + rubber duck it with pseudo code

def int_count(input):
    print(f"input value: {input}")
    if input < 0:
        input *= -1
    print(f"input length: {len(str(input))}")

int_count(10.3)

def old_solutions():
  def helper(input):
      if input < 10 and input > -10:
          print("One Digit")
      elif input > 10 and input < 100 or input < -10 and input > -100:
          print("Two Digits")
      else:
          print("i cant count that high... or low")


  def helper2(input):
      # print(input)
      if input in range(9) or input in range(0, -9, -1):
          print("One Digit")
      elif input in range(10, 99) or input in range(-10, -99, -1):
          print("Two Digits")
      else:
          print("i cant count that high... or low")


  def for_loop_helper(input):
      print(abs(input))
      iterable = str(abs(input))
      count = 0
      for iterator in iterable:
          # print(iterator)
          count += 1
      print(f"{count} digits")


  def is_not_zero(num):
      if num > 0:
          print("Positive")
          return True
      elif num < 0:
          print("Negative")
          return True
      else:
          return False


  def digits(num):
      if is_not_zero(num): #true or false
          for_loop_helper(num)
          # helper2(num)
      elif is_not_zero(num):
          for_loop_helper(num)
          # helper2(num)
      else:
          print("Thats Zero")


  digits(77563457634753456)
