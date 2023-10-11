module "ecr-front" {
  source = "terraform-aws-modules/ecr/aws"

  repository_name = var.ecr-front

  repository_force_delete = true // Delete the repository even if it contains images. 

  repository_lifecycle_policy = jsonencode({
    rules = [
      {
        rulePriority = 1,
        description  = "Keep only 1 image", // FinOps for not explode $100 costs
        selection = {
          tagStatus     = "any",
          countType     = "imageCountMoreThan",
          countNumber   = 1
        },
        action = {
          type = "expire"
        }
      }
    ]
  })

  repository_image_tag_mutability = "MUTABLE"

  tags = merge(var.tags,
    {
      USER   = var.USER
      BRANCH = var.BRANCH
      COMMIT = var.COMMIT
      Terraform   = "true"
      Environment = "test"
  })
}