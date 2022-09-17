
for i in range(12, 120):
    # 12 is the sine of which num table user wants
    # 120 is the ending number of the given table
    with open("Ch9_Que3_tables.txt", "w") as f:
        for j in range(1, 11):
            # 1 is the starting number of the table
            # 11 is the times of multiplying of the table
            f.write(f"{i}*{j}={i*j}\n")
    break
