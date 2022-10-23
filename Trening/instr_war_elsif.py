min_likes = 500
min_shares = 100

num_likes = 1000
num_shares = 99


if num_likes >= min_likes and num_shares >= min_shares:
    print("promcja 10%")
elif num_likes < min_likes and num_shares >= min_shares:
    print("brakuje likeów")
else:
    print("brakuje udostepnień")
