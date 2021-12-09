#!/usr/bin/env python3
import os
import aws_cdk as cdk
from stacks.vpc_stack import VpcStack
from stacks.system_stack import SystemStack

env = cdk.Environment(
    account=os.environ.get('CDK_DEPLOY_ACCOUNT', os.environ['CDK_DEFAULT_ACCOUNT']),
    region=os.environ.get('CDK_DEPLOY_REGION', os.environ['CDK_DEFAULT_REGION']),
)

app = cdk.App()
vpc_stack = VpcStack(app, 'VpcStack', env=env)
system_stack = SystemStack(app, 'SystemStack', vpc=vpc_stack.vpc, env=env)


app.synth()
