import os
import random

from aws_cdk import core

import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_s3_assets as s3_assets


class SteamcmdEc2Stack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.vpc = ec2.Vpc.from_lookup(self, "VPC", vpc_id='vpc-0051b8b7bdff9a7d0')
        self.userdata = self.define_userdata_asset(os.getcwd(), 'configure.sh')
        self.ami = self.find_ami()
        self.instance = self.define_ec2_instance()
        self.add_userdata_to_instance()

    def define_userdata_asset(self, path, filename):
        full_path = os.path.join(path, filename)
        if os.path.isfile(full_path):
            return s3_assets.Asset(self, "UserDataAsset", path=full_path)
        else:
            print(f"Could not find {full_path}")

    def find_ami(self):
        return ec2.MachineImage.latest_amazon_linux()

    def define_ec2_instance(self):
        t3a_small = ec2.InstanceType.of(
            instance_class=ec2.InstanceClass.BURSTABLE3_AMD,
            instance_size=ec2.InstanceSize.SMALL
        )

        return ec2.Instance(
            self,
            "Instance",
            instance_type=t3a_small,
            machine_image=self.ami,
            vpc=self.vpc,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
            key_name="Gazwald"
        )

    def add_userdata_to_instance(self):
        local_path = self.instance.user_data.add_s3_download_command(
            bucket=self.userdata.bucket,
            bucket_key=self.userdata.s3_object_key
        )

        self.instance.user_data.add_execute_file_command(
            file_path=local_path,
            arguments="--verbose -y"
        )

        self.userdata.grant_read(self.instance.role)

