provider "aws" {
  region = "ca-central-1" # Change as needed
}

resource "aws_security_group" "aurora_mysql" {
  name        = "aurora-mysql-sg"
  description = "Security group for Aurora MySQL"

  # Allow MySQL traffic from your local machine
  ingress {
    from_port   = 3306
    to_port     = 3306
    protocol    = "tcp"
    cidr_blocks = ["192.168.1.116/32"]  # Replace with your actual IP address
  }

  # Allow MySQL traffic from anywhere for testing
  ingress {
    from_port   = 3306
    to_port     = 3306
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_rds_cluster" "aurora_mysql" {
  cluster_identifier      = "aurora-mysql-cluster"
  engine                  = "aurora-mysql"
  engine_version          = "8.0.mysql_aurora.3.04.0"
  master_username         = "admin"
  master_password         = "ChangeMe123!" # Change to a secure value or use secrets manager
  skip_final_snapshot     = true
  
  # Set up security group
  vpc_security_group_ids = [aws_security_group.aurora_mysql.id]
  
  # Specify database name
  database_name = "aurora_mysql"
}

resource "aws_rds_cluster_instance" "aurora_mysql_instance" {
  identifier              = "aurora-mysql-instance-1"
  cluster_identifier      = aws_rds_cluster.aurora_mysql.id
  instance_class          = "db.t3.medium"
  engine                  = aws_rds_cluster.aurora_mysql.engine
  engine_version          = aws_rds_cluster.aurora_mysql.engine_version
  publicly_accessible     = true
}

output "rds_endpoint" {
  value = aws_rds_cluster.aurora_mysql.endpoint
}

output "rds_writer_endpoint" {
  value = aws_rds_cluster.aurora_mysql.endpoint
}

output "rds_reader_endpoint" {
  value = aws_rds_cluster.aurora_mysql.reader_endpoint
}
