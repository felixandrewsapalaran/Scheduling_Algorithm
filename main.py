# casting in python applied using the following line (int/int = double)

from __future__ import division


# This class used to print each scheduling algorithm row

class SchedulingRow:
    # Declaring variables
    pn = 0  # Project Number
    at = 0.0  # Arrival Time
    bt = 0.0  # Burst Time
    ct = 0.0  # Complete Time
    tt = 0.0  # Turn Around Time
    wt = 0.0  # Waiting Time
    btRemaining = 0.0  # Remaining Burst Time

    # Class Constructor
    def __init__(self, at, bt):
        self.at = at
        self.bt = bt

    # row number p1 to p6
    def printRow(self, i):
        print('{:>6}{:>6.1f}{:>6.1f}{:>6.1f}{:>6.1f}{:>6.1f}\n'.format(i, self.at, self.bt, self.ct, self.tt, self.wt))

    # Note: {:>6.1f} means print 6 spaces before, 1 digit from the float number


# This class is the core of the program which calculates all scheduling algorithms

class SchedulingAlgorithm:
    # Declaring variables
    FCFS = []  # List of SchedulingRow objects
    att = 0.0  # Avg Turn Around Time
    awt = 0.0  # Avg Waiting Time

    # Default Constructor
    def __init__(self):
        self.att = 0.0
        self.awt = 0.0

    # Adding new period of time
    def add(self, at, bt):
        row = SchedulingRow(at, bt)
        row.pn = len(self.FCFS)
        self.FCFS.append(row)

    # Calculate all 6 variables if each process
    def compute(self, switchingOverHead, evalOrder):

        ct = 0.0  # Complete Time
        sumtt = 0.0  # Total Turn Around Time
        sumwt = 0.0  # Total Waiting Time

        for i in range(0, len(self.FCFS)):
            # evaluation order this code 41 - 46 lets you re order the number of processes
            j = i  # the loop compute evaluates position in j
            # if no special order then j= i means sequential

            if evalOrder is not None:
                # if there is ordering supplied, it look up ordering in the array using the code below
                j = evalOrder[i] - 1

            row = self.FCFS[j]
            ct = ct + row.bt
            row.ct = ct
            # compute tt
            row.tt = ct - row.at
            # avg tt for avg
            sumtt += row.tt
            # compute wt
            row.wt = row.tt - row.bt
            # compute wt for avg
            sumwt += row.wt

            ct += switchingOverHead

        # compute att, awt
        self.att = sumtt / len(self.FCFS)
        self.awt = sumwt / len(self.FCFS)

    # round robin when timeSlice is exceeded
    def compute2(self, switchingOverHead, evalOrder, timeSlice):
        queue = []  # List of SchedulingRow objects

        for i in range(0, len(self.FCFS)):
            # evaluation order this code 41 - 46 lets you re order the number of processes
            j = i  # the loop compute evaluates position in j
            # if no special order then j= i means sequential

            if evalOrder is not None:
                # if there is ordering supplied, it look up ordering in the array using the code below
                j = evalOrder[i] - 1

            row = self.FCFS[j]
            queue.append(row)
            row.btRemaining = row.bt

        ct = 0.0
        sumtt = 0.0
        sumwt = 0.0
        ctr = 0

        while len(queue) > 0:
            print("queue size is ", len(queue), '\n')
            if ctr > 100:
                break

            ctr += 1
            # search loop to find something ready to run
            for i in range(0, len(queue)):
                print("searching position ", i, '\n')
                row = queue[i]

                if row.at <= ct:
                    # run this row
                    # to time slice
                    ts = min(row.btRemaining, timeSlice)
                    row.btRemaining -= ts
                    print("pn", row.pn + 1, " at {:>1.1f}".format(ct), " giving time", ts, " remaining",
                          row.btRemaining, "\n")
                    ct = ct + ts

                    if row.btRemaining == 0:
                        # otherwise compute sums, and, remove it from the queue
                        row.ct = ct
                        # compute tt
                        row.tt = ct - row.at
                        # avg tt for avg
                        sumtt += row.tt
                        # compute wt
                        row.wt = row.tt - row.bt
                        # compute wt for avg
                        sumwt += row.wt
                        # remove from the Queue
                        queue.remove(queue[i])
                    else:
                        # if anything is left, move it to the end of the queue
                        queue.remove(queue[i])
                        queue.append(row)

                    ct += switchingOverHead
                    # we found something to run, so stop search loop
                    # and go back to outer while loop
                    break

        # compute att, awt
        self.att = sumtt / len(self.FCFS)
        self.awt = sumwt / len(self.FCFS)

    def printTable(self):
        print("\tPro   AT    BT    CT    TT    WT\n")
        for i in range(0, len(self.FCFS)):
            row = self.FCFS[i]
            row.printRow(i)

        print("att = ", '{:>2.2f}\n'.format(self.att))
        print("awt = ", '{:>2.2f}\n'.format(self.awt))


# Program starts here

if __name__ == '__main__':
    Jobs = SchedulingAlgorithm()
    print("\nFirst Come First Serve Algorithm")

    Jobs.add(0, 6)
    Jobs.add(3, 2)
    Jobs.add(5, 1)
    Jobs.add(9, 7)
    Jobs.add(10, 4)
    Jobs.add(11, 3)

    Jobs.compute(0.0, None)     # Passing None means we're in FCFS algorithm
    Jobs.printTable()

    print("\nSJF")
    array = [1, 3, 2, 4, 6, 5]
    Jobs.compute(0.0, array)     # Passing array means we're in SJF algorithm
    Jobs.printTable()

    print("\nRound Robin")
    Jobs.compute2(0.0, None, 4)     # Passing None + quantum = 4 means we're in Round Robin algorithm
    Jobs.printTable()

    """
    Hint: The queue of processes would be as following
    
        1 2 3 4 5 6  7 8 9  10 11 12 13 14 15 16 17 18 19 20 21 22 23
        ==============================================================
        P0    |P1 |P2|P0 |P3          |P4         |P5      |P3      |
    """

    print("\nWITH Context Switching Time = 0.4 milisecond.")

    print("\nFCFS")
    Jobs.compute(0.4, None)    # Passing context time = 0.4 and None means we're in FCFS algorithm
    Jobs.printTable()

    print("\nSJF")
    array = [1, 3, 2, 4, 6, 5]
    Jobs.compute(0.4, array)     # Passing context time = 0.4 and array means we're in SJF algorithm
    Jobs.printTable()

    print("\nRound Robin")
    Jobs.compute2(0.4, None, 4)    # Passing context time = 0.4 + None + quantum= 4 means we're in Round Robin algorithm
    Jobs.printTable()

    print("\nWith the above solution/calculations it shows that the Shortest Job First(SJF) is the optimal & "
          "effecient one.")
