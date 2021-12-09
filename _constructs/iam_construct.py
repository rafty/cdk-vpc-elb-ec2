from constructs import Construct
from aws_cdk import aws_iam


class IamConstruct(Construct):
    def __init__(self, scope: Construct, id: str) -> None:
        super().__init__(scope, id)

        # ------------------------------------------
        # SSM Iam Role
        # ------------------------------------------
        self._iam_role = aws_iam.Role(
            self, 'SsmIamRole',
            assumed_by=aws_iam.ServicePrincipal('ec2.amazonaws.com'),
            managed_policies=[
                aws_iam.ManagedPolicy.from_aws_managed_policy_name(
                    'AmazonSSMManagedInstanceCore'),
                aws_iam.ManagedPolicy.from_aws_managed_policy_name(
                    'CloudWatchAgentServerPolicy')
            ]
        )

    @property
    def iam_role(self):
        return self._iam_role
