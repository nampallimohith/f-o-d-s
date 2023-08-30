from collections import Counter
likes = [120, 250, 80, 180, 300, 120, 200, 150, 80, 250]
like_distribution = Counter(likes)
print("Likes Frequency Distribution:")
for like_count, frequency in like_distribution.items():
    print(f"{like_count} likes: {frequency} posts")
