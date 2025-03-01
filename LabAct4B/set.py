# Our Sets
A = {'a', 'b' , 'c', 'd' , 'f' , 'g'}
B = {'c', 'b', 'h', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'h', 'i', 'j', 'k'}

# 1.
# a. How many elements are there in set A and B
elementsTotal = len(A) + len(B);
print("Total number of elements in set A and B: " + str(elementsTotal))
# b. How many elements are there in B that is not part of A and C
elementsB = B - (A | C)  
elementCntr = len(elementsB)
print("Total number of elements in set B that is not part of A and C is: " + str(elementCntr))  

# c. Show the following using set operations
# & FOR INTERSECTION, - TO MINUS OR REMOVE A CERTAIN SET, | IS THE UNION, sorted() to sort it from a - z
# i. [h, i, j, k]
print(sorted(C - A))
# ii. [c, d, f]
print(sorted(A & C))
# iii. [b, c, h]
print(sorted((A & B) | (B & C)))
# iv. [d, f]
print(sorted(A & C - B))
# v. [c]
print(sorted(A & B & C))
# vi. [l, m, o]
print(sorted(B - (A | C)))


# 2.
exchange_rates = {
"EUR": 0.931936166,
"GBP": 0.827816452,
"JPY": 131.1994943,
"AUD": 1.439773864,
"CHF": 0.920289009,
"CAD": 1.342307659,
"NZD": 1.583390808,
"TRY": 18.83402666,
"NGN": 460.386436,
"KGS": 86.20468637,
"MGA": 4304.101563,
"SRD": 32.59911243,
"GHS": 12.17177575,
"CUP": 1,
"NOK": 10.29227611,
"QAR": 3.647456564,
"CZK": 22.15119887,
"HRK": 7.362267938,
"RSD": 108.5081368,
"NIO": 36.54560531,
"SBD": 8.41428026,
"MWK": 1026.169965,
"YER": 250.1646044,
"VES": 23.11957702,
"BDT": 105.5535749,
"RON": 4.561702839,
"DZD": 136.0870755,
"ARS": 189.5406395,
"STN": 23.0151436,
"BIF": 2075.047081,
"MMK": 2099.761791,
"MUR": 45.3436214,
"AED": 3.672925821,
"IDR": 15094.62702,
"MXN": 18.93036821,
"UAH": 36.47194942,
"CRC": 582.3070036,
"BZD": 2.015272062,
"GNF": 8608.203125,
"SZL": 17.51748808,
"SOS": 568.3301096,
"INR": 82.61621692,
"NPR": 132.2230022,
"XAF": 611.4472661,
"AZN": 1.696962033,
"PYG": 7285.404817,
"GYD": 210.9510362,
"RWF": 1084.498031,
"ERN": 15.07318741,
"WST": 2.691706364,
"BRL": 5.197907606,
"LKR": 366.2309244,
"TND": 3.06595472,
"VND": 23535.7878,
"IQD": 1459.94509,
"AFN": 90.1474709,
"NAD": 17.51748808,
"SYP": 2448.555556,
"MOP": 8.082523382,
"BAM": 1.823726569,
"DKK": 6.931756629,
"PKR": 268.4966324,
"BGN": 1.821637812,
"RUB": 73.13025012,
"TMT": 3.499199157,
"SVC": 8.753525323,
"XCD": 2.705752348,
"LAK": 16822.1374,
"GTQ": 7.840953567,
"SAR": 3.752211266,
"PLN": 4.412868592,
"GIP": 0.828083251,
"GEL": 2.650753558,
"MKD": 57.30296175,
"AWG": 1.809871879,
"AOA": 512.4883721,
"MVR": 15.45371669,
"BHD": 0.376643982,
"EGP": 30.36480984,
"KRW": 1260.46907,
"MRO": 36.02010686,
"COP": 4746.429423,
"BBD": 2.018594852,
"DJF": 177.9832815,
"HNL": 24.64988814,
"KES": 124.8661359,
"HKD": 7.848810813,
"MAD": 10.22720501,
"ZAR": 17.71922356,
"MDL": 18.7962013,
"PAB": 1,
"FJD": 2.201278594,
"CDF": 2074.070588,
"MZN": 64.24781341,
"UGX": 3672.833333,
"KWD": 0.305557504,
"THB": 33.40043917,
"TWD": 30.0665132,
"IRR": 41997.79068,
"BOB": 6.884075235,
"LRD": 156.8469751,
"SDG": 565.0512821,
"TOP": 2.380319723,
"VUV": 121.4193228,
"OMR": 0.38471052,
"ILS": 3.482745868,
"PEN": 3.854426226,
"UZS": 11278.03328,
"ETB": 53.68331303,
"TTD": 6.777487314,
"PGK": 3.52422837,
"BWP": 12.92492669,
"SEK": 10.58459208,
"SGD": 1.325506488,
"HUF": 361.7082622,
"BYN": 2.786552647,
"TJS": 10.29429222,
"GMD": 63.2338594,
"CVE": 102.9766355,
"ZMW": 19.22110772,
"KHR": 4096.096654,
"DOP": 56.40700086,
"CNY": 6.787890099,
"ISK": 141.0981925,
"LYD": 4.781245694,
"CLP": 796.7962659,
"BSD": 1,
"XPF": 110.9561452,
"ALL": 107.9662927,
"SCR": 13.61569354,
"ANG": 1.795903979,
"LBP": 4634.156998,
"MYR": 4.292053266,
"KZT": 455.4250399,
"HTG": 150.619352,
"BND": 1.323344843,
"KMF": 460.7359398,
"LSL": 17.51748808,
"TZS": 2336.903499,
"JOD": 0.709595406,
"PHP": 54.81472581,
"XOF": 611.3128462,
"AMD": 395.6927535,
"UYU": 39.19277801,
"JMD": 154.645614,
"SSP": 741.986532,
"MRU": 36.36468647,
"MNT": 3506.284805
}

dollar = float(input("How much dollar do you have? "))
currency = input("What currency you want to have? ").upper()

print("\nDollar:", dollar, "USD")

if currency in exchange_rates:
    converted_amount = dollar * exchange_rates[currency]
    print(currency + ":", converted_amount)
else:
    print("Please input the correct currency.")