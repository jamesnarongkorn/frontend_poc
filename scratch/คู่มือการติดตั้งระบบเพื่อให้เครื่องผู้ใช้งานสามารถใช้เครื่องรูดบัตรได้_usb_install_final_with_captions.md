## คู่มือการติดตั้งเครื่องเพื่อให้เครื่องของผู้ใช้งานชำระเงินผ่านบัตรเครดิตได้ (MIS2 Link POS Version 1.1.0)
- 1. Software Requirement
- 1.1. Windows XP, Windows 7 (32-bit และ 64-bit) หรือ Windows 10 (32-bit และ 64-bit) (วิธีตรวจสอบเวอร์ชั่นของ Windows ตามข้อ 5)
- 1.2. JRE runtime ต้องมีเพื่อให้ผู้ใช้สามารถรัน oracle form ได้ ต้องทำการติดตั้งก่อนกรณีที่ยังไม่สามารถรัน oracle form ได้ หรือ download ได้ที่ http://misweb.bma.go.th/download/MISEDCTEMP/jdk-6u45-windows-i586.exe
- 1.3. Driver สำหรับเครื่องรูดบัตร (rxtxSerial.dll)

## การติดตั้ง JRE runtime (กรณีไม่สามารถเข้าระบบการเงินรับได้)
- 2.1. ทำการ download โปรแกรม JRE runtime ให้ผู้ใช้งานเข้าไปที่หน้าเขียว http://misweb.bma.go.th/ และทำการ download โปรแกรม โดยให้กดที่คำว่า Download Java JDK ตรงด้านล่างซ้ายมือตรงหน้าเขียวดังภาพ หรือ Download จาก http://misweb.bma.go.th/download/MISEDCTEMP/java_jdk6.exe

<!-- image: A screenshot containing the letterhead information for Bangkok, including contact telephone numbers and the date '29 สิงหาคม 2566'. -->

<!-- image: A screenshot highlighting the 'Download Java JDK' option within a list of downloadable programs. The option is enclosed in a red rectangle. -->

- 2.2. เมื่อคลิกที่ Download Jre จะปรากฏหน้าจอดังภาพ ให้กดปุ่ม Save

<!-- image: A 'Save As' dialog box, showing the 'Downloads' folder and the 'jdk-6u45-windows-i586.exe' file selected for saving as an 'Application'. The 'Save' button is highlighted. -->

- 2.3. เมื่อทำการ Download เรียบร้อยแล้วให้ทำการติดตั้งโดยการดับเบิลคลิกที่ไฟล์ดังกล่าว

<!-- image: A screenshot of Windows File Explorer showing an application named 'jdk-6u45-windows-i586.exe'. Its file type is displayed as 'Application'. -->

จะปรากฏหน้าจอดังภาพ แล้วทำการกดปุ่ม Next

<!-- image: A screenshot showing the initial setup screen for 'Java(TM) SE Development Kit 6 Update 45'. The 'Next >' button is outlined with a red box, indicating the next step in the installation process. -->

- 2.4. จะปรากฏหน้าจอดังภาพ ทำการกดปุ่ม Next

<!-- image: A screenshot of the Java SE Development Kit 6 Update 45 installation wizard, displaying the 'Custom Setup' screen where users can select optional features to install. The 'Next' button is highlighted with a red outline. -->

- 2.5. จะปรากฏหน้าจอการติดตั้ง

<!-- image: A window displaying the progress of the 'Java(TM) SE Development Kit 6 Update 45' installation, showing the status as 'Extracting Installer' and a partially filled green progress bar. -->

- 2.6. เมื่อทำการติดตั้งสำเร็จจะปรากฏหน้าจอดังภาพ ทำการกดปุ่ม Next

<!-- image: A screenshot of the Java Setup 'Destination Folder' window. The default installation path is 'C:\Program Files\Java\jre6\'. The 'Next' button is available to proceed with the installation. -->

- 2.7. จะปรากฏหน้าจอการติดตั้ง

