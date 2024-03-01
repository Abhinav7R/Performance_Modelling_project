import numpy as np

def generate_exponential_xi(n, lmbda):
    y = np.random.uniform(0, 1, n)
    x = [-np.log(1 - y[i]) / lmbda for i in range(len(y))]
    return x

def generate_si_sigma_xi(n):
    n_sorted = sorted(n)
    si_signma_xi = []
    for i in range(len(n_sorted)):
        si_signma_xi.append(sum(n_sorted[:i+1]))
    return si_signma_xi

def generate_sizes(si_sigma_xi):
    sizes = np.random.randint(1, 10, len(si_sigma_xi))
    print(sizes)
    return [(si_sigma_xi[i], sizes[i]) for i in range(len(si_sigma_xi))]

def main():
    xi= generate_exponential_xi(10, 1)
    print(xi)
    #basically the arrival times of the jobs in the queue
    si_sigma_xi = generate_si_sigma_xi(xi)
    print(si_sigma_xi)
    #append random sizes to all the jobs in the queue
    #list of tuples (arrival time, size)
    arrival_times_sizes = generate_sizes(si_sigma_xi)
    print(arrival_times_sizes)

if __name__ == "__main__":
    main()
