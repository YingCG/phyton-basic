some_meaning = {
    "Oh, ok" : "I thought you and I were on the same page. I thoought you understand me, but you don't",
    "Home" : "Where I can be ugly in peace",
    "I'm on my way": "I'm just getting dressed",
    "Etc": "End of thinking capacity."
    }


print(some_meaning["Home"])
some_meaning["Loop"] = "Keep going! Keep going! Keep going! ..."
print(some_meaning)

# to loop through
for key in some_meaning:
    print(key)
    print(some_meaning[key])