<!-- image: A screenshot of the Java installation progress window, indicating that the installer is extracting files. The window also displays the message '3 Billion Devices Run Java' and features the Oracle logo. -->

- 2.8. เมื่อทำการติดตั้งสำเร็จจะปรากฏหน้าจอดังภาพ
- 2.9. หลังจากนั้นทำการตั้งค่าเพื่อให้เครื่องสามารถใช้งาน java ได้ โดยการคลิกขวาที่ My computer

<!-- image: A completion screen of the Java SE Development Kit 6 Update 45 installation. It indicates a successful installation and suggests clicking 'Next Steps' to access tutorials and documentation. A 'Close' button is visible at the bottom. -->

และเลือก Properties

<!-- image: A screenshot of the Windows start menu, showing the 'Computer' menu item selected, which displays a context menu including 'Open', 'Manage', 'Scan for viruses', 'Map network drive', 'Show on Desktop', 'Rename', and 'Properties'. -->

- 2.10. จะปรากฏหน้าจอตามภาพด้านล่าง จากนั้นให้ผู้ใช้งานคลิกเลือก Advanced system settings

<!-- image: A screenshot of the Windows System control panel displaying basic computer information, with 'Advanced system settings' highlighted on the left navigation panel. -->

- 2.11. จะปรากฏหน้าจอด้านล่าง ให้คลิกที่ปุ่ม Environment Variables

<!-- image: A screenshot of the 'Advanced' tab within the 'System Properties' window. The 'Environment Variables...' button is highlighted with a red box. -->

- 2.12. หลังจากที่คลิกที่ปุ่ม Environment Variables จะปรากฏหน้าจอด้านล่าง ทำการเลือก variable = Path แล้วกดปุ่ม Edit

<!-- image: A screenshot of the 'Environment Variables' window in Windows, showing both user and system variables. The 'Path' variable is selected under 'System variables', and the 'Edit...' button is highlighted with a red box. -->

- 2.13. หลังจากที่เลือกที่ชื่อ Path กดปุ่ม Edit แล้วให้ทำการแก้ไข Variable value ของเครื่อง โดยการนำ java path มาไว้ด้านหน้าสุด หรือต่อท้ายสุดของ Variable value (ไม่ต้องลบค่าเดิมของ Variable value) ในที่นี้ java path คือ C:\Program Files\Java\jdk1.6.0_45\bin

<!-- image: A screenshot of the 'Edit System Variable' window in Windows, showing the 'Path' variable being edited to include 'bin;C:\Program Files\Java\jdk1.6.0_45\bin'. -->

จากนั้นกดปุ่ม OK จะปรากฏหน้าจอตามภาพด้านล่าง

<!-- image: A screenshot of the 'Environment Variables' dialog box, showing user and system variables, with 'Path' selected under 'System variables', and the 'OK' button highlighted. -->

จากนั้นกดปุ่ม OK เพื่อสิ้นสุดการแก้ไข

## วิธีการตรวจสอบเวอร์ชั่นโปรแกรม
- 3.1. เปิดโปรแกรม Control Panel ของ Windows ดังภาพตัวอย่าง

<!-- image: A desktop icon labeled "Control Panel", featuring a blue icon with a pie chart and slider bars. -->

- 3.2. คลิกเปิด 'Programs and Features' ในวงกลมสีแดงดังภาพ

<!-- image: A screenshot of the Windows Control Panel with the 'Programs and Features' icon highlighted by a red box. -->

- 3.3. ตรวจสอบชื่อและเวอร์ชั่นของโปรแกรมดังต่อไปนี้
- 3.3.1. โปรแกรม Driver เครื่องรูดบัตร
หากในเครื่องไม่มีโปรแกรมดังรูป หรือมีโปรแกรมชื่อ 'VeriFone Vx Installer version 1.0.0.37' ให้ทำการติดตั้งโปรแกรม Driver เครื่องรูดบัตรใหม่ ตามข้อ 4.2

<!-- image: A view of the 'Programs and Features' list in Windows, showing 'VerifoneUnifiedDriverInstaller64 Build 2' version '5.0.4.0'. -->

