terraform {
  required_version = "1.4.2"
  required_providers {
    aws = "4.63.0"
  }
}

provider "aws" {
  region = "eu-west-3"
}
terraform {
  backend "s3" {
    region         = "eu-west-3"
    bucket         = "my-travel-map-bucket"
    key            = "infra.tfstate"
    dynamodb_table = "my-travel-map"
  }
}
