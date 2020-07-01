# Creating required Azure Cognitive Services

---

## Creating the Fruit Classification Model

The [Azure Custom Vision](https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/) service is a simple way to create an image classification machine learning model without having to be a data science or machine learning expert. You simply upload multiple collections of labelled images. For example, you could upload a collection of banana images and label them as 'banana'.

To create your own classification model read [How to build a classifier with Custom Vision](https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/getting-started-build-a-classifier/?WT.mc_id=devto-blog-dglover) for more information. It is important to have a good variety of labelled images so be sure to read [How to improve your classifier](https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/getting-started-improving-your-classifier/?WT.mc_id=devto-blog-dglover).

## Exporting an Azure Custom Vision Model

This "Image Classification" module includes a simple fruit classification model that was exported from Azure Custom Vision. For more information read how to [Export your model for use with mobile devices](https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/export-your-model/?WT.mc_id=devto-blog-dglover). It is important to select one of the "**compact**" domains from the project settings page otherwise you will not be able to export the model.

Follow these steps to export your Custom Vision project model.

1. From the **Performance** tab of your Custom Vision project click **Export**.

    ![export model](../resources/exportmodel.png)

2. Select Dockerfile from the list of available options

    ![export-as-docker.png](../resources/export-as-docker.png)

3. Then select the Linux version of the Dockerfile.

   ![choose docker](../resources/export-choose-your-platform.png)

4. Download the docker file and unzip and you have a ready-made Docker solution with a Python Flask REST API. This was how I created the Azure IoT Edge Image Classification module in this solution. Too easy:)

## Azure Speech Services

[Azure Speech Services](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/) supports both "speech to text" and "text to speech". For this solution, I'm using the text to speech (F0) free tier which is limited to 5 million characters per month. You will need to add the Speech service using the Azure Portal and "Grab your key" from the service.

![azure speech service](../resources/speech-service.png)

Open the deployment.template.json file and update the BingKey with the key you copied from the Azure Speech service.

![speech key](../resources/speech-key.png)