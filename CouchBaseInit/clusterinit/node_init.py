import os
import subprocess


class NodeInit(object):
    os.chdir('C:\\Program Files\\Couchbase\\Server\\bin')

    def __init__(self, node_data_path, node_index_path, hostname):
        self.hostname = hostname
        self.node_data_path = node_data_path
        self.node_index_path = node_index_path

    def setpath(self):
        node_init_cli = 'couchbase-cli node-init -c localhost:8091 -u Admin -p Admin123 '+ ' ' \
                        '--node-init-data-path=' + self.node_data_path +' '\
                        '--node-init-index-path=' + self.node_index_path
        # ' ' + '--node-init-hostname=' + hostname
        p = subprocess.Popen(node_init_cli, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        response = str(output)
        if 'ERROR' not in response:
            print("SUCCESS: node init is successful")
            return 'SUCCESS'
        else:
            print("ERROR : node init is not successful and REASON : ", output)

