import matplotlib.pyplot as plt

f = open("corona_data.csv", "r")

data = f.readlines()
us_indexes = []
for i in range(len(data)):
    if data[i].find("***** USA *****") != -1:
        us_indexes.append(i)

print(us_indexes)
print(data[us_indexes[0] + 1].split()[1])

state_confirmed_data = {}

for i in range(len(us_indexes)):
    line_num = us_indexes[i] + 3
    line = data[line_num]
    while line != "\n":
        if line.split("\t")[0].strip() not in state_confirmed_data:
            state_confirmed_data[line.split("\t")[0].strip()] = []
        state_confirmed_data[line.split("\t")[0].strip()].append(int(line.split("\t")[1].strip().replace(",", "")))

        line_num += 1
        line = data[line_num]
for pair in state_confirmed_data:
    print(pair, state_confirmed_data[pair])
f.close()
for pair in state_confirmed_data:
    plt.plot(state_confirmed_data[pair])
plt.show()