##TO READ FROM STDIN
##import fileinput
##
##for line in fileinput.input():
##    pass

##TO WRITE TO STDOUT
##import sys
##for i in range(3):
##  sys.stdout.write('Dive in')

##----------------------PROGRAM-------------------------
import fileinput
import sys

##CLASS DECLARATION
class Worker:

    def __init__(self,name):
        self.name = name
        self.status = "idle" #statuses: idle, working
        self.job = None

    def assign_job(self,new_job):
        self.status = "working"
        self.job = new_job

    def remove_job(self):
        self.status = "idle"
        self.job = None

class Job:

    def __init__(self,job,tasks,duration,start_min,priority):
        self.name = job
        self.task_count = tasks #permanent value of tasks
        self.tasks = tasks #decrementable value of tasks
        self.timer = duration
        self.duration = duration
        self.start_min = start_min
        self.priority = priority

    def decrement_timer(self):
        #Start new task/end task only when timer reaches 0
        #print "in decr"
        #print "tasks left: ",self.tasks

        #Note: we're running the decrement @ the start of the count ..
        # ie. iterating through timer values 5,4,3,2,1 means 5 iterations
        # of decrement and there 5 time units have elapsed!
        if self.timer == 1:
            
            #print "timer is 1: ",self.timer
            
            #If no more tasks left, return 2 for job completed
            if self.tasks == 1:
                #print "job done"
                return 2

            #Otherwise, reset timer, and decrement tasks, return 1
            else:
                #print "reset timer"
                self.tasks = self.tasks - 1
                self.timer = self.duration #Reset timer for new task
                #print "tasks: ",self.tasks
                #print "timer: ",self.timer
                return 1

        #Otherwise, just decrement timer
        else:
            #print "timer is not 0: ",self.timer
            
            self.timer = self.timer - 1
            return 0

##FUNCTION DECLARATIONS
def simple_scheduler(cl_jobs,cl_workers): #Read class of jobs and workers

    timer = 0
    jobs_completed = 0
    next_avail_job = 0 #stores index in list of next available job
    job_index_max = len(cl_jobs) - 1 #since index goes from 0 -> total-1
    jobs_removed = []

    #Print values before starting scheduler
    #print "Timer: ",timer
    #print "Jobs completed: ",jobs_completed
    #print "Next available job: ",next_avail_job
    #print "Total jobs: ",job_index_max+1

    #Want to run until all jobs are complete
    while jobs_completed < job_index_max+1:
        
        #Assign jobs to all idle workers (takes 0 time units) and let all workers
        # perform their task for 1 unit of time
        for worker in cl_workers:

            #Assign jobs to all idle workers
            if worker.status == 'idle':
                #print next_avail_job
                worker.assign_job(cl_jobs[next_avail_job])

                print timer,worker.name,worker.job.name #ONLY LEGAL OUTPUT

                if (next_avail_job < job_index_max):
                    next_avail_job += 1

            #Process worker's current task

            #If w
    timer = 0
    jobs_completed = 0
    start_dict = {}
    avail_jobs = []
    current_jobs = []
    job_index_max = len(cl_jobs) - 1 #since index goes from 0 -> total-1
    jobs_removed = []

    #Assign the start_time limits
    for job in cl_jobs:
        start_min = job.start_min

        #If key exists, append to list @ key
        if start_min in start_dict.keys():
            start_dict[start_min].append(job)

        else:
            start_dict[start_min] = [job]

    #TEST:
