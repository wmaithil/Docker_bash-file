import socket
import threading
from Queue import Queue

print_lock=threading.Lock()

target=raw_input("Enter name of target")


#server=raw_input("Enter name of website ")

def portscan(port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		con=s.connect((target,port))
		with print_lock:
			print 'port ',port,' is open '
		con.close()
	except:
		pass
		
print "portscan func successfull"		
def threader():
	while True:
		worker=q.get()
		portscan(worker)
		q.task_done()
				
print "threader func successfull"
q=Queue()

for i in range(100):
	t=threading.Thread(target=threader)
	t.daemon=True
	t.start()
	
print "thread func successfull"
for worker in range(15,500):
	q.put(worker)
	
q.join()
	
"""for i in range(20,1000):
	if pscan(i):
		print 'Discovered Port', i ,' is Open !!!!'
	else:
		print 'Port ', i , 'is Closed'
		
"""	
		

