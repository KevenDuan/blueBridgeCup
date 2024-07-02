mod = 10**9 + 7
print((pow(2023, 2023, mod) - (pow(2023, 2023, mod) * pow(7, mod - 2, mod)) % mod - 
       (pow(2023, 2023, mod) * pow(17, mod - 2, mod)) % mod + (pow(2023, 2023, mod) * pow(7 * 17, mod - 2, mod)) % mod) % mod) 