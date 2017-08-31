import numpy             as np
import matplotlib.pyplot as plt

max_people = 100 # max people to take into account
max_it     = int(10e4) # max number of iterations each loop
year       = 365 # days
res        = np.zeros(max_people)

acum       = [[],[]]
coinc      = [[],[],[],[],[],[],[],[],[],[]]

for people in range(1,max_people):

    bdays     = np.sort(np.random.randint(1, 366, [max_it, people]))
    dif       = people-np.array(list(map(len, np.array(list(map( np.unique, bdays))))))
    acum[0]  += list([people]*max_it)
    acum[1]  += list(dif)
    coinc[0] += [people]
    coinc[1] += [(max_it-len(dif[dif<1]))/max_it]
    coinc[2] += [(max_it-len(dif[dif<2]))/max_it]
    coinc[3] += [(max_it-len(dif[dif<3]))/max_it]
    coinc[4] += [(max_it-len(dif[dif<4]))/max_it]
    coinc[5] += [(max_it-len(dif[dif<5]))/max_it]
    coinc[6] += [(max_it-len(dif[dif<6]))/max_it]
    coinc[7] += [(max_it-len(dif[dif<7]))/max_it]
    coinc[8] += [(max_it-len(dif[dif<8]))/max_it]
    coinc[9] += [(max_it-len(dif[dif<9]))/max_it]

plt.figure()
plt.hist2d(acum[0], acum[1], [500, 100])
plt.show()

plt.figure()
plt.plot(coinc[0], coinc[1],label='1')
plt.plot(coinc[0], coinc[2],label='2')
plt.plot(coinc[0], coinc[3],label='3')
plt.plot(coinc[0], coinc[4],label='4')
plt.plot(coinc[0], coinc[5],label='5')
plt.plot(coinc[0], coinc[6],label='6')
plt.plot(coinc[0], coinc[7],label='7')
plt.plot(coinc[0], coinc[8],label='8')
plt.plot(coinc[0], coinc[9],label='9')
plt.legend()
plt.show()
