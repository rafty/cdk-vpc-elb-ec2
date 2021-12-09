from constructs import Construct
from aws_cdk import aws_ec2


class VpcConstruct(Construct):
    def __init__(self, scope: Construct, id: str) -> None:
        super().__init__(scope, id)

        self._vpc = aws_ec2.Vpc(
            self, 'Vpc',
            cidr="10.10.0.0/16",
            max_azs=2,
            nat_gateways=2,
            enable_dns_hostnames=True,  # default: True
            enable_dns_support=True,  # default: True
            subnet_configuration=[
                aws_ec2.SubnetConfiguration(
                    subnet_type=aws_ec2.SubnetType.PUBLIC,
                    name="Public",
                    cidr_mask=24),
                aws_ec2.SubnetConfiguration(
                    subnet_type=aws_ec2.SubnetType.PRIVATE_WITH_NAT,
                    name="Private",
                    cidr_mask=24),
            ],
        )

    @property
    def vpc(self):
        return self._vpc
