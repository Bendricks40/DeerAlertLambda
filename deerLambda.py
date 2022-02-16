import json
import boto3
import os 

bucket_name = os.environ.get('bucket_name')

def lambda_handler(event, context):
    file_obj = event["Records"][0]
    key = str(file_obj["s3"]['object']['key'])
    if animal_detector(key, bucket_name):
        print("Something was spotted!")
    else:
        print("no animal from list identified")

def animal_detector(photo, bucket):
    client=boto3.client('rekognition')
    response = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':photo}},
        MaxLabels=20)
    found = False
    animalList = []
    for label in response['Labels']:
        print(label)
    for label in response['Labels']:
        animalList.append(str(label['Name']))
        if label['Name'] == 'Deer':
            print("DEER FOUND WITH {} percent confidence!!!".format(label['Confidence']))
            found = True
            deercaller()
        if label['Name'] == 'Fox':
            print("FOX FOUND WITH {} percent confidence!!!".format(label['Confidence']))
            found = True
            Fox()
        if label['Name'] == 'Rabbit':
            print("RABBIT FOUND WITH {} percent confidence!!!".format(label['Confidence']))
            found = True
            rabbit()   
        if label['Name'] == 'Dog':
            print("Dog FOUND WITH {} percent confidence!!!".format(label['Confidence']))
            found = True
            wildlife()  
        if label['Name'] == 'Cat':
            print("Cat FOUND WITH {} percent confidence!!!".format(label['Confidence']))
            found = True
            wildlife() 
        if label['Name'] == 'Wildlife':
            print("Wildlife FOUND WITH {} percent confidence!!!".format(label['Confidence']))
            found = True
            wildlife() 
        if label['Name'] == 'Animal':
            print("Animal FOUND WITH {} percent confidence!!!".format(label['Confidence']))
            #found = True
            #wildlife() 
        if label['Name'] == 'Mammal':
            print("Mammal FOUND WITH {} percent confidence!!!".format(label['Confidence']))
            found = True
            wildlife() 
        if label['Name'] == 'Rat':
            print("Rat FOUND WITH {} percent confidence!!!".format(label['Confidence']))
            found = True
            #wildlife() 
        if label['Name'] == 'Mouse':
            print("Mouse FOUND WITH {} percent confidence!!!".format(label['Confidence']))
            found = True
            #wildlife() 
        if label['Name'] == 'Person':
            print("Person FOUND WITH {} percent confidence!!!".format(label['Confidence']))
            found = True
            #wildlife() 
        if label['Name'] == 'Human':
            print("Human FOUND WITH {} percent confidence!!!".format(label['Confidence']))
            found = True
            #wildlife() 
        if label['Name'] == 'Man':
            print("Man FOUND WITH {} percent confidence!!!".format(label['Confidence']))
            found = True
            #wildlife() 
            
    #send a text with all things identified 
    #print("about to send animaltext")
    #animaltext(animalList)
    return found
    
def deercaller():
    client = boto3.client('connect')
    response = client.start_outbound_voice_contact(
        DestinationPhoneNumber = os.environ.get('DestinationPhoneNumber'), 
        SourcePhoneNumber = os.environ.get('SourcePhoneNumber'), 
        ContactFlowId = os.environ.get('DeerContactFlowId'), 
        InstanceId = os.environ.get('InstanceId'))
        
def wildlife():
    client = boto3.client('connect')
    response = client.start_outbound_voice_contact(
        DestinationPhoneNumber = os.environ.get('DestinationPhoneNumber'), 
        SourcePhoneNumber = os.environ.get('SourcePhoneNumber'), 
        ContactFlowId = os.environ.get('wildlifeContactFlowID'), 
        InstanceId = os.environ.get('InstanceId'))
        


def fox():
    client = boto3.client('connect')
    response = client.start_outbound_voice_contact(
        DestinationPhoneNumber = os.environ.get('DestinationPhoneNumber'), 
        SourcePhoneNumber = os.environ.get('SourcePhoneNumber'), 
        ContactFlowId = os.environ.get('FoxContactFlowId'), 
        InstanceId = os.environ.get('InstanceId'))
        
        
def rabbit():
    client = boto3.client('connect')
    response = client.start_outbound_voice_contact(
        DestinationPhoneNumber = os.environ.get('DestinationPhoneNumber'), 
        SourcePhoneNumber = os.environ.get('SourcePhoneNumber'), 
        ContactFlowId = os.environ.get('RabbitContactFlowId'), 
        InstanceId = os.environ.get('InstanceId'))
        
        
def animaltext(animalList):
    sns = boto3.client('sns')
    # Publish a simple message to the specified SNS topic
    if animalList:
        response = sns.publish(
                TopicArn='arn:aws:sns:us-east-1:317729718442:Animal_Alerter',   
                Message='Here is what was spotted: {}'.format(animalList),   
        )
