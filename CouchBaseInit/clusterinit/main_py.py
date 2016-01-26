import subprocess
import sys
from clusterinit import bucket_create
from clusterinit import node_init
from clusterinit import server_add
from clusterinit import cluster_init


def main():

    if getNodeInitResponse() != 'SUCCESS':
        sys.exit(1)

    if getClusterInitResponse() != 'SUCCESS':
        sys.exit(1)

    #if getNodeAddResponse() != 'SUCCESS':
    #    sys.exit(1)

    if getBcreateResponse() != 'SUCCESS':
        sys.exit(1)

    rebalance('localhost','Admin','Admin123')



def getNodeInitResponse():
    nodeInit = node_init.NodeInit('D:\\Python', 'D:\\Python', 'localhost')
    return nodeInit.setpath()

def getClusterInitResponse():
    clusterInit = cluster_init.ClusterInit('Admin', 'Admin123', '400', '8091', ('data'))
    return clusterInit.initcluster()


def getNodeAddResponse():
    serverAdd = server_add.ServerAdd('Admin', 'Admin123', 'localhost', ('data'))
    return serverAdd.addServer()


def getBcreateResponse():
    bucketCreate = bucket_create.BucketCreate('Admin', 'Admin123', 'pttdata', 'valueOnly', 'couchbase', '1121', '100', 'low', '0', '1', '0')
    return bucketCreate.bucketcreate()


def rebalance(ipadress,adminusername,adminpassword):
    server_add_cli = 'couchbase-cli rebalance -c '+ipadress+':8091 -u '+adminusername+' -p '+adminpassword
    p = subprocess.Popen(server_add_cli, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    response = str(output)
    if 'ERROR' in response:
        print('ERROR: rebalance is not started due to  REASON :  '+response)
    else:
        print("SUCCESS: rebalance is completed")
        return 'SUCCESS'


if __name__ == main():
    main()
