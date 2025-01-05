from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
    aws_lambda as lambda_,
    aws_lambda_event_sources as lambda_event_sources
)


class SqsLambdaDemoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create our Queue
        queue = sqs.Queue(
            self, "SqsLambdaDemoQueue",
            visibility_timeout=Duration.seconds(300),
        )

        # Create our lambda Function
        

        
