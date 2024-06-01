import json
import boto3

ec2 = boto3.client('ec2')
instance_id = '<your ec2 instance id>'

def lambda_handler(event, context):

    action = json.loads(event['body'])['action']
    print(f"{action =}")
    try:
        if action == 'start':
            response = ec2.start_instances(InstanceIds=[instance_id])
            state = response['StartingInstances'][0]['CurrentState']['Name']
            print(f'Instance {instance_id} is {state}')
            return {
                'statusCode': 200,
                'body': json.dumps(f'Instance {instance_id} is {state}')
            }
        elif action == 'stop':
            response = ec2.stop_instances(InstanceIds=[instance_id])
            state = response['StoppingInstances'][0]['CurrentState']['Name']
            print(f'Instance {instance_id} is {state}')
            return {
                'statusCode': 200,
                'body': json.dumps(f'Instance {instance_id} is {state}')
            }
        else:
            print('Invalid action. Use "start" or "stop".')
            return {
                'statusCode': 400,
                'body': json.dumps('Invalid action. Use "start" or "stop".')
            }
    except Exception as e:
        print(f"{e = }")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
