import numpy as np

jobsArray = []

class Job:
    def __init__(self, arrival_time, service_time, priority):
        self.arrival_time = arrival_time
        self.service_time = service_time
        self.priority = priority
        self.waiting_time = None
        self.isJobDone = False

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

def areJobsLeft(jobsArray):
    for job in jobsArray:
        if job.isJobDone == False:   
            return True
    return False

def getHighestPriorityJob(jobsArray,global_clock):
    index = -1
    priority = 100000
    for i, job in enumerate(jobsArray):
        if job.priority <= priority and global_clock >= job.arrival_time and job.isJobDone == False:
            priority = job.priority
            index = i 
            
    return index

def getNextJobArrival(jobsArray):
    index = -1
    for i, job in enumerate(jobsArray):
        if job.isJobDone == False:
            return i 
            
def simulate_queue(jobsArray,numJobs):
    global_clock = 0
    numJobsdone = 0
    while numJobsdone != numJobs:
        
        highest_priority_job_index = getHighestPriorityJob(jobsArray,global_clock)
        
        if highest_priority_job_index == -1:
            index =  getNextJobArrival(jobsArray)
            global_clock = jobsArray[index].arrival_time
            highest_priority_job_index = index

        currJob = jobsArray[highest_priority_job_index]  
        jobsArray[highest_priority_job_index].waiting_time = global_clock -  jobsArray[highest_priority_job_index].arrival_time
        global_clock += currJob.service_time  
        jobsArray[highest_priority_job_index].isJobDone = True 
        numJobsdone += 1 

def main():
    # number of jobs
    n = 10
    number_of_queues = 4
    lmbda = 0.1
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

    # Simulate the queue with the given arrival times and sizes using sjf
    simulate_queue(jobsArray,n)

    print("Jobs:")
    for job in jobsArray:
        print("Arrival Time:", job.arrival_time, "Service Time:", job.service_time, "Priority:", job.priority, "Waiting Time:", job.waiting_time)


if __name__ == "__main__":
    main()
