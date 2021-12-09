from aws_cdk import Stack
from constructs import Construct
from aws_cdk import aws_ec2
# from aws_cdk import aws_elasticloadbalancingv2
from aws_cdk import aws_elasticloadbalancingv2_targets
from _constructs.iam_construct import IamConstruct
from _constructs.alb_construct import AlbConstruct
from _constructs.ec2_construct import Ec2InstanceConstruct


class SystemStack(Stack):
    def __init__(self,
                 scope: Construct,
                 construct_id: str,
                 vpc: aws_ec2.Vpc,
                 **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        iam_construct = IamConstruct(self, 'IamConstruct')
        alb_construct = AlbConstruct(self, 'AlbConstruct', vpc=vpc)
        instance_construct = Ec2InstanceConstruct(
            self, 'InstanceConstruct',
            vpc=vpc,
            iam_role=iam_construct.iam_role
        )
        alb_construct.target_group.add_target(
            aws_elasticloadbalancingv2_targets.InstanceTarget(
                instance_construct.instance,
                port=80
            )
        )







