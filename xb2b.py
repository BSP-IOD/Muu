print("""
                 Muu
             Release V3.0
             
                XB2B
""")

print("1. Kilobytes (KB) to Bytes.")
print("2. Megabytes (MB) to Bytes.")
choice = input("Select (1/2): ")
print("")

if choice == '1':
    kb = float(input("Enter amount of KB: "))
    bytes_val = kb * 1024
    print(f"{kb} KB converted to bytes: {bytes_val:,.0f}.")

elif choice == '2':
    mb = float(input("Enter amount of MB: "))
    bytes_val = mb * 1024 * 1024
    print(f"{mb} MB converted to bytes: {bytes_val:,.0f}.")

else:
    print("Error.")
