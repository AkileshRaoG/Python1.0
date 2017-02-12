from rip.ripper import Rest_ripper
from rip.parse_stat import my_parser as rp
from rip.logger import log
from threading import Thread
import time
class deploy:
    def __init__(self):

        self.stat=Rest_ripper()
        self.entries = rp().read_input_file('req_modified.cfg')
    def post_deploy(self):
        '''for each component connect to the URL and get he stats'''

        for e in self.entries:
                log.debug("Now Processing %s : %s"%(e.type,e.ip))

                log.debug("PARAMS=%s"%e.data)
                log.debug("TIME_FRAME=%s"%e.times)
                t=Thread(target=self.stat.make_url_connect ,args=(e.ip, e.data, e.type,e.times,e.port,e.ssl,e.username,e.password))
                t.start()



if __name__ == "__main__":
    '''deploy the ripper and start the stat collection'''
    start_time=time.time()
    d=deploy()
    d.post_deploy()
    log.debug("Thread Processed for %s SECONDS!!!"%(time.time()-start_time))
