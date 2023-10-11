resource "aws_key_pair" "epita_key" {
  key_name   = "epita"
  public_key = tls_private_key.key.public_key_openssh
}

resource "random_shuffle" "public_subnet_id" {
  input        = data.terraform_remote_state.vpc.outputs.vpc_public_subnets
  result_count = 1
}

resource "aws_instance" "my-ec2" {
  ami = "ami-05e8e219ac7e82eba"

  subnet_id                   = element(random_shuffle.public_subnet_id.result, 0)
  associate_public_ip_address = true

  instance_type          = "t2.micro"
  iam_instance_profile   = "LabInstanceProfile" // As we can't create IAM Role, I'm using an existing role
  vpc_security_group_ids = [aws_security_group.sg-epita.id]
  key_name               = aws_key_pair.epita_key.key_name

  tags = merge(var.tags,
    {
      USER   = var.USER
      BRANCH = var.BRANCH
      COMMIT = var.COMMIT
      Name        = "ec2-epita"
      Terraform   = "true"
      Environment = "test"
  })
}

resource "aws_security_group" "sg-epita" {
  name_prefix = "sg_epita"
  description = "SG used in my courses"

  vpc_id = data.terraform_remote_state.vpc.outputs.vpc_id

  # Règle pour autoriser tout le trafic
  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "all"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "all"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = merge(var.tags,
    {
      USER   = var.USER
      BRANCH = var.BRANCH
      COMMIT = var.COMMIT
      Terraform   = "true"
      Environment = "test"
  })
}