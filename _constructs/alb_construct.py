from constructs import Construct
from aws_cdk import aws_ec2
from aws_cdk import aws_elasticloadbalancingv2


class AlbConstruct(Construct):
    def __init__(
            self,
            scope: Construct,
            id: str,
            vpc: aws_ec2.Vpc
    ) -> None:
        super().__init__(scope, id)

        # ------------------------------------------
        # ALB Security Group
        # ------------------------------------------
        alb_sg = aws_ec2.SecurityGroup(
            self, 'AlbSecurityGroup',
            security_group_name='alb-sg',
            vpc=vpc,
            description='Allow ssh access to ec2 instances from anywhere',
            allow_all_outbound=True
        )
        alb_sg.add_ingress_rule(
            peer=aws_ec2.Peer.any_ipv4(),
            connection=aws_ec2.Port.tcp(80),
            description='allow HTTP traffic from anywhere'
        )

        # ------------------------------------------
        # ALB
        # ------------------------------------------
        alb = aws_elasticloadbalancingv2.ApplicationLoadBalancer(
            self, 'Alb',
            vpc=vpc,
            vpc_subnets=aws_ec2.SubnetSelection(subnet_group_name='Public'),
            internet_facing=True,
        )

        # ------------------------------------------
        # ALB Target Group
        # ------------------------------------------
        health_check = aws_elasticloadbalancingv2.HealthCheck(
            path='/phpinfo.php',
            healthy_http_codes='200',
            healthy_threshold_count=2,
            unhealthy_threshold_count=2
        )

        self._alb_target_group = aws_elasticloadbalancingv2.ApplicationTargetGroup(
            self, 'AlbTargetGroup',
            vpc=vpc,
            port=80,
            protocol=aws_elasticloadbalancingv2.ApplicationProtocol.HTTP,
            target_type=aws_elasticloadbalancingv2.TargetType.INSTANCE,
            health_check=health_check
        )

        # ------------------------------------------
        # ALB Listener
        # ------------------------------------------
        alb.add_listener('PublicAlbListener',
                         port=80,
                         default_target_groups=[self._alb_target_group]
                         )

    @property
    def target_group(self):
        return self._alb_target_group