- 3.3.2. โปรแกรมเชื่อมต่อกับเครื่องรูดบัตร (MIS2 Link POS)
หากในเครื่องไม่มีโปรแกรมดังรูป หรือมีโปรแกรมชื่อ 'MIS2 edcCall' หรือ โปรแกรมชื่อ 'MISEDCTEMP' ให้ทำการติดตั้งโปรแกรมเชื่อมต่อกับเครื่องรูดบัตรใหม่ ตามข้อ 4.1

<!-- image: A screenshot of the Windows 'Programs and Features' control panel, listing installed software with 'MIS2 Link POS' highlighted in a red box. -->

## การติดตั้งโปรแกรมที่เชื่อมต่อกับเครื่องรูดบัตร (MIS2 Link POS)
**โปรดทำการตรวจสอบเวอร์ชั่นของโปรแกรมก่อนทำขั้นตอนนี้ ตามข้อ 3**

(กรณีในเครื่องมีโปรแกรมที่เชื่อมต่อกับเครื่องรูดบัตร เวอร์ชั่นเก่า เช่น 'MIS2 edcCall' หรือ 'MISEDCTEMP' ให้ถอนการติดตั้งตามข้อ 4.1.1 กรณีไม่มีโปรแกรมที่เชื่อมต่อกับเครื่องรูดบัตร ให้ข้ามไปที่ข้อ 4.1.8)

เวอร์ชั่นล่าสุดชื่อ MIS2 Link POS เวอร์ชั่น 1.1.0

- 4.1.1. เปิดโปรแกรม Control Panel ของ Windows ดังภาพตัวอย่าง

<!-- image: A desktop icon labeled 'Control Panel', displaying a blue icon with a pie chart and slider controls. -->

- 4.1.2. คลิกเปิดโปรแกรมในวงกลมสีแดงดังภาพ

<!-- image: A screenshot of the Windows Control Panel, with the 'Programs and Features' icon highlighted by a red rectangle. -->

- 4.1.3. ดับเบิลคลิกที่โปรแกรม 'MIS2 edcCall' หรือ 'MISEDCTEMP'

<!-- image: A screenshot of the Windows 'Programs and Features' window, showing the installed programs list. The 'MIS2 edcCall' program is highlighted. The text below explains the name of the program is either 'MIS2 edcCall' or 'MISEDCTEMP'. -->

- 4.1.4. จะปรากฏหน้าจอดังภาพ จากนั้นคลิก Next

<!-- image: A screenshot of the MIS2 edcCall Setup Wizard. The initial screen welcomes the user and explains that the wizard can change or remove MIS2 edcCall features. The 'Next' button is highlighted with a red box. -->

- 4.1.5. จะปรากฏหน้าจอดังภาพ จากนั้นเลือก Remove

<!-- image: A dialog box titled 'MIS2 edcCall Setup Wizard' providing options to 'Modify, Repair, or Remove installation'. The 'Remove' option, highlighted by a red box, is currently selected, indicating the user's intention to uninstall the 'MIS2 edcCall' software. -->

- 4.1.6. จะปรากฏหน้าจอดังภาพ จากนั้นคลิก Remove

<!-- image: A dialog titled 'MIS2 edcCall Setup Wizard' with the prompt "Begin remove of MIS2 edcCall". The 'Remove' button is highlighted with a red rectangle. -->

- 4.1.7. จะปรากฏหน้าจอดังภาพ จากนั้นคลิก Finish

<!-- image: A window displaying the completion of the MIS2 edcCall removal, with the message "MIS2 edcCall has been successfully removed." and a 'Finish' button highlighted in a red box. -->

- 4.1.8. ทำการดาวน์โหลดโปรแกรม จากหน้าเขียว http://misweb.bma.go.th/ หรือเข้า link โดยตรง http://misweb.bma.go.th/download/MISEDCTEMP/usb/MIS2_EDC.zip
- 4.1.9. ทำการแตกไฟล์ MIS2_EDC.zip ออก จะได้ไฟล์ MIS2 EDC.exe ดังภาพ

