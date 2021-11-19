from mysql.connector import connect

class Connection :
    def connection(self):
        self.db = connect(
            host = "localhost",
            user = "root",
            password = "root",
            database = "kampus"
        )

        return self.db