##    keys_list = start_dict.keys()
##    print keys_list
##    for key in keys_list:
##        for i in range(len(start_dict[key])):
##            print key,start_dict[key][i]

    #Print values before starting scheduler
    #print "Timer: ",timer
    #print "Jobs completed: ",jobs_completed
    #print "Next available job: ",next_avail_job
    #print "Total jobs: ",job_index_max+1

    #Want to run until all jobs are complete
    while jobs_completed < job_index_max+1:

        #print timer

        #Update available jobs
        if timer in start_dict.keys():
            #print timer
            for i in range(len(start_dict[timer])):
                avail_jobs.append(start_dict[timer][i])            
        
        #Assign jobs to all idle workers (takes 0 time units) and let all workers
        # perform their task for 1 unit of time
        for worker in cl_workers:

            #Assign jobs to all idle workers
            if worker.status == 'idle':
                #print next_avail_job
                print "avail jobs: ",avail_jobs
                print "current jobs: ",current_jobs
                
                if len(avail_jobs) != 0:
                    worker.assign_job(avail_jobs[0]) #Assign first available job
                    current_jobs.append(avail_jobs[0])
                    avail_jobs.remove(avail_jobs[0])
                elif len(current_jobs) != 0:
                    worker.assign_job(current_jobs[0]) #Speed up existing job
                else:
                    pass
                
                if worker.job != None:
                    print timer,worker.name,worker.job.name #ONLY LEGAL OUTPUT

            #Process worker's current task

            #If worker's status is not 'idle', then process the job
            #This case may occur if another android finishes the job in the same
            #time step.
            if not (worker.job in jobs_removed):
                job_status = worker.job.decrement_timer()
            else:
                worker.remove_job()

            #If job status is 2, then re-assign worker
            if job_status == 2:
                current_jobs.remove(worker.job)
                jobs_removed.append(worker.job)
                worker.remove_job()
                jobs_completed += 1
                job_status = 0 #reset job status, for case of multiple workers
                               # on the same job

        #Reset jobs removed
        jobs_removed = []

        #Increment timer
        timer += 1
        
    #Print after scheduler has run
    #print "Timer: ",timer
    #print "Jobs completed: ",jobs_completed
    #print "Next available job: ",next_avail_job
    #print "Total jobs: ",job_index_max+1orker's status is not 'idle', then process the job
            #This case may occur if another android finishes the job in the same
            #time step.
            if not (worker.job in jobs_removed):
                job_status = worker.job.decrement_timer()
            else:
                worker.remove_job()

            #If job status is 2, then re-assign worker
            if job_status == 2:
                jobs_removed.append(worker.job)
                worker.remove_job()
                jobs_completed += 1
                job_status = 0 #reset job status, for case of multiple workers
                               # on the same job

        #Reset jobs removed
        jobs_removed = []

        #Increment timer
        timer += 1
        
    #Print after scheduler has run
    #print "Timer: ",timer
    #print "Jobs completed: ",jobs_completed
    #print "Next available job: ",next_avail_job
    #print "Total jobs: ",job_index_max+1

def moderate_scheduler(cl_jobs,cl_workers): #Read class of jobs and workers

    timer = 0
    jobs_completed = 0
    start_dict = {}
    avail_jobs = []
    current_jobs = []
    job_index_max = len(cl_jobs) - 1 #since index goes from 0 -> total-1
    jobs_removed = []

    #Assign the start_time limits
    for job in cl_jobs:
        start_min = job.start_min

        #If key exists, append to list @ key
        if start_min in start_dict.keys():
            start_dict[start_min].append(job)

        else:
            start_dict[start_min] = [job]

    #TEST:
##    keys_list = start_dict.keys()
##    print keys_list
##    for key in keys_list:
##        for i in range(len(start_dict[key])):
##            print key,start_dict[key][i]

    #Print values before starting scheduler
    #print "Timer: ",timer
    #print "Jobs completed: ",jobs_completed
    #print "Next available job: ",next_avail_job
    #print "Total jobs: ",job_index_max+1

    #Want to run until all jobs are complete
    while jobs_completed < job_index_max+1:

        #print timer

        #Update available jobs
        if timer in start_dict.keys():
            #print timer
            for i in range(len(start_dict[timer])):
                avail_jobs.append(start_dict[timer][i])            
        
        #Assign jobs to all idle workers (takes 0 time units) and let all workers
        # perform their task for 1 unit of time
        for worker in cl_workers:

            #Assign jobs to all idle workers
            if worker.status == 'idle':
                #print next_avail_job
                print "avail jobs: ",avail_jobs
                print "current jobs: ",current_jobs
                
                if len(avail_jobs) != 0:
                    worker.assign_job(avail_jobs[0]) #Assign first available job
                    current_jobs.append(avail_jobs[0])
                    avail_jobs.remove(avail_jobs[0])
                elif len(current_jobs) != 0:
                    worker.assign_job(current_jobs[0]) #Speed up existing job
                else:
                    pass
                
                if worker.job != None:
                    print timer,worker.name,worker.job.name #ONLY LEGAL OUTPUT

            #Process worker's current task

            #If worker's status is not 'idle', then process the job
            #This case may occur if another android finishes the job in the same
            #time step.
            if not (worker.job in jobs_removed):
                job_status = worker.job.decrement_timer()
            else:
                worker.remove_job()

            #If job status is 2, then re-assign worker
            if job_status == 2:
                current_jobs.remove(worker.job)
                jobs_removed.append(worker.job)
                worker.remove_job()
                jobs_completed += 1
                job_status = 0 #reset job status, for case of multiple workers
                               # on the same job

        #Reset jobs removed
        jobs_removed = []

        #Increment timer
        timer += 1
        
    #Print after scheduler has run
    #print "Timer: ",timer
    #print "Jobs completed: ",jobs_completed
    #print "Next available job: ",next_avail_job
    #print "Total jobs: ",job_index_max+1

