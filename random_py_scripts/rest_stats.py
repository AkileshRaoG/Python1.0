'''
Created on Aug 21, 2014

@author: devasj1
'''
import requests
import json
import csv
import time
import argparse

class RestValueGetter():
    
    def __init__(self, url, username='admin', password='netwitness', stat_format="csv"):
        '''
        Initialize the Crawler
        '''
        self.username = username
        self.password = password
        self.stat_format = stat_format
        self.url = url
        self.auth = (self.username,self.password)
        self.content_type = {'force-content-type': 'application/json'}
        self.outfile = "RestStats%s.%s" %( time.strftime("%Y%m%d_%H%M%S"),stat_format.lower())

    def send_request(self,path):
        url = self.url + path
        try:
            print ("Requesting For Path:%s") %(url)
            resp = requests.get(url, params=self.content_type, auth=self.auth)
            json_resp = json.loads(resp.text)
            print ("Response For Path:%s is:%s") %(path, json_resp)
            return json_resp
        except:
            print ("Error For Path:%s") %(path)
            return {}
        
    def get_stats(self, stats_node):
        nodes = self.send_request(path=stats_node).get("nodes")
        if nodes != None:
            for node in nodes:
                if node.get("value"):
                    self.set_output(stat=node.get('path'), value= node.get("value"))
                else:
                    self.get_stats(stats_node=node.get("path"))

    def set_output(self, stat, value):
        if self.stat_format.upper() == "CSV":
            csv_writer = csv.writer(open(self.outfile, "ab"), delimiter=',', quotechar=" ", quoting=csv.QUOTE_MINIMAL)
            print ("Adding Stats row %s:%s") %(stat, value)
            csv_writer.writerow([stat, str(value).replace(",", "|")])
        
if __name__ == '__main__':
    """
    Please use the below call to get the Property/Stat Values From a RestNode
    RestValueCrawler(LFName='ALL', noofevents=10, noofThreads=20)
    """
    parser = argparse.ArgumentParser(description='RestStatsGetter Arguments Parser')
    default_username = "admin"
    default_password = "netwitness"
    default_path = "/"
    default_format = "csv"

    parser.add_argument("-url", "--url",
                       metavar="url",
                       type = str,
                       help="URL of the Rest Service to connect, protocol://host:port")
    parser.add_argument("-u", "--username",
                      metavar="username",
                      default= default_username,
                      help="Username for the Rest Service to connect")
    parser.add_argument("-p", "--password",
                      metavar="password",
                      type= str,
                      default= default_password,
                      help="Password for the Rest Service to connect")
    parser.add_argument("-n", "--node",
                      metavar="node",
                      type= str,
                      default=default_path,
                      help="Root Node for the Rest Service to start Fetching Values Default is %s" %(default_path))
    parser.add_argument("-r", "--format",
                      metavar="format",
                      type= str,
                      default=default_format,
                      help="Format of the Fetching Values to Store in to File. Default is %s" %(default_format))
    
    args = parser.parse_args()
        
    crawler = RestValueGetter(url=args.url, username=args.username, password=args.password, stat_format=args.format)
    crawler.get_stats(stats_node=args.node)

    
    
    
    