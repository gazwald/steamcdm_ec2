#!/usr/bin/env python3
import os

from aws_cdk import core

from steamcmd_ec2.steamcmd_ec2_stack import SteamcmdEc2Stack

env = {'account': os.getenv('AWS_ACCOUNT', os.getenv('CDK_DEFAULT_ACCOUNT', '')),
       'region': os.getenv('AWS_DEFAULT_REGION', os.getenv('CDK_DEFAULT_REGION', 'ap-southeast-2'))}


app = core.App()
SteamcmdEc2Stack(app, "steamcmd-ec2", env=env)

app.synth()
