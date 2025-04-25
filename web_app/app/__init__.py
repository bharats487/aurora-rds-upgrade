from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from boto3 import client
import os

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config['DEBUG'] = True  # Enable debug mode for troubleshooting

db = SQLAlchemy()

# Configure database connection
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

# Get database endpoint from AWS RDS
endpoint = get_db_endpoint()
if endpoint:
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://admin:ChangeMe123!@{endpoint}:3306/aurora_mysql"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

from app import routes
