#implement a recursive function ti calculate the factorial of agiven number


def fact_rec(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * fact_rec(n - 1)


number = 4
res = fact_rec(number)

print("the factorial of {}is{}.".format(number, res))
