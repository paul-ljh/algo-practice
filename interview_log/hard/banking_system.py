
def solution(queries):
    bs = BankingSystem()
    return bs.process_queries(queries)

class BankingSystem:
    def __init__(self):
        self.bank_data = {}
        self.transfer_data = []
        self.payment_id = 0
        self.payment_queue = []
        self.payment_id_pool = {}

    def process_queries(self, queries):
        result = []
        for query in queries:
            result.append(self.process_query(query))
        return result

    def process_query(self, query):
        if query[0] == 'CREATE_ACCOUNT':
            return self.create_account(query)
        elif query[0] == 'DEPOSIT':
            return self.deposit(query)
        elif query[0] == 'TOP_SPENDERS':
            return self.top_spenders(query)
        elif query[0] == 'SCHEDULE_PAYMENT':
            return self.queue_payment(query)
        else:
            return self.transfer(query)

    def queue_payment(self, query):
        self.payment_id += 1
        self.payment_id_pool.add(self.payment_id)
        self.payment_queue.append([query[2], query[3], query[1]+query[-1]])
        self.payment_queue.sort(key=[-1], reverse=True)
        return f"payment{self.payment_id}"

    def top_spenders(self, query):
        result = []
        count = int(query[-1])
        for i in range(min(count, len(self.transfer_data))):
            result.append(f"{self.transfer_data[i][0]}({self.transfer_data[i][1]})")
        return ', '.join(result)

    def reconciliate_transfer_data(self, source_account_id, amount):
        source_index = None
        for i in range(len(self.transfer_data)):
            if self.transfer_data[i][0] == source_account_id:
                self.transfer_data[i][1] += amount
                source_index = i
                break

        source_transfer_amount = self.transfer_data[source_index][1]
        for i in reversed(range(source_index)):
            account_id, transfer_amount = self.transfer_data[i][0], self.transfer_data[i][1]
            if source_transfer_amount > transfer_amount:
                self.transfer_data[i] = [source_account_id, source_transfer_amount]
                self.transfer_data[i+1] = [account_id, transfer_amount]
            elif source_transfer_amount == transfer_amount:
                if source_account_id < account_id:
                    self.transfer_data[i] = [source_account_id, source_transfer_amount]
                    self.transfer_data[i+1] = [account_id, transfer_amount]
                else:
                    break
            else:
                break


    def transfer(self, query):
        source_account_id, target_account_id, amount = query[2], query[3], int(query[-1])
        if source_account_id not in self.bank_data or target_account_id not in self.bank_data:
            return ''
        elif source_account_id == target_account_id:
            return ''
        elif self.bank_data[source_account_id] < amount:
            return ''
        else:
            self.bank_data[source_account_id] -= amount
            self.bank_data[target_account_id] += amount

            self.reconciliate_transfer_data(source_account_id, amount)
            return str(self.bank_data[source_account_id])

    def create_account(self, query):
        account_id = query[-1]
        if account_id in self.bank_data:
            return 'false'
        else:
            self.bank_data[account_id] = 0
            self.transfer_data.append([account_id, 0])
            self.reconciliate_transfer_data(account_id, 0)
            return 'true'

    def deposit(self, query):
        account_id = query[2]
        if account_id in self.bank_data:
            amount = int(query[-1])
            self.bank_data[account_id] += amount
            return str(self.bank_data[account_id])
        else:
            return ''
