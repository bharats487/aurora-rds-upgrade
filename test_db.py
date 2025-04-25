from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.orm import declarative_base, sessionmaker
from boto3 import client
import os

# Get database endpoint from AWS RDS
def get_db_endpoint():
    rds_client = client('rds')
    try:
        response = rds_client.describe_db_clusters(
            DBClusterIdentifier='aurora-mysql-cluster'
        )
        cluster = response['DBClusters'][0]
        return cluster['Endpoint']
    except Exception as e:
        print(f"Error getting DB endpoint: {e}")
        return None

# Get database endpoint
endpoint = get_db_endpoint()
if not endpoint:
    print("Could not get RDS endpoint")
    exit(1)

# Create database engine
engine = create_engine(f"mysql+pymysql://admin:ChangeMe123!@{endpoint}:3306/aurora_mysql")

# Define a base class for declarative class definitions
Base = declarative_base()

# Define a test table
class TestTable(Base):
    __tablename__ = 'test_table'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

try:
    # Test connection
    session = Session()
    print("Database connection successful!")
    
    # Test query
    result = session.execute(text("SELECT 1")).fetchone()
    print("Test query result:", result)
    
    # Create test table
    Base.metadata.create_all(engine)
    print("Test table created successfully!")
    
    # Insert test data
    test_user = TestTable(name='Test User')
    session.add(test_user)
    session.commit()
    print("Test data inserted successfully!")
    
except Exception as e:
    print(f"Error: {str(e)}")
