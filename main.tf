#provider block
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "us-east-1"
}

#creating s3 bucket
resource "aws_s3_bucket" "factorial_bucket" {
  bucket = "zahaab-pythom-bucket"
  acl= "private"
}