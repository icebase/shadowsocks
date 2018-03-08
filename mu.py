import db_transfer
import config
import logging
from musdk.client import Client


class MuApiTransfer(db_transfer.TransferBase):
    client = None
    users = []

    def __init__(self):
        super(MuApiTransfer, self).__init__()
        self.pull_ok = False
        self.port_uid_table = {}
        self.init_mu_client()

    def init_mu_client(self):
        mu_url = config.mu_uri
        mu_token = config.token
        node_id = config.node_id
        mu_client = Client(mu_url, node_id, mu_token)
        self.client = mu_client

    def pull_db_all_user(self):
        print("pull all users...")
        return self.pull_db_users()

    def pull_db_users(self):
        users = self.client.get_users_res()
        if users is None:
            return self.users
        for user in users:
            self.port_uid_table[user['port']] = user['id']
        self.users = users
        return users

    def update_all_user(self, dt_transfer):
        print('call update all user')
        print(dt_transfer)
        update_transfer = {}
        logs = []
        for id in dt_transfer.keys():
            transfer = dt_transfer[id]
            if transfer[0] + transfer[1] < 1024:
                continue
            update_transfer[id] = transfer
            uid = self.port_uid_table[id]
            log = self.client.gen_traffic_log(uid, transfer[0], transfer[1])
            logs.append(log)
        print("logs ", logs)
        ok = self.client.update_traffic(logs)
        if ok is False:
            logging.error("update traffic failed...")
            return {}
        return update_transfer
