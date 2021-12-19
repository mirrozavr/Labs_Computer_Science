import matplotlib.pyplot as plt

X = []
Y = []
with open('001.dat', 'r') as f:
    N = f.read().split()
    print(N)
n = int(N[0])

for i in range(1, 2 * n + 1, 2):
    X.append(float(N[i]))
    Y.append(float(N[i + 1]))

if max(X) + abs(min(X)) >= max(Y) + abs(min(Y)):
    x = abs((max(X) + abs(min(X))) / (max(Y) + abs(min(Y))))
    y = 1
else:
    x = 1
    y = abs((max(Y) + abs(min(Y))) / (max(X) + abs(min(X))))

plt.figure(figsize=(int(5 * x), int(5 * y)))
plt.plot(X, Y, "mo")
plt.show()