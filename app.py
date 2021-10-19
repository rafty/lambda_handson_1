#!/usr/bin/env python3
import os

from aws_cdk import core as cdk

from aws_cdk import core

from lambda_handson_1.lambda_handson_1_stack import LambdaHandson1Stack


app = core.App()

LambdaHandson1Stack(app, "LambdaHandson1Stack")

app.synth()
