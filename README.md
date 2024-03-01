# Analysis of Scheduling Policies in Queueing Systems

## Introduction
2 different scheduling policies are simulated,

1. `Pre-emptive` Shortest Job First `(SJF)`
2. `Non Preemptive` Shortest Job First `(SJF)`

## Dataset Used

In both the queueing systems simulated, a common `job size dataset` was created beforehand. This dataset contains the following parameters:
    
    1. Service Time (Exponential with rate λ)
    2. Arrival Time (Exponential interarrival times with rate μ)
    3. Priority

The priority is assigned based on their service times and the number of queues which is set as 4.

## Graphs and Other Derivations

Statistical inferences like `mean waiting time`, `mean sojourn time`, `mean service time`, etc are also derived.

### Pre-emptive SJF

The following graphs are plotted for `Pre-emptive SJF`:

    1. Arrival and Departures times of each job
    2. Average Latency Vs Priority
    3. Average Pre-emptions Vs Priority
    4. Number of Jobs in System Vs Time 
    5. Latency Vs Job Arrivals
    6. Number of Preemptions Vs Job Arrivals
    7. Response Time Vs Job Arrivals
    8. Waiting Time Vs Job Arrivals

### Non Preemptive SJF

The following graphs are plotted for `Non Preemptive SJF`:

    1. Arrival and Departures times of each job
    2. Number of Jobs in System Vs Time 
    3. Waiting Time Vs Job Arrivals


# How to Simulate

One can follow the following steps to simulate these results

1. Pull/Download this repositiory to your local machine

2. Generate the dataset by running the `generate_data.py` script - `python generate_data.py`.

3. Run all the cells in both the `jupyter notebooks`, that is, `non_premptive.ipynb` and `preemptive.ipynb`.

One can change parameters like `service rate`, `number of queues`, `number of jobs`, etc, easily by changing the constants field which are defined at the beggining of the code.