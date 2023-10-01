s = "Jatin is a good boy"

with open("first_file.txt", "w") as f:
    f.write(s)

with open("first_file.txt", "a") as fa:
    fa.write("This will append")

with open("first_file.txt", "r") as fp:
    r = fp.read()
    print(r)