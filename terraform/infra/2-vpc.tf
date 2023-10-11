module "vpc" {
  source = "terraform-aws-modules/vpc/aws"

  name = "VPC"
  cidr = "10.0.0.0/16"

  azs             = ["eu-west-3a", "eu-west-3b", "eu-west-3c"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]

  enable_nat_gateway = false
  create_igw = true

  tags = merge(var.tags,
    {
      USER   = var.USER
      BRANCH = var.BRANCH
      COMMIT = var.COMMIT
      Terraform   = "true"
      Environment = "test"
  })
}