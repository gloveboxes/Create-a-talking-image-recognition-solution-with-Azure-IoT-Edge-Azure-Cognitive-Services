# Module 6: Camera settings

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

The solution works best when you turn off the camera auto focus and set the line frequency.

You will see in the repo that you cloned to the Raspberry Pi that there is a **set-camera.sh**.

The settings you choose will depend on your camera.

But for reference these are the settings I use.

Note, **power_line_frequency=1** is 50Hz.

```bash
v4l2-ctl --set-ctrl=power_line_frequency=1
v4l2-ctl --set-ctrl=focus_auto=0
v4l2-ctl --set-ctrl=brightness=150
v4l2-ctl --set-ctrl=contrast=7
v4l2-ctl --set-ctrl=saturation=100
v4l2-ctl --set-ctrl=focus_absolute=20
v4l2-ctl --set-ctrl=zoom_absolute=20
```

You can find out more about these settings at [Manual USB camera settings in Linux](https://www.kurokesu.com/main/2016/01/16/manual-usb-camera-settings-in-linux/)

These settings are reset on reboot so you will need to reload at bootup.

The easist way to do this is add the required camera settings to the /etc/rc.local file.


---

**[Home](../../README.md)**

---