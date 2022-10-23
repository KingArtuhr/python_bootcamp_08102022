min_likes = 500
min_shares = 100

num_likes = 1300
num_shares = 101

if num_likes > min_likes and num_shares > min_shares:
    print("dzień dobry mamy dla państwa zniżkę 10%")
else:
    print("przepraszamy ale ceny są regulare")

is_pizza_order = False
is_large_drink_order = False
is_weekend = True

if (is_pizza_order or is_large_drink_order) and not is_weekend:
    print("dostajesz kupon na darbowego burgera")
else:
    print("nie ma promocji")


disk_size = 143
disk_size_used = 133
file_size = 10

if disk_size - disk_size_used >= file_size:
    print("file can be downloaded")
else:
    print("there is not enough space to download the file")