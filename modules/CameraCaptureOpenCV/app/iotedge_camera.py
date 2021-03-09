# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for
# full license information.

import os
import random
import sys
import time
import asyncio
from azure.iot.device import IoTHubModuleClient, Message
# import ptvsd

# ptvsd.enable_attach(address=('0.0.0.0', 5678))
# ptvsd.wait_for_attach()


# from iothub_client import IoTHubModuleClient, IoTHubClientError, IoTHubTransportProvider
# from iothub_client import IoTHubMessage, IoTHubMessageDispositionResult, IoTHubError

import CameraCapture
from CameraCapture import CameraCapture


# global counters
SEND_CALLBACKS = 0
module_client = None


def send_to_Hub_callback(strMessage):
    if strMessage == []:
        return

    message = Message(strMessage)
    message.content_encoding = "utf-8"
    message.custom_properties["appid"] = "scanner";


    # hubManager.send_event_to_output("output1", message, 0)
    print('sent from send_to_Hub_callback')

# Callback received when the message that we're forwarding is processed.


def send_confirmation_callback(message, result, user_context):
    global SEND_CALLBACKS
    SEND_CALLBACKS += 1


class HubManager(object):

    async def __init__(
            self
    ):
        self.client = IoTHubModuleClient.create_from_connection_string("HostName=glovebox-iothub.azure-devices.net;DeviceId=rpi8gb;SharedAccessKey=jHsEt+KayurPjY3AghOYI5j7T3x15qQmN9flHojkF+4=")
        await self.client.connect()

    def send_event_to_output(self, outputQueueName, event, send_context):
        pass
        
        # self.client.send_message(message);
        # self.client.send_event_async(
        #     outputQueueName, event, send_confirmation_callback, send_context)


def initialise(
        videoPath,
        bingSpeechKey,
        predictThreshold,
        imageProcessingEndpoint="",
        speechMapFileName = None
):
    '''
    Capture a camera feed, send it to processing and forward outputs to EdgeHub

    :param str connectionString: Edge Hub connection string. Mandatory.
    :param int videoPath: camera device path such as /dev/video0 or a test video file such as /TestAssets/myvideo.avi. Mandatory.
    :param str imageProcessingEndpoint: service endpoint to send the frames to for processing. Example: "http://face-detect-service:8080". Leave empty when no external processing is needed (Default). Optional.

    '''
    try:
        print("\nPython %s\n" % sys.version)
        print("Camera Capture Azure IoT Edge Module. Press Ctrl-C to exit.")

        # global hubManager
        # hubManager = HubManager()

        with CameraCapture(videoPath, bingSpeechKey, predictThreshold, imageProcessingEndpoint, send_to_Hub_callback, speechMapFileName) as cameraCapture:
            cameraCapture.start()
    except KeyboardInterrupt:
        print("Camera capture module stopped")


def __convertStringToBool(env):
    if env in ['True', 'TRUE', '1', 'y', 'YES', 'Y', 'Yes']:
        return True
    elif env in ['False', 'FALSE', '0', 'n', 'NO', 'N', 'No']:
        return False
    else:
        raise ValueError('Could not convert string to bool.')


async def main():
    global module_client
    try:
        VIDEO_PATH = os.getenv('Video', '0')
        PREDICT_THRESHOLD = os.getenv('Threshold', .75)
        IMAGE_PROCESSING_ENDPOINT = os.getenv('AiEndpoint', 'http://localhost:80/image')
        AZURE_SPEECH_SERVICES_KEY = os.getenv('azureSpeechServicesKey', '2f57f2d9f1074faaa0e9484e1f1c08c1')
        SPEECH_MAP_FILENAME = os.getenv('SpeechMapFilename', 'speech_map_australian.json')


        # The client object is used to interact with your Azure IoT hub.
        # module_client = IoTHubModuleClient.create_from_edge_environment()

        module_client = IoTHubModuleClient.create_from_connection_string("HostName=glovebox-iothub.azure-devices.net;DeviceId=rpi8gb;SharedAccessKey=jHsEt+KayurPjY3AghOYI5j7T3x15qQmN9flHojkF+4=")
        
        module_client.connect()

    except ValueError as error:
        print(error)
        sys.exit(1)

    initialise(VIDEO_PATH, AZURE_SPEECH_SERVICES_KEY,
         PREDICT_THRESHOLD, IMAGE_PROCESSING_ENDPOINT, SPEECH_MAP_FILENAME)

if __name__ == "__main__":
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    # loop.close()

    # If using Python 3.7 or above, you can use following code instead:
    asyncio.run(main())
