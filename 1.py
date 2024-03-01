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

def generate_sizes(si_sigma_xi, mu):
    sizes = generate_exponential_xi(len(si_sigma_xi), mu)
    # print(sizes)
    return [(si_sigma_xi[i], sizes[i]) for i in range(len(si_sigma_xi))]

def assign_priority(arrival_times_and_sizes, number_of_queues, average_service_time):
    bin_size = 2 * average_service_time / number_of_queues
    arrival_times_and_service_times_and_priority = []
    for i in range(len(arrival_times_and_sizes)):
        priority = int(arrival_times_and_sizes[i][1] / bin_size)
        if priority >= number_of_queues:
            priority = number_of_queues - 1
        arrival_times_and_service_times_and_priority.append((arrival_times_and_sizes[i][0], arrival_times_and_sizes[i][1], priority))
    return arrival_times_and_service_times_and_priority

def simulate_queue(arrival_times_and_priority):
    pass

def main():
    #number of jobs
    n = 100
    number_of_queues = 4
    lmbda = 10
    mu = 0.2

    xi= generate_exponential_xi(n, lmbda)
    # print(xi)
    #basically the arrival times of the jobs in the queue
    si_sigma_xi = generate_si_sigma_xi(xi)
    # print(si_sigma_xi)

    #append random sizes to all the jobs in the queue
    #list of tuples (arrival time, size)
    #sizes are between 1 and 10
    arrival_times_and_sizes = generate_sizes(si_sigma_xi, mu)
    # print(arrival_times_and_sizes)
    #Note service time is same as sizes
    arrival_times_and_service_times_and_priority = assign_priority(arrival_times_and_sizes, number_of_queues, 1/mu)
    # print(arrival_times_and_service_times_and_priority)    

    #count number of jobs in each queue
    count = [0,0,0,0]
    for i in range(len(arrival_times_and_service_times_and_priority)):
        count[arrival_times_and_service_times_and_priority[i][2]] += 1
    print(count)

    #simulate the queue with the given arrival times and sizes using sjf
    # simulate_queue(arrival_times_and_service_times_and_priority)

if __name__ == "__main__":
    main()
