import numpy as np

class Job:
    def __init__(self, arrival_time, service_time, priority):
        self.arrival_time = arrival_time
        self.service_time = service_time
        self.priority = priority

def generate_exponential_xi(n, lmbda):
    y = np.random.uniform(0, 1, n)
    x = [-np.log(1 - y[i]) / lmbda for i in range(len(y))]
    return x

def generate_si_sigma_xi(n):
    n_sorted = sorted(n)
    si_sigma_xi = []
    for i in range(len(n_sorted)):
        si_sigma_xi.append(sum(n_sorted[:i+1]))
    return si_sigma_xi

def generate_sizes(si_sigma_xi, mu):
    sizes = generate_exponential_xi(len(si_sigma_xi), mu)
    jobs = []
    for i in range(len(si_sigma_xi)):
        jobs.append(Job(si_sigma_xi[i], sizes[i], None))
    return jobs

def assign_priority(jobsArray, number_of_queues, average_service_time):
    bin_size = 2 * average_service_time / number_of_queues
    for job in jobsArray:
        priority = int(job.service_time / bin_size)
        if priority >= number_of_queues:
            priority = number_of_queues - 1
        job.priority = priority
    return jobsArray

def main():
    # number of jobs
    n = 100
    number_of_queues = 4
    lmbda = 10
    mu = 0.2

    xi = generate_exponential_xi(n, lmbda)
    si_sigma_xi = generate_si_sigma_xi(xi)

    jobsArray = generate_sizes(si_sigma_xi, mu)

    jobsArray = assign_priority(jobsArray, number_of_queues, 1/mu)

    # Count number of jobs in each queue
    count = [0] * number_of_queues
    for job in jobsArray:
        count[job.priority] += 1
    print("Counts per priority:", count)
    
    print("Jobs:")
    for job in jobsArray:
        print("Arrival Time:", job.arrival_time, "Service Time:", job.service_time, "Priority:", job.priority)


if __name__ == "__main__":
    main()
