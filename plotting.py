import matplotlib.pyplot as plt
def plot_time_for_each_job_barh(jobsArray):
    arrival_times = []
    duration = []
    index = []
    count = 0
    for i in jobsArray:
        arrival_times.append(i.arrival_time)
        duration.append(i.service_time + i.waiting_time)
        index.append(count)
        count += 1
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.barh(index, duration, left=arrival_times, color='skyblue', edgecolor='grey')
    ax.set_xlabel('Time')
    ax.set_title('Arrival and Departure Times')
    plt.grid(True)
    plt.show()

def number_of_jobs_in_system_at_any_time(jobsArray):
    arrival_times = []
    departure = []
    timestamps=[]
    counts = []
    unit_time = 0.25
    time = 0
    for i in jobsArray:
        arrival_times.append(i.arrival_time)
        departure.append(i.arrival_time + i.service_time + i.waiting_time)
    while(time<max(departure)):
        timestamps.append(time)
        arrivals = 0
        departures = 0
        for atime in arrival_times:
            if atime<time:
                arrivals+=1
        for dtime in departure:
            if dtime<time:
                departures+=1  
        counts.append(arrivals-departures)  
        time += unit_time
    plt.plot(timestamps,counts)
    plt.xlabel("Time")
    plt.ylabel("Number of jobs in system")
    plt.show()

def which_job_is_being_served(jobsArray):
    timestamps = []
    job_served = []
    colors = []
    time = 0
    unit_time = 0.25
    max_departure = 0
    for job in jobsArray:
        job.first_service = job.arrival_time + job.waiting_time
        job.departure = job.arrival_time+job.waiting_time+job.service_time
        max_departure = max(job.departure,max_departure)     
    while time<max_departure:
        timestamps.append(time)
        flag = 0
        for job in jobsArray:
            if job.first_service<=time and job.departure>time:
                job_served.append(1)
                colors.append(job.color)
                flag = 1
                break
        if flag==0:
            job_served.append(0)
            colors.append("white")
        time += unit_time
    plt.bar(timestamps,job_served,color=colors)
    plt.xlabel("Time")
    plt.ylabel("Type of job")
    plt.ylim(0,10)
    plt.title("Identity of Jobs with time")
    plt.show()