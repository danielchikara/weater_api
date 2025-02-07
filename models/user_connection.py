import psycopg

class UserConnection():
    conn = None

    def __init__(self):
        try:
            self.conn = psycopg.connect("dbname=weater_bd user=danielchikara password=angelesfuimos123 host=localhost port=5432")
        except psycopg.OperationalError as err:
            print(err)
            self.conn.close()

    def write(self, data):
        with self.conn.close()  as cur:
          pass
           

    def __def__(self):
        self.conn.close()
    
