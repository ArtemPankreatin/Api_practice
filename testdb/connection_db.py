import psycopg2
class DB():
    def __init__(self):
        self.connection = psycopg2.connect(host='54.37.74.248', database='api', user='klim', port='5432')
        self.cursor = self.connection.cursor()

    def execute(self,command):
        try:
            self.cursor.execute(command)
        except Exception as err:
            if err == '0':
                pass
            else:
                print(err)

    def commit(self):
        self.connection.commit()