data "terraform_remote_state" "vpc" {
  backend = "s3"
  config = {
    region         = "eu-west-3"
    bucket         = "my-travel-map-bucket"
    key            = "infra.tfstate"
    dynamodb_table = "my-travel-map"
  }
}
