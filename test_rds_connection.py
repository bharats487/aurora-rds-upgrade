import pymysql
import sys

def test_connection():
    try:
        # Connection parameters
        host = "aurora-mysql-cluster.cluster-ckwj8hhzuve1.ca-central-1.rds.amazonaws.com"
        user = "admin"
        password = "ChangeMe123!"
        database = "aurora_mysql"
        port = 3306

        # Create connection
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port,
            cursorclass=pymysql.cursors.DictCursor
        )

        print("Successfully connected to RDS!")
        
        # Test query
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            print("Test query result:", result)
            
        connection.close()
        print("Connection closed successfully.")
        
    except Exception as e:
        print(f"Error connecting to RDS: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    test_connection()
