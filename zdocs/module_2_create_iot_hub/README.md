# Creating an Azure IoT Hub

<!-- This solution will use three services

1. [Azure IoT Hub](https://docs.microsoft.com/en-us/azure/iot-hub/)
2. [Azure Custom Vision](https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/)
3. [Azure Speech Services](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/) -->

---

## Create an Azure Subscription

If you do not have an Azure Subscription then [create an Azure Subscription](https://azure.microsoft.com/en-us/free/). Students can sign up for a free [Azure for Students](https://azure.microsoft.com/en-us/free/students/) subscription that does not require credit card verification.

---

## Prepare Azure resources

You can prepare Azure cloud resources with the Azure CLI, the Azure Portal Web interface, or deployment templates. For this module, we will be using an Azure deployment template.

Click the **Deploy to Azure** button to deploy Azure resources. An IoT Hub will be created.

[![Deploy to Azure](https://azuredeploy.net/deploybutton.png)](https://azuredeploy.net/?repository=https://github.com/gloveboxes/Create-a-talking-image-recognition-solution-with-Azure-IoT-Edge-Azure-Cognitive-Services/tree/master/zdocs/azure-deployment)

1. Select or create a new resource group, choose the site located closest to you, and select the IoT Hub Tier. The default IoT Hub tier is the free **F1** tier. You can only have one free IoT Hub per subscription. If you already have a free IoT Hub then either select S1 ([pricing](https://azure.microsoft.com/en-us/pricing/details/iot-hub/)) or delete your existing free IoT Hub before proceeding.

    ![](../resources/azure-deployment-settings.png)

2. Click **Next**.
3. Click **Deploy**. The deployment will take three to four minutes to complete.

    ![](../resources/azure-deployment-completed.png)

4. When the deployment has completed, click on **Manage your resources**. You will see the IoT Hub listed in the Azure Web Portal.

    ![](../resources/azure-iot-resources.png)

5. Click on the IoT Hub resource created to open it.
6. From the IoT Hub blade, select **IoT Edge** from the IoT Hub blade sidebar menu
7. Click **+ New**
8. In the **Device ID** dialogue box, name your device **rpi-edge-device**.
9. Click **Save**. This will create the device.
10. Click on the newly create IoT Edge device
11. Click the **Copy** icon to the right of the **Primary Connection String** field and save to Notepad or a text edit on your Operating System as you will need this connection string when configuring your Iot Edge device.
    ![](../resources/iot-edge-device-connaction-string.png)