<!-- image: A Windows desktop icon labelled 'MIS2 EDC.exe'. The icon image depicts a payment terminal with a credit card behind it, overlaid with a blue and yellow shield graphic. -->

- 4.1.10. ทำการติดตั้ง โดยคลิกที่ MIS2 EDC.exe จะปรากฏหน้าจอดังภาพ จากนั้นกดปุ่ม Yes

<!-- image: A User Account Control dialog box asking if you want to allow an app from an unknown publisher to make changes to your device. The app listed is 'MIS2 EDC.exe', and the 'Yes' button is highlighted with a red box. -->

- 4.1.11. ทำการติดตั้ง โดยดับเบิลคลิกที่ MIS2 EDC.exe จะปรากฏหน้าจอดังภาพ จากนั้นกดปุ่ม Next

<!-- image: A screenshot of the MIS2 Link POS Setup Wizard, with the welcome message and an explanation of the wizard's purpose. The 'Next' button is highlighted to proceed with the installation. -->

- 4.1.12. จะปรากฏหน้าจอดังภาพ จากนั้นเลือก Typical

<!-- image: A dialog box titled "MIS2 Link POS Setup Wizard" prompting the user to choose the setup type, with options 'Typical' to start the installation of default features, and 'Custom' to select which features are installed. The 'Typical' option is surrounded by a red box. -->

- 4.1.13. จะปรากฏหน้าจอดังภาพ จากนั้นกดปุ่ม Next

<!-- image: A window titled 'MIS2 Link POS Setup Wizard', prompting the user to select the installation folder, which defaults to C:\MISEDCTEMP\. It displays the total space required (4.67 MB), available space (83 GB), and remaining free space (83 GB) on the drive, with 'Next >' highlighted for advancing the installation. -->

- 4.1.14. จะปรากฏหน้าจอดังภาพ จากนั้นกดปุ่ม Install

<!-- image: A screenshot showing the MIS2 Link POS Setup Wizard. The window prompts the user to begin the installation by clicking 'Install', review settings by clicking 'Back', or exit the wizard by clicking 'Cancel'. The 'Install' button is emphasized with a red outline. -->

- 4.1.15. จะปรากฏหน้าจอดังภาพ

<!-- image: A screenshot of the 'MIS2 Link POS Setup Wizard' installation dialog box. A progress bar is visible, and the status is 'Validating install'. A 'Cancel' button is available. -->

- 4.1.16. รอจนติดตั้งเสร็จ จะปรากฏหน้าจอ จากนั้นกดปุ่ม Finish

<!-- image: A screenshot showing the successful installation of 'MIS2 Link POS', with a message confirming the installation. A 'Finish' button is visible at the bottom of the window. -->

## การติดตั้ง Driver เครื่องรูดบัตร
(กรณีในเครื่องมีโปรแกรม Driver เวอร์ชั่นเก่า เช่น โปรแกรม 'VeriFone Vx Installer version 1.0.0.37' ให้ทำการถอนการติดตั้ง ตามข้อ 4.2.1 กรณีไม่มีโปรแกรม Driver เวอร์ชั่นเก่า ให้ข้ามไปที่ข้อ 4.2.9)

โปรแกรม Driver เวอร์ชั่นล่าสุด

- 4.2.1. เสียบ USB เครื่องรูดบัตร เปิดโปรแกรม Control Panel ของ Windows ดังภาพตัวอย่าง

<!-- image: A screenshot of the Windows Control Panel icon, which is blue with an image of a pie chart and a set of sliders and buttons. The label 'Control Panel' is below the icon. -->

- 4.2.2. เลือก Device Manager

<!-- image: A screenshot of the Windows Control Panel, with the 'Device Manager' icon highlighted by a red rectangle. -->

- 4.2.3. ไปที่แถบ Port (COM & LPT) จะมี Port ที่ชื่อ VX 520 GPRS Terminal (COM9) ให้คลิกขวาแล้วเลือก Uninstall Device

