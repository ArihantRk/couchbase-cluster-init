import os
import subprocess


class BucketCreate(object):
    os.chdir('C:\\Program Files\\Couchbase\\Server\\bin')
    space = ' '

    def __init__(self, adminuser, adminpassword, bucketname, eviction, buckettype, port, ramsize, priority,
                 replica, flushenable, replicaindex):
        self.adminuser = adminuser
        self.adminpassword = adminpassword
        self.bucketname = bucketname
        self.eviction = eviction
        self.buckettype = buckettype
        self.port = port
        self.ramsize = ramsize
        self.priority = priority
        self.replica = replica
        self.replicaindex = replicaindex
        self.flushenable = flushenable

    def bucketcreate(self):
        bucket_create_cli = 'couchbase-cli bucket-create -c localhost:8091 -u ' + self.adminuser + ' -p ' + self.adminpassword + BucketCreate.space+ \
                            '--bucket=' + self.bucketname + BucketCreate.space +\
                            '--bucket-eviction-policy=' + self.eviction + BucketCreate.space + \
                            '--bucket-type=' + self.buckettype + BucketCreate.space + \
                            '--bucket-port=' + self.port + BucketCreate.space + \
                            '--bucket-ramsize=' + self.ramsize + BucketCreate.space +\
                            '--bucket-priority=' + self.priority + BucketCreate.space +\
                            '--bucket-replica=' + self.replica + BucketCreate.space +\
                            '--enable-flush=' + self.flushenable + BucketCreate.space +\
                            '--enable-index-replica=' + self.replicaindex + BucketCreate.space +\
                            '--wait'

        p = subprocess.Popen(bucket_create_cli, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        response = str(output)
        if 'ERROR' in response:
            print('ERROR: Bucket create '+self.bucketname+' REASON :' + response)
        else:
            print('SUCCESS: Bucket create ' +self.bucketname)
            return 'SUCCESS'

