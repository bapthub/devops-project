variable "region" {
  description = "Region used for deploying on AWS."
  type        = string
  default     = "eu-west-3"
}

variable "tags" {
  description = "Tags mappings"
  type        = map(any)
  default = {
    SCHOOL = "EPITA"
    PROMO  = "APPING II 2021-2024"
    GROUP  = "1"
  }
}

variable "ecr-front" {
  description = "ECR Repository for the frontend"
  type = string
  default = "ecr-front"
}

variable "COMMIT" {
  type = string
}

variable "BRANCH" {
  type = string
}

variable "USER" {
  type = string
}