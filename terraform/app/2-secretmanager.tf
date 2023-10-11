resource "tls_private_key" "key" {
  algorithm = "RSA"
  rsa_bits  = 2048
}

resource "aws_secretsmanager_secret" "epita_key" {
  name = "epita-secret"
  tags = merge(var.tags,
    {
      USER   = var.USER
      BRANCH = var.BRANCH
      COMMIT = var.COMMIT
      Terraform   = "true"
      Environment = "test"
  })
}

resource "aws_secretsmanager_secret_version" "epita" {
  secret_id     = aws_secretsmanager_secret.epita_key.id
  secret_string = tls_private_key.key.private_key_pem
}