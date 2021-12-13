
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                                               #
# instruction:
#         first input: activaion code
#          second input:  current holding value
# 
#     activaton codes:
#        Converts Degree Celcius to Kelvin in input: 1
#        Converts kelvin to degree celcius:                2
#        Converts degree celcius to Farenheit :         3
#        Converts Farenheit to kelvin:                         4
#
#
#eg: stdin:    1
#                    45
# here 45°C converts to 318.15 K
#
#                                                                                                #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #






print("Which one you need\n Celcius to kelvin (1),\n kelvin to Celcius(2)\n Celcius to Farenheit(3)\n Farenheit to kelvin(4) \n\"Type the associated number to run required function\"")
math= input()
if (math=="1"):
    print(" Degree Celsius to Kelvin calc")
    dc_k = float(input(" Degree Celsius:"))
    kfrdc= dc_k+273.15  #Kelvin from celcius
    print("\n In kelvin :")
    print(kfrdc)
if (math=="2"):
    print(" Kelvin to Degree Celcius calc")
    k_dc =float(input(" Kelvin:"))
    dc_frk= k_dc-273.15 #celcius from kelvin
    print("\n In celcius:")
    print(dc_frk) 
if (math=="3"):
    print(" Degree Celcius to Farenheit calc")  #(1°C × 9/5) + 32 = 33.8°F
    dc_df = float(input("Degree Celsius:"))
    df_frdc= (dc_df*9/5)+32 #farenheit from celcius 
    print("\n In farenheit :")
    print(df_frdc)
if (math=="4"):
    print(" Farenheit to Degree celcius calc")
    df_dc = float(input(" Farenheit: "))
    dc_frdf =(df_dc-32)*5/9 #    Celcius from farenheit
    print("\n In farenheit:")
    print(dc_frdf)
