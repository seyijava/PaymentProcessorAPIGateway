'''
Created on Jan 19, 2018

@author: Admin
'''

from persistqueue import Queue;
import schedule
import time




  
def processMessage():
    queue = Queue("C:\\BigDataPlatform\\Projects\\bigdata\\Queue")
    item = queue.get();
    print(item.transactionChannel)
    queue.task_done()

schedule.every(1).second.do(processMessage)
 
if __name__ == '__main__':
   while True:
       schedule.run_pending()
       time.sleep(1)
