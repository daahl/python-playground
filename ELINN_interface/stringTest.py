statusString = "sf1:1,sf2:0"

split1 = statusString.split(",")

print(split1)

for s in split1:
    print(s.split(":"))