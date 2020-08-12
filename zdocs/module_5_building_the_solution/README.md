# Module 5: Build and deploy the solution

---

## Index

* Module 1: [Create an Azure IoT Hub](../module_1_create_iot_hub/README.md)
* Module 2: [Install Azure IoT Edge on your Raspberry Pi](../module_2_install_azure_iot_edge/README.md)
* Module 3: [Set up your development environment](../module_3_set_up_computer/README.md)
* Module 4: [Create Azure Cognitive Services](../module_4_create_azure_resources/README.md)
* Module 5: [Build and deploy the solution](../module_5_building_the_solution/README.md)
* Module 6: [Build and deploy the solution](../module_6_camera_settings/README.md)

* [Home](../../README.md)

---

## Understanding the Project Structure

The following describes the highlighted sections of the project.

1. There are two modules: CameraCaptureOpenCV and ImageClassifierService.

2. The module.json file defines the Docker build process, the module version, and your docker registry. Updating the version number, pushing the updated module to an image registry, and updating the deployment manifest for an edge device triggers the Azure IoT Edge runtime to pull down the new module to the edge device.

3. The deployment.template.json file is used by the build process. It defines what modules to build, what message routes to set up, and what version of the IoT Edge runtime to run.

4. The deployment.json file is generated from the deployment.template.json and is the [Deployment Manifest](https://docs.microsoft.com/en-us/azure/iot-edge/module-composition/?WT.mc_id=julyot-tir-dglover)

5. The version.py in the project root folder is a helper app you can run on your development machine that updates the version number of each module. Useful as a change in the version number is what triggers Azure IoT Edge runtime to pull the updated module and it is easy to forget to change the module version numbers:)

    ![visual studio code project structure](../resources/visual-studio-code-open-project.png)  

## Building the Solution

You need to ensure the image you plan to build matches the target processor architecture. In our case, we are going to build for **arm32v7**.

1. Confirm processor architecture.
    From the Visual Studio Code bottom bar click the currently selected processor architecture, then from the popup select **arm32v7**.
    ![](../resources/select-processor-architecture.png)

6. Next, Build and Push the solution to Docker by right mouse clicking the deployment.template.json file and select "**Build and Push IoT Edge Solution**". The first build will be slow as Docker needs to pull the base layers to your local machine. If you are cross compiling to arm32v7 then the first build will be very slow as OpenCV and Python requirements need to be compiled. On a fast Intel i7-8750H processor cross compiling this solution will take approximately 40 minutes.

    ![docker build and push](../resources/solution-build-push-docker.png)

## Deploying the Solution

When the Docker Build and Push process has completed select the Azure IoT Hub device you want to deploy the solution to. Right mouse click the deployment.json file found in the config folder and select the target device from the drop-down list.

   ![deploy to device](../resources/deploy-to-device.png)

## View the device telemetry from the Azure Cloud Shell

1. You will need to know the name of the Azure IoT Hub you created. You can get the name from the Azure web portal.
    ![](resources/azure-iot-resources.png)
2. Open the Azure Cloud shell at [https://shell.azure.com](https://shell.azure.com).
3. In the Cloud Shell, run the [az extension add](https://docs.microsoft.com/cli/azure/extension?view=azure-cli-latest&WT.mc_id=julyot-tir-dglover) command to add the Microsoft Azure IoT Extension to your CLI shell. The IoT Extension adds IoT Hub, IoT Edge, and IoT Device Provisioning Service (DPS) specific commands to Azure CLI.

    ```bash
    az extension add --name azure-iot
    ```

4. Start the IoT Hub Events Monitor with the following command. Be sure to use your IoT Hub name.

    ```bash
    az iot hub monitor-events --hub-name {your IoT Hub name}
    ```

5. Observe telemetry in the cloud. The output will be similar to the following screen.

    ![](resources/iot-hub-monitor-events.png)

6. Use <kbd>ctrl+c</kbd> to stop the event monitor.

## Monitoring the Solution on the IoT Edge Device

Once the solution has been deployed you can monitor it on the IoT Edge device itself using the ```iotedge list``` command.

```bash
iotedge list
```

  ![watch iotedge list](../resources/iotedge-list.png)

## Monitoring the Solution from the Azure IoT Edge Blade

You can monitor the state of the Azure IoT Edge module from the Azure IoT Hub blade on the [Azure Portal](http://portal.azure.com).

   ![azure iot edge devices](../resources/azure-iotedge-monitoring.png)

   Click on the device from the Azure IoT Edge blade to view more details about the modules  running on the device.

   ![azure iot edge device details](../resources/azure-portal-iotedge-device-details.png)

---

**[NEXT](../module_6_camera_settings/README.md)**

---