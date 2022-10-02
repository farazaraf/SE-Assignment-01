import threading
import time
import random
import sys




class Node:
	def __init__(self):
		self.data = None
		self.next = None

class Queue:
	def __init__(self):
		self.front = None
		self.rear = None

	def delOrder(self,order):
		temp = self.front
		
		if self.front.data[1] == order:
			self.deQueue()
			#self.front != self.front
			#self.front.next
			#temp =temp.next;
			temp.next = self.front

		while temp.data != self.rear.data:
			#print("tempdata is: ", temp.data, "\nrear is: ",self.rear.data);
			if temp.next.data[1] == order :
				temp.next = temp.next.next
				break
			elif order != temp.data and temp.next.next == self.rear:
				print("Item not found in the list.")
				break
			else:
				temp = temp.next
		
		#self.front = None
		#self.rear.link = self.front
		#temp.next = self.front.next.next
		
	def enQueue(q, value):
		temp = Node()
		temp.data = value
		if q.front == None:
			q.front = temp
		else:
			q.rear.next = temp

		q.rear = temp
		q.rear.next = q.front

# Function to delete element from
# Circular Queue
	def deQueue(q):
		if (q.front == None):
			#print("Queue is empty")
			return -999

		# If this is the last node to be deleted
		value = None # Value to be dequeued
		if (q.front == q.rear):
			value = q.front.data
			q.front = None
			q.rear = None
		else: # There are more than one nodes
			temp = q.front
			value = temp.data
			q.front = q.front.next
			q.rear.next = q.front

		return value
	def displayQueue(q):
		temp = q.front
		print("Elements in Circular Queue are: ",end = " ")
		while (temp.next != q.front):
			print(temp.data, end = " ")
			temp = temp.next
		print(temp.data)

Order_Queue = Queue()
start = time.perf_counter()


class ShopFunctions:

    def __init__(self):
        self.q = Queue()
        self.x = None
        self.y = None
    
    def AddOrder(self,order):
        self.q.enQueue(order)

    def DisplayOrders(self):
        self.q.displayQueue()
    
    def ShowPrice(self,order):
        self.tprice = order[4]
        print(f"\nThe Final Price is: {self.tprice}\nPlease pay at the Checkout Thankyou!")
        self.ChangeStatus(order)    

    def ChangeStatus(self,order):
        order[3] = 'complete'
        

    def Interior(self):
        print("Cleaning Up Car Interior...")
        time.sleep(3)
        print("Done Cleaning Interior.")
    def Exterior(self):
        print("Washing The Exterior...")
        time.sleep(2)
        print("Done Washing Exterior")

    def Full(self):
        self.Interior()
        self.Exterior()

    def Oil_Change(self):
        print("Changing Oil...")
        time.sleep(2)
        print("Finished Oil Change")

    def Tire_Maintenance(self):
        print("Tire Maintenance occuring...")
        time.sleep(1)
        print("Finished Tire Maintenance")

    def Full_Car_Check(self):
        print("Full Car Maintenance in Progress...")
        time.sleep(4)
        print("Finishing Car maintenance")

    def Custom_Issues(self):
        print("Custom Order...")
        time.sleep(2)
        print("Finished Custom Order")

    def Tinted_Windows(self):
        print("Custom Window Customization..")
        time.sleep(3)
        print("Finished Customization")

    def Custom_Rims(self):
        print("Custom Rims Customization..")
        time.sleep(3)
        print("Finished Customization")
        
    def Custom_Exhaust(self):
        print("Custom Exhaust Customization..")
        time.sleep(3)
        print("Finished Customization")

    def separateName(self,order):
        func = order[2]
        result = eval('self.' + func + "()")

    def ManageFunction(self,Orderx,Ordery):
        if Orderx[0] != Ordery[0]:
            print("Execute Multithread")
            t1 = threading.Thread(target=self.separateName,args=(Orderx,))
            t2 = threading.Thread(target=self.separateName,args=(Ordery,))
            t1.start()
            t2.start()
            t1.join()
            t2.join()
        else:
            self.separateName(self.x)
            self.separateName(self.y)
    def RunOrder(self):
        #check if there is an order in the queue
        self.x = self.q.deQueue()
        if self.x == -999:
            print ("No Orders")
        else:
            self.y = self.q.deQueue()
            if self.y == -999:
                self.separateName(self.x)
                self.ShowPrice(self.x)
            else:
                self.ManageFunction(self.x,self.y)
            
