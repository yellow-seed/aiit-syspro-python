d = { "alice": 3, "bob": 5, "dave": 4, "victor": 10}

sorted_dict = sorted(d.items(), key=lambda x:x[1], reverse=True)

for(k, v) in sorted_dict:
    print(k, "->", v)