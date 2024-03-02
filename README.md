# Analysis of Scheduling Policies in Queueing Systems

## Introduction
2 different scheduling policies are simulated,

1. `Pre-emptive` Shortest Job First `(SJF)`
2. `Non Preemptive` Shortest Job First `(SJF)`

## Dataset Used

In both the queueing systems simulated, a common `job size dataset` was created using random data generator - `generate_data.py`. This dataset contains the following parameters:
    
    1. Interarrival Time (Exponential with rate λ)
    2. Service Time (Exponential with rate μ)
    3. Priority

The priority is assigned based on their service times (job size) and the number of queues which is set as 4.

## Graphs and Other Derivations

Statistical inferences like `mean waiting time`, `mean sojourn time`, `mean service time`, etc are also derived.

### Pre-emptive SJF

The following graphs are plotted for `Pre-emptive SJF`:

    1. Waiting Time Vs Job Arrivals
    2. Average Waiting Time Vs Priority
    3. Latency Vs Job Arrivals
    4. Average Latency Vs Priority
    5. Response Time Vs Job Arrivals
    6. Average Response Time Vs Priority
    7. Number of Preemptions Vs Job Arrivals
    8. Average Pre-emptions Vs Priority

### Non Preemptive SJF

The following graphs are plotted for `Non Preemptive SJF`:

    1. Waiting Time Vs Job Arrivals
    2. Average Waiting Time Vs Priority

### Comparison between Preemptive and Non preemptive

    1. No of jobs in the system v/s time
    2. Arrival and Departures times of each job
    3. Job (scheduling) history in the system


# How to Simulate

One can follow the following steps to simulate these results

1. Clone/Pull/Download this repositiory to your local machine

2. Generate the dataset by running the `generate_data.py` script
   
        python generate_data.py

4. Run all the cells in both the `jupyter notebooks`, that is, `non_premptive.ipynb` and `preemptive.ipynb`.

One can change parameters like `service rate`, `number of queues`, `number of jobs`, etc, easily by changing the constants field which are defined at the beggining of the code in `generate_data.py`

### Team Members

    1. M S S Sriharsha (2022101041)
    2. Abhinav Raundhal (2022101089)
    3. Archisha Panda (2022111019)
    4. Yash Shinde (2022111009)
    5. Aanvik Bhatnagar (2022101103)
