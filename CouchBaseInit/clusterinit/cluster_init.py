import  os
import subprocess


class ClusterInit(object):
    os.chdir('C:\\Program Files\\Couchbase\\Server\\bin')
    space = ' '

    def __init__(self, adminuser, adminpassword, ramsize, clusterport, services):
        self.adminuser = adminuser
        self.adminpassword = adminpassword
        self.ramsize = ramsize
        self.clusterport = clusterport
        self.service = services

    def initcluster(self):
        node_init_cli = 'couchbase-cli cluster-init -c localhost:8091 -u Admin -p Admin123' + ' '\
                        '--cluster-init-username=' + self.adminuser + ClusterInit.space + \
                        '--cluster-init-password=' + self.adminpassword + ClusterInit.space + \
                        '--cluster-init-ramsize=' + self.ramsize + ClusterInit.space + \
                        '--cluster-init-port=' + self.clusterport + ClusterInit.space + \
                        '--services=' + str(self.service)

        p = subprocess.Popen(node_init_cli, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        response = str(output)
        if 'ERROR' in response:
            print('ERROR: cluster init is not successful  REASON :  '+response)
        else:
            print("SUCCESS: cluster init is successful")
            return 'SUCCESS'


