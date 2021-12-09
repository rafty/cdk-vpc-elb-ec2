from aws_cdk import Stack
from constructs import Construct
from _constructs.vpc_construct import VpcConstruct


class VpcStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc_construct = VpcConstruct(self, 'VpcConstruct')
        self._vpc = vpc_construct.vpc

    @property
    def vpc(self):
        return self._vpc