def required_scheduler(cl_jobs,cl_workers):

    timer = 0
    jobs_completed = 0
    start_dict = {}
    avail_jobs = []
    current_jobs = []
    job_index_max = len(cl_jobs) - 1 #since index goes from 0 -> total-1
    jobs_removed = []

    #Assign the start_time limits
    for job in cl_jobs:
        start_min = job.start_min

        #If key exists, append to list @ key
        if start_min in start_dict.keys():
            start_dict[start_min].append(job)

        else:
            start_dict[start_min] = [job]

    #TEST:
##    keys_list = start_dict.keys()
##    print keys_list
##    for key in keys_list:
##        for i in range(len(start_dict[key])):
##            print key,start_dict[key][i]

    #Print values before starting scheduler
    #print "Timer: ",timer
    #print "Jobs completed: ",jobs_completed
    #print "Next available job: ",next_avail_job
    #print "Total jobs: ",job_index_max+1

    #Want to run until all jobs are complete
    while jobs_completed < job_index_max+1:

        #print timer

        #Update available jobs
        if timer in start_dict.keys():
            #print timer
            for i in range(len(start_dict[timer])):
                avail_jobs.append(start_dict[timer][i])            
        
        #Assign jobs to all idle workers (takes 0 time units) and let all workers
        # perform their task for 1 unit of time
        for worker in cl_workers:

            #Assign jobs to all idle workers
            if worker.status == 'idle':
                #print next_avail_job
                print "avail jobs: ",avail_jobs
                print "current jobs: ",current_jobs
                
                if len(avail_jobs) != 0:
                    worker.assign_job(avail_jobs[0]) #Assign first available job
                    current_jobs.append(avail_jobs[0])
                    avail_jobs.remove(avail_jobs[0])
                elif len(current_jobs) != 0:
                    worker.assign_job(current_jobs[0]) #Speed up existing job
                else:
                    pass
                
                if worker.job != None:
                    print timer,worker.name,worker.job.name #ONLY LEGAL OUTPUT

            #Process worker's current task

            #If worker's status is not 'idle', then process the job
            #This case may occur if another android finishes the job in the same
            #time step.
            if not (worker.job in jobs_removed):
                job_status = worker.job.decrement_timer()
            else:
                worker.remove_job()

            #If job status is 2, then re-assign worker
            if job_status == 2:
                current_jobs.remove(worker.job)
                jobs_removed.append(worker.job)
                worker.remove_job()
                jobs_completed += 1
                job_status = 0 #reset job status, for case of multiple workers
                               # on the same job

        #Reset jobs removed
        jobs_removed = []

        #Increment timer
        timer += 1
        
    #Print after scheduler has run
    #print "Timer: ",timer
    #print "Jobs completed: ",jobs_completed
    #print "Next available job: ",next_avail_job
    #print "Total jobs: ",job_index_max+1

##PROGRAM

inp_str = []
inp_list = []
jobs = [] #list of lists
workers = [] #list of lists
cl_jobs = [] #list of job classes
cl_workers = [] #list of worker classes

#Read lines
inp_str = raw_input()

#Sample Input
#job count_doodads 119 11 0 1\njob stamp_whatsits 264 5 22 1\nworker Android_Joe\nworker Android_Mary\n

#Split up input list
inp_list = inp_str.split('\\n')
#inp_list = inp_list[:-1] #Get rid of last space element
#print inp_list

for line in inp_list:
    new_line = line.split(' ')
    #print new_line

    #Put line into jobs or workers list
    if new_line[0] == "job":
        jobs.append(new_line)
        
    elif new_line[0] == "worker":
        workers.append(new_line)

#print jobs
#print workers

#Create a list of job classes
for job in jobs:
    #print job

    cl_jobs.append(Job(job[1],int(job[2]),int(job[3]),int(job[4]),int(job[5]))) #job,tasks,duration,start_min,priority

#Create list of worker classes
for worker in workers:
    #print worker

    cl_workers.append(Worker(worker[1])) #name

###Test
##for cl_elem in cl_jobs:
##    print cl_elem.job
##    print cl_elem.tasks
##    print cl_elem.task_count
##    print cl_elem.timer
##    print cl_elem.duration
##    print cl_elem.start_min
##    print cl_elem.priority
##   
##for cl_elem in cl_workers:
##    print cl_elem.name
##
###job count_doodads 119 11 0 1\njob stamp_whatsits 264 5 22 1\nworker Android_Joe\nworker Android_Mary\n
##
##sample_job = Job('sample job',3,5,0,1)
##sample_job = cl_jobs[0]
##timer = 0
##job_out = 0
##
##while job_out != 2:
##    job_out = sample_job.decrement_timer()
##    timer += 1
##    #print timer
##
##print timer
##print sample_job.duration
##print job_out

#Setup simple scheduler
simple_scheduler(cl_jobs,cl_workers) #cl_jobs,cl_workers
#moderate_scheduler(cl_jobs,cl_workers)
#required_scheduler(cl_jobs,cl_workers)

    
    



