# Photo Station Automation Program 
## Description
This project intergrates photo taking, photo uploading and database synchronization functions for finds recording process in APSAP photo station. The program aims to provide a easy-to-use and a user-friendly platform for user to record finds efficiently while reducing the requirement for the operator.
&nbsp;
* Main Intergrated functions
  * Photo taking and video preview (previous done by Canon EOS)
  * Photo preview (new)
  * Weight measuring (previous done by Bonita Software)
  * Photo uploading to local shared drive (new) (auto)
  * Create find object on server after recording the find (new)
&nbsp;
## Table of Contents
* [1.Installation](##1Installation)
* [2.Configuration](##2Configuration)
* [3.Usage](##3Usage)
* [4.Credits](##4Credits)
* [5.Reference](##5Reference)
&nbsp;
## 1.Installation 
### 1.1 Installation from FLASH DISK/Onedrive
Install by copy and paste the whole project folder from Flash Disk/Onedrive, then it is good to go. All dependencies should be included.
### 1.2 Installation from Biginning
(To be done by Eric)
&nbsp;
## 2.Configuration 
This section is for both hardware and software)
### 2.1 Hardware Configuration
* Canon Camera
  * Connect charging cable to camera and usb-micro_usb cable to computer.
  * Make sure SD card is in the camera.
  * Change to manual focus: menu -> shooting settings -> 6 -> Focus mode to "MF".
  * After setting up the camera, manually focus the camera to the plate until you can see the words on color board most clearly.
  * To restore the setting, change focus mode to "AF".
* Electronic Scale
  * Connect cable with computer and scale
  * Continuous signal setting: press "ON/OFF" -> when starting (loading 999999 to 111111)(see reference 5.3) -> press "TARE" "TARE" "TARE" and "UNIT" -> it should be showing "01-Diu" -> press "Zero" until it shows "09-Ode" -> Press "CAL/PRT" to confirm-> Press "ZERO" until it shows "3" -> Press "CAL/PRT" to confirm -> Turn off the scale and open it, it should be set.
* LED light
  * Follow the instruction of your supervisor.
### 2.2 Software Configuration
* Check if the lab NAS drive is connected and mapped to local machine.
&nbsp;
## 3.Usage
[Demo video]()
&nbsp;
## 4.Credits
* LI Haochen, Harry - Software, Photo uploading function and server synchronization function
* JIN Yushang, Eric - Hardware, Photo taking function, livestream and preview function, weight measurement function
* FAN Zheyu, Uky - Software, GUI backend design, GUI frontend design, logic optimization
* SONG Yichuan, Tiger - Software, GUI design
* Special thanks to Gabriel Paul Getzie for helping on test server related issue.
&nbsp;
## 5.Reference
### 5.1 From Test Server Builder
#### [Python code: testing backend](https://github.com/ggetzie/aslcv2_be/blob/master/main/test_local.py)
#### [Restricted material and category combinations for uploading](https://j20200007.kotsf.com/asl/api/find/mc/)
### 5.2 Test Server Related
#### [Test server](https://j20200007.kotsf.com/asl/)
#### [API.cs](https://github.com/ggetzie/ObjectPhotoUploader/blob/master/ObjectPhotoUploader/API.cs)
#### Test server login: username:*autophoto*;password:*Armenia1*
### 5.3 Hardware Related
#### [Electronic Scale Continuous Streaming Setting](https://forum.arduino.cc/t/interfacing-with-scales-rs232-gm-series-scales-bonita-labs-gmb-flb-forelibra-solved/906449/8)
