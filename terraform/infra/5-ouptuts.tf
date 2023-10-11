output "vpc_id" {
  value = module.vpc.vpc_id
}

output "vpc_public_subnets" {
  value = module.vpc.public_subnets
}

output "ecr_front_id" {
  value = module.ecr-front.repository_url
}