# Module 2: Install Azure IoT Edge on your Raspberry Pi

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

## Hardware requirements

1. Raspberry Pi 4 recommended, 2GB or better
2. USB Camera
3. Speaker

### Booting from high speed USB3 storage

As we will be building Docker images on the Raspberry Pi 4 so I would recommend a fast SD Card or a high speed USB3 Flash or SSD drive.

* I use a Samsung [USB 3.1 Flash Drive FIT Plus 128GB](https://www.samsung.com/us/computing/memory-storage/usb-flash-drives/usb-3-1-flash-drive-fit-plus-128gb-muf-128ab-am/) or USB3 SSD drive. See the [5 of the Fastest and Best USB 3.0 Flash Drives](https://www.makeuseof.com/tag/5-of-the-fastest-usb-3-0-flash-drives-you-should-buy/)
* For instruction on booting from USB3 see [How to Boot Raspberry Pi 4 From a USB SSD or Flash Drive](https://www.tomshardware.com/how-to/boot-raspberry-pi-4-usb). Note, at the time of writing, set the *FIRMWARE_RELEASE_STATUS* to *stable* rather than *beta*.

---

## Raspberry Pi set up

### Create the Raspberry Pi OS Image

I recommend using Raspberry Pi OS Lite as it takes less resources than the full Raspberry Pi Desktop version. If you've not set up a Raspberry Pi before then this is a great guide. "[Setting up a Headless Pi](https://learn.pimoroni.com/tutorial/sandyj/setting-up-a-headless-pi)". Be sure to use the WiFi network as your development computer.



### Start Raspberry Pi and update

1. Insert SD Card or USB3 drive, and power on your Raspberry Pi.
2. Log into the Raspberry Pi over your network

    ```bash
    ssh pi@raspberrypi.local
    ```

    or depending on your network settings try

    ```bash
    ssh pi@raspberrypi
    ```

3. Update and reboot

    ```bash
    sudo apt update && sudo apt full-upgrade && sudo reboot
    ```

4. Optionally overclock the Raspberry Pi 4.

    Though not a requirement, the machine learning inference times will be improved by overclocking the Raspberry Pi 4. You will need a Raspberry Pi heat sink if you overclock. See the [How to overclock Raspberry Pi 4](https://magpi.raspberrypi.org/articles/how-to-overclock-raspberry-pi-4) article for more information. 

    I use the following settings in the ```/boot/config.txt```.

    ```text
    over_voltage=6
    arm_freq=2000
    gpu_freq=700
    ```

    and reboot.

---

## Install Docker on the Raspberry Pi

1. Log into your Raspberry Pi

    ```bash
    ssh pi@raspberrypi.local
    ```

2. From the SSH session run the following command.

    ```bash
    curl -sSL get.docker.com | sh && sudo usermod pi -aG docker && sudo reboot
    ```

---

## Install the Docker Registry on the Raspberry Pi

Azure IoT Edge relies on Docker images being distributed from a [Docker Registry](https://docs.docker.com/registry/). In production you would deploy Docker images from a registry such as [Azure Container Registry](https://azure.microsoft.com/en-us/services/container-registry/?WT.mc_id=julyot-tir-dglover).

When you are developing an Azure Iot Edge module it is faster to install a local container registry on the Raspberry Pi and deploy Docker images from the local registry to Azure IoT Edge.

1. Log into your Raspberry Pi

    ```bash
    ssh pi@raspberrypi.local
    ```

2. From the SSH session, run the following command.

    ```bash
    docker run -d -p 5000:5000 --restart=always --name registry registry:2
    ```
3. **Do NOT close the SSH session.**

---

## Install Azure IoT Edge on the Raspberry Pi

Be sure to review the full [Install the Azure IoT Edge runtime on Debian-based Linux systems](https://docs.microsoft.com/en-us/azure/iot-edge/how-to-install-iot-edge-linux?WT.mc_id=julyot-tir-dglover) guide.

1. Log into your Raspberry Pi

    ```bash
    ssh pi@raspberrypi.local
    ```

2. Install the *libssl1.0.2* library required by Azure IoT Edge.

    ```bash
    sudo apt-get install libssl1.0.2
    ```

3. Copy the following bash command block, and paste into the SSH session to install Azure IoT Edge. Press <kbd>Enter</kbd> to start the installation process.

    ```bash
    curl https://packages.microsoft.com/config/debian/stretch/multiarch/prod.list > ./microsoft-prod.list && \
    sudo cp ./microsoft-prod.list /etc/apt/sources.list.d/ && \
    curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg && \
    sudo cp ./microsoft.gpg /etc/apt/trusted.gpg.d/ && \
    sudo apt-get update && \
    sudo apt-get -y install iotedge
    ```

---

## Configure the Azure IoT Edge device

You need to configure the Azure IoT Edge connection string.

1. Open the Azure IoT Edge config file.

    ```bash
    sudo nano /etc/iotedge/config.yaml
    ```

2. Scroll down to the Manual provisioning configuration section.

    ```yaml
    # Manual provisioning configuration
    provisioning:
        source: "manual"
        device_connection_string: "<ADD DEVICE CONNECTION STRING HERE>"
    ```

3. Update the **device_connection_string** property with the Azure IoT Edge Connection string you saved to Notepad.

4. Press <kbd>ctrl + X</kbd>, then **y** to confirm you wish to save the config.
5. Press <kbd>Enter</kbd> to confirm the file name

6. Reboot the Raspberry Pi

    ```bash
    sudo reboot
    ```

---

## Clone the image recognition solution to the Raspberry Pi

1. Log into your Raspberry Pi

    ```bash
    ssh pi@raspberrypi.local
    ```

2. From the SSH session, install the git client.

    ```bash
    sudo apt install -y git
    ```

3. From the SSH session, clone the solution repository to the Raspberry Pi

    ```bash
    git clone https://github.com/gloveboxes/Create-a-talking-image-recognition-solution-with-Azure-IoT-Edge-Azure-Cognitive-Services.git
    ```

---

**[NEXT](../module_3_set_up_computer/README.md)**

---
