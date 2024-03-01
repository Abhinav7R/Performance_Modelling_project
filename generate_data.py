import numpy as np

# number of jobs
n = 100
number_of_queues = 4
lmbda = 0.1
mu = 0.2

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


xi = generate_exponential_xi(n, lmbda)
si_sigma_xi = generate_si_sigma_xi(xi)
jobsArray = generate_sizes(si_sigma_xi, mu)
jobsArray = assign_priority(jobsArray, number_of_queues, 1/mu)    

# for i in range(len(jobsArray)):
    # print(jobsArray[i].arrival_time, jobsArray[i].service_time, jobsArray[i].priority, end='\n')    

#write to a csv file
import csv
with open('jobs.csv', mode='w') as jobs_file:
    jobs_writer = csv.writer(jobs_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    jobs_writer.writerow(['arrival_time', 'service_time', 'priority'])
    for job in jobsArray:
        jobs_writer.writerow([job.arrival_time, job.service_time, job.priority])
