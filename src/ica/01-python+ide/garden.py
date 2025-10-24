bed_len = 10
bed_width = 2

bed_len_inches = bed_len * 12
bed_width_inches = bed_width * 12

flower_spacing = 6

num_cols = bed_len_inches // flower_spacing
num_rows = bed_width_inches // flower_spacing

total_flowers = int(num_cols * num_rows)

print("Number of rows:", num_rows)
print("Number of cols:", num_cols)
print("Total flowers:", total_flowers)