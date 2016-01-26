import  os
import subprocess


class ServerAdd(object):
    os.chdir('C:\\Program Files\\Couchbase\\Server\\bin')
    space = ' '

    def __init__(self, adminuser, adminpassword, nodeip, services):
        self.adminuser = adminuser
        self.adminpassword = adminpassword
        self.nodeip = nodeip
        self.service = services

    def addServer(self):
        server_add_cli = 'couchbase-cli server-add -c '+self.nodeip+':8091 -u '+self.adminuser+' -p '+self.adminpassword+' '\
                        '--server-add=' + self.nodeip + ServerAdd.space + \
                        '--server-add-username=' + self.adminuser + ServerAdd.space + \
                        '--server-add-password=' + self.adminpassword + ServerAdd.space + \
                        '--services=' + str(self.service)

        p = subprocess.Popen(server_add_cli, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        response = str(output)
        if 'ERROR' in response:
            print('ERROR: cluster init is not successful  REASON :  '+response)
        else:
            print("SUCCESS: cluster init is successful")
            return 'SUCCESS'
