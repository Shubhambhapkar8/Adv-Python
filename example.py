# calculate simple intrest
def simple_intrest(p: float|int, n: int, r: float|int) -> tuple:
    """
    p: principle in INR
    n: number of years
    r: rate of intrest in percent per annum
    output intrest amount
    """
    i= (p*n*r)/100
    a = p + i

    return i, a
# Take p, n, r as input from user
p = float(input("Please enter principle in INR : "))
n = int(input("Please enter Number of Years :  "))
r = float(input("Please enter rate of intrest in %p.a. : "))

# Call the simple intrest function
i, a = simple_intrest(p, n, r)

# Print the intrest and amount
print(f"simple Intrest : {i:.2f} INR")
print(f"amount : {a:.2f} INR ")