<!-- image: A screenshot of the Windows Device Manager, with the 'Ports (COM & LPT)' section expanded, showing 'VX 520 GPRS Terminal (COM9)' selected. The contextual menu for the device is open, and the 'Uninstall device' option is highlighted. -->

- 4.2.4. ติ๊กที่ช่อง Delete the driver software for this device แล้วคลิก Uninstall

<!-- image: A screenshot of the 'Uninstall Device' window for 'VX 520 GPRS Terminal (COM9)'. The 'Delete the driver software for this device' checkbox is checked, and the 'Uninstall' button is highlighted by a red rectangle. -->

- 4.2.5. คลิกเปิดโปรแกรมในวงกลมสีแดงดังภาพ

<!-- image: A view of the 'All Control Panel Items' window in Windows, with the 'Programs and Features' icon highlighted by a red rectangle. -->

- 4.2.6. ดับเบิลคลิกที่โปรแกรม 'VeriFone Vx Installer version 1.0.0.37'

<!-- image: A screenshot of the 'Programs and Features' window in Windows, listing installed programs, with 'VeriFone Vx Installer version 1.0.0.37' highlighted. -->

- 4.2.7. คลิก Yes

<!-- image: A confirmation dialog box titled "VeriFone Vx Installer Uninstall" prompting the user to confirm if they want to completely remove VeriFone Vx Installer and all of its components. The dialog has 'Yes' and 'No' buttons. -->

- 4.2.8. คลิก OK

<!-- image: A dialog box stating "VeriFone Vx Installer uninstall complete. Some elements could not be removed. These can be removed manually.". The only option is to click 'OK'. -->

- 4.2.9. ดาวน์โหลด Driver ใหม่ได้ที่หน้าเขียว http://misweb.bma.go.th หรือเข้า link โดยตรง http://misweb.bma.go.th/download/MISEDCTEMP/usb/Driver.rar จากนั้นทำการแตกไฟล์จะได้ไฟล์ดังภาพ

<!-- image: A screenshot displaying a folder icon labeled 'Verifone DriverInstaller-5.0.4.0'. -->

- 4.2.10. ดับเบิลคลิกไฟล์ดังกล่าว จะพบ 2 โฟลเดอร์ ให้ดับเบิลคลิกโฟลเดอร์ที่ตรงกับเวอร์ชั่นของ Windows (ตรวจสอบเวอร์ชั่นของ Windows ตามข้อ 5)

<!-- image: A screenshot displaying two file folders, one labeled "Windows 32 Bit" and the other labeled "Windows 64 Bit". -->

- 4.2.11. ดับเบิลคลิกไฟล์ดังภาพเพื่อทำการติดตั้งโปรแกรม

<!-- image: A view of a Windows Installer Package file named 'VerifoneUnifiedDriverInstaller64.msi' icon, indicating it's a Windows Installer Package. -->

- 4.2.12. จะขึ้นหน้าการติดตั้งโปรแกรมดังรูป คลิก Next

<!-- image: A screenshot of the InstallShield Wizard for VerifoneUnifiedDriverInstaller64 Build 2, with the 'Next' button highlighted in red. -->

- 4.2.13. คลิก Next

<!-- image: A screenshot of the Verifone Unified DriverInstaller64 InstallShield Wizard, on the 'Selecting the serial port name and number' screen, with the Port root name set to 'COM', the Port Number base set to '9' and the 'Single device system' checkbox selected. The 'Next' button is highlighted. -->

- 4.2.14. คลิก Install

<!-- image: A screenshot of the 'Ready to Install the Program' screen in the Verifone Unified Driver Installer, with the 'Install' button highlighted in a red box. -->

- 4.2.15. รอการติดตั้งเสร็จสิ้น

<!-- image: A screenshot of the Verifone Unified Driver Installer showing the progress bar, indicating that the installation is in progress. The message displayed informs the user to wait while the InstallShield Wizard installs the Verifone Unified Driver Installer. -->

- 4.2.16. คลิก Finish

## การเชื่อมต่อและตรวจสอบไฟล์ portName.txt
- 4.3. จากนั้นเสียบเข้ากับเครื่องคอมพิวเตอร์ที่สามารถรันระบบการเงินรับได้ ผ่านสาย USB เสียบปลั๊กให้เรียบร้อยจะสามารถใช้โปรแกรมระบบการเงินรับ ส่งข้อมูลให้กับเครื่องรูดบัตรได้

<!-- image: A screenshot showing the final screen of the Verifone Unified Driver Installer. The InstallShield Wizard has completed installation, and the 'Finish' button is highlighted with a red box. -->

**หากไม่สามารถติดต่อกับเครื่องรูดบัตรได้ เบื้องต้นให้ทำการเช็คไฟล์ portName.txt โดยมีวิธีการดังนี้**
- ดับเบิลคลิกไฟล์ portName.txt โดยไฟล์จะอยู่ที่ C:\MISEDCTEMP\log
- พิมพ์ข้อความ COM แล้วตามด้วยเลขดังรูป โดยให้ตรงกับ Port ของเครื่องใน Device Manager

<!-- image: A screenshot of a folder named "log" within a directory path that includes "MISEDC...", listing the file "portName.txt" as a 'Text Document' with a size of '1 KB', and a 'Date modified' value of '1/9/2566 14:57'. -->

<!-- image: A screenshot of the Windows Device Manager showing the COM ports available, with 'VX 520 GPRS Terminal (COM9)' highlighted, paired with a Notepad window containing the text 'COM9'. -->

- คลิก File > Save
- หลังจากนั้น ทำการทดสอบเครื่องรูดบัตรอีกครั้งในระบบ

<!-- image: A screenshot of the 'File' menu in Notepad. The 'Save' option is highlighted. The keyboard shortcut 'Ctrl+S' is displayed next to 'Save'. -->

## ขั้นตอนการตรวจสอบเวอร์ชั่นของ Windows
- 5.1. Windows 7
- 5.1.1. คลิกขวาที่ My Computer จากนั้นคลิกที่ Properties ตามภาพด้านล่าง

<!-- image: A screenshot of the right-click menu for the 'Computer' icon on a Windows desktop, with 'Properties' highlighted by a red box at the bottom of the menu. -->

**กรณีไม่พบไอคอน My Computer บนหน้าจอ ให้คลิกปุ่ม Start จากนั้นคลิกขวาที่ Computer แล้วคลิกที่ Properties ตามภาพด้านล่าง**

<!-- image: A view of the Windows start menu. The 'Computer' menu item is selected, and a context menu is open, with the 'Properties' option highlighted. -->

- 5.1.2. จะปรากฏหน้าจอ พร้อมรายละเอียดของ Windows ให้ดูรายละเอียดที่หัวข้อ System type จะบอกเวอร์ชั่นของ Windows ที่ใช้งานอยู่

<!-- image: A screenshot of the Windows System information screen, showing 'Acer' as the manufacturer, 'Veriton X480G' as the model, 'Intel(R) Core(TM)2 Duo CPU E8400 @ 3.00GHz' as the processor, '2.00 GB' of installed memory (RAM), and '32-bit Operating System' as the system type. -->

- 5.2. Windows 10
- 5.2.1. คลิกที่ Start <!-- image: A screenshot of the Windows Start Menu, with the 'Settings' option highlighted by a red rectangle. --> แล้วคลิก Setting <!-- image: A screenshot of the Windows 'Settings' menu, with the 'About' option highlighted. -->
- 5.2.2. คลิกที่ System
- 5.2.3. คลิกที่ About ให้ดูรายละเอียดที่หัวข้อ System type จะบอกเวอร์ชั่นของ Windows ที่ใช้งานอยู่

<!-- image: A Windows desktop view of the 'MIS2 EDC.exe' installation file icon, which is orange with a stylized cash register and a Windows security shield overlay. -->

## การถอดการติดตั้งระบบเชื่อมต่อเครื่องรูดบัตร (กรณีไม่สามารถยกเลิกการรับเงินได้)
การถอดการติดตั้งโปรแกรมมี 2 วิธี
1. ถอนการติดตั้งผ่านโปรแกรม MIS2 EDC.exe (เริ่มข้อ 6.1 ถึง 6.8)
2. ถอนการติดตั้งผ่าน Control Panel (เริ่มข้อ 6.9 ถึง 6.14)

