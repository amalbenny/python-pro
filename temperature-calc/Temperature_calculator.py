print("Which one you need\n Celcius to Kelvin (1),\n Kelvin to Celcius(2)\n\"Type the associated number to required function\"")
math= input()
if (math=="1"):
    print(" Degree Celsius to Kelvin calc")
    dc_k = float(input(" Degree Celsius:"))
    kfrdc= dc_k+273.15
    print("\n In kelvin :")
    print(kfrdc)
if (math=="2"):
    print(" Kelvin to Degree Celcius calc")
    k_dc =float(input(" Kelvin:"))
    dc_frk= k_dc-273.15
    print("\n In celcius:")
    print(dc_frk)
