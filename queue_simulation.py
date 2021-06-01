import random
from queue import Queue

# This is a model of queue in a store.
# We presume following statements to be true:
# in an hour we have 200 customers in the store;
# probability of customer showing up at every second is constant;
# customers have an equal chance of having from 1 to 70 items;
# speed of scanning the products is constant for an employee and we ignore the time needed to pay;
# we have two types of employees: regulars (speed 20) and learning (speed 15);
# speed of employee is determined as items/minute
# there is one queue in the store.
# We look at an hour of store's traffic to determine if certain amount of registers with certain employees
# can handle the traffic


class Employee(object):
    """Implementation of an employee of a store"""
    def __init__(self, speed):
        """Takes speed of scanning and init variables speed,
        current task as none and time remaining as 0."""
        self.speed = speed
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        """What happens for every second of simulation."""
        if self.current_task:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        """If employee don't have a current tasks return False,
        return True otherwise"""
        if not self.current_task:
            return False
        else:
            return True

    def start_customer(self, next_cus):
        """Takes next_customer (an instance of class Customer
        and set the current task to that customer and time remaining
        proportional to number of items"""
        self.current_task = next_cus
        self.time_remaining = next_cus.get_items() * 60 / self.speed


class Customer(object):
    """Implementation of a customer in a store"""
    def __init__(self, time):
        """Take time and saves it as variable time_stamp.
        Set items variable as random int between 1 and 50."""
        self.time_stamp = time
        self.items = random.randrange(1, 51)

    def get_stamp(self):
        """Return time stamp variable"""
        return self.time_stamp

    def get_items(self):
        """Return items variable"""
        return self.items

    def wait_time(self, current_time):
        """Take current time and returns difference between current time and
        time saved as time stamp"""
        return current_time - self.time_stamp


def new_customer(how_busy, num_sec):
    """Take number of customers (how_busy) and number of secods.
    Return True if random num between 1 and value rn is equal to rn."""
    rn = num_sec//how_busy
    num = random.randrange(1, rn + 1)
    if num == rn:
        return True
    else:
        return False


def take_next_cus(reg_queue, emp, waiting_times, t):
    """Take reg_queue (register que), emp(employee),  waiting times list and current second.
    If employee is not busy and there is a customer in queue set new task for employee, take customer off
    the queue and add the waiting time of a customer to the list of waiting times"""
    if (not emp.busy()) and (not reg_queue.is_empty()):
        next_cus = reg_queue.dequeue()
        waiting_times.append(next_cus.wait_time(t))
        emp.start_customer(next_cus)


def simulation(work_speed, num_sec, how_busy):
    """Take list of work speeds of employees, number of seconds and number of customers.
    Create instances of Employee class for every speed, empty queue and empty list for waiting times.
    In every second (t) if customer arrives add them to queue and evaluate take_next_cus function and
    tick of an employee. Return tuple of average waiting times and size of que"""
    emp = []
    for item in range(len(work_speed)):
        emp.append(Employee(work_speed[item]))

    reg_queue = Queue()
    waiting_times = []

    for t in range(num_sec):
        if new_customer(how_busy, num_sec):
            cus = Customer(t)
            reg_queue.enqueue(cus)

        for i in emp:
            take_next_cus(reg_queue, i, waiting_times, t)
            i.tick()

    return sum(waiting_times)/len(waiting_times), reg_queue.size()


def multiple_simulations(work_speed, num=20):
    """Take list employee's work speeds and optional number of iterations (simulations).
    Return average wait time and average number of customers remaining from those simulations"""
    mean_wait = 0
    customers_remaining = 0
    for i in range(num):
        sim = simulation(work_speed, 3600, 200)
        mean_wait += sim[0]
        customers_remaining += sim[1]

    return mean_wait/num, customers_remaining/num


if __name__ == "__main__":
    # simulation
    speed_list = [[20, 15, 15], [20, 20, 15], [20, 20, 15], [20, 20, 15, 15], [20, 20, 15, 15, 15],
                  [20, 20, 20, 20, 20]]
    for i in speed_list:
        count = [0, 0]
        sym = multiple_simulations(i)
        for item in i:
            if 15 == item:
                count[0] += 1
            elif 20 == item:
                count[1] += 1
        if sym[0] < 120:
            result = "good enough!"
        else:
            result = "not good enough :("
        string = "With %s learning employee(s) and %s regular employee(s) " % (count[0], count[1])
        string += "average waiting time is %s and average number of customers remaining is %s and that's %s"\
                  % (sym[0], sym[1], result)
        print(string)