**ถอนการติดตั้งผ่านโปรแกรม MIS2 EDC.exe**
- 6.1. เปิดโปรแกรม MIS2 EDC.exe ดังภาพตัวอย่าง

<!-- image: A window with the title 'MIS2 EDC.exe' indicating the file's publisher is unknown and its origin is the hard drive. The 'Yes' button is framed with a red outline, indicating it's the selected option. -->

- 6.2. จะปรากฏหน้าจอดังภาพ จากนั้นคลิก Yes

<!-- image: A screenshot of the MIS2 Link POS Setup Wizard. The window displays a welcome message and prompts the user to click 'Next' to continue the installation or 'Cancel' to exit the wizard. The 'Next' button is highlighted by a red square. -->

- 6.3. จะปรากฏหน้าจอดังภาพ จากนั้นคลิก Next

<!-- image: A screenshot of the MIS2 Link POS Setup Wizard, with the 'Remove' option highlighted by a red box. -->

<!-- image: A screen capture of the 'MIS2 Link POS Setup Wizard' showing the 'Begin remove of MIS2 Link POS' page. The 'Remove' button is highlighted in red. -->

- 6.4. จะปรากฏหน้าจอดังภาพ จากนั้นเลือก Remove
- 6.5. จะปรากฏหน้าจอดังภาพ จากนั้นคลิก Remove

<!-- image: A window titled 'MIS2 Link POS Setup Wizard' indicating the removal process. The message 'Removing MIS2 Link POS...' is displayed, along with the status 'Generating script operations for action:'. A progress bar shows the current progress. The 'Cancel' button is available at the bottom right. -->

- 6.6. จะปรากฏหน้าจอดังภาพ

<!-- image: A screenshot of the 'MIS2 Link POS Setup Wizard' window, confirming successful removal of 'MIS2 Link POS'. The 'Finish' button is highlighted in red. -->

- 6.7. รอถอนการติดตั้งเสร็จสิ้น จะปรากฏหน้าจอดังภาพ จากนั้นคลิก Finish

<!-- image: An icon of the Windows Control Panel as it appears on the desktop. The icon depicts a blue screen with a pie chart graphic and sliders. The text 'Control Panel' is displayed underneath the icon. -->

- 6.8. เมื่อทำการเสร็จสิ้นแล้ว ให้ทำการติดตั้งระบบเชื่อมต่อเครื่องรูดบัตรใหม่อีกครั้งตามขั้นตอนที่ 4.1

**ถอนการติดตั้งผ่าน Control Panel**
- 6.9. เปิดโปรแกรม Control Panel ของ Windows ดังภาพตัวอย่าง

<!-- image: A screenshot of the Windows Control Panel, with the 'Programs and Features' icon highlighted by a red rectangle. -->

- 6.10. คลิกเปิด Program and Features ดังภาพ

<!-- image: A dialog box with the message 'Are you sure you want to uninstall MIS2 Link POS?' and the 'Yes' button highlighted in a red box. -->

- 6.11. ดับเบิลคลิกที่โปรแกรม MISEDCTEMP
- 6.12. จะปรากฏหน้าจอดังภาพ ให้คลิก Yes

<!-- image: A User Account Control dialog box asking if the user wants to allow an app from an unknown publisher to make changes to their device. The file path is 'C:\Windows\Installer\5ff5c13.msi'. The publisher is unknown, and the file origin is the hard drive on the computer. The 'Yes' button is highlighted in red. -->

- 6.13. จะปรากฏหน้าจอดังภาพ จากนั้นคลิก Yes

<!-- image -->

- 6.14. รอถอนการติดตั้งเสร็จสิ้น เมื่อทำการเสร็จสิ้นแล้ว ให้ทำการติดตั้งระบบเชื่อมต่อเครื่องรูดบัตรใหม่อีกครั้งตามขั้นตอนที่ 4.1