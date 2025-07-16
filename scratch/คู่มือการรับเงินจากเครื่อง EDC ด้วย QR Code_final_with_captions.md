## 1. การติดตั้งซอฟต์แวร์

- 1.1. เสียบสาย Adapter เครื่อง EDC เข้ากับปลั๊กไฟ
- 1.2. นำสาย Port USB จากเครื่อง EDC เสียบที่เครื่องคอมพิวเตอร์ที่ใช้โปรแกรมการรับเงิน ดังรูป 1-1
- 1.3. ติดตั้ง Driver สำหรับใช้งานเครื่อง EDC

<!-- image: Two Verifone VX 520c payment terminals are shown side-by-side. The left terminal displays a message in Thai, which translates to "Connect to the computer." The right terminal displays the Main Menu screen with options for QR PAYMENT, credit/debit card, and fund transfers. The screen indicates page 1/3 of the menu. -->
รูป 1-1 หน้าจอเครื่อง EDC พร้อมใช้งาน

## 2. การเข้าใช้งานระบบงานการเงินรับ (MIS2)

2.1. เจ้าหน้าที่ผู้ใช้งานต้องเข้าใช้งาน ผ่านระบบ Single Sign On และเลือกระบบงาน MIS2 ดังรูป 2-1

รูป 2-1 หน้าจอ แสดงการเลือกระบบเข้าใช้งาน

2.2. เลือกระบบงานที่ต้องการใช้งาน <ระบบงานการเงินรับ> จะปรากฏ หน้าจอหลัก ระบบงานการเงินรับ ดังรูป 2-2

รูป 2-2 หน้าจอหลัก ระบบงานการเงินรับ

<!-- image: A low-angle shot of temple spires and a statue, all against a bright blue sky with wispy clouds. -->

## 3. การเข้าใช้งานโปรแกรมการรับเงินรายได้จากใบแจ้งการชำระ

เลือกเมนู <บันทึก / แก้ไขข้อมูล> จากนั้นเลือกเมนู <รับเงินรายได้จากใบแจ้งการชำระ> ดังรูป 3-1 จะปรากฏหน้าจอโปรแกรมรับเงินรายได้จากใบแจ้งการชำระ ดังรูป 3-2

รูป 3-1 เมนูรับเงินรายได้จากใบแจ้งการชำระ

<!-- image: A screenshot of a menu list in Thai, numbered from 01 to 14, listing various payment and banking options. Option 14, "รับเงินรายได้จากใบแจ้งการชำระ," is highlighted in blue. -->

รูป 3-2 หน้าจอโปรแกรมรับเงินรายได้จากใบแจ้งการชำระ

<!-- image: A view of the PTARDT01 'Receipts from Invoice' window. It contains fields for barcode input, invoice details, payment information, document details, and payment methods, with labels and text in Thai. -->

## 4. การตรวจสอบความพร้อมใช้งานเครื่อง EDC กับโปรแกรมรับเงิน

ตรวจสอบเครื่อง EDC พร้อมใช้งานกับโปรแกรมรับเงินรายได้จากใบแจ้งการชำระหรือไม่ ดังรูป 4-1

- 4.1. เลือกประเภทการรับเงิน เป็น 'บัตรเครดิต / เดบิต /ATM' จากข้อมูลเอกสารการเงิน
- 4.2. กดปุ่ม <ทดสอบเครื่อง EDC>
- 4.3. จะปรากฏข้อความ 'เครื่อง EDC พร้อมใช้งาน' แสดงว่าเครื่อง EDC กับโปรแกรมรับเงินรายได้จากใบแจ้งการชำระ พร้อมใช้งานแล้ว

รูป 4-1 หน้าจอระบบทดสอบเครื่อง EDC พร้อมใช้งาน

<!-- image: A screenshot of a software interface in Thai, highlighting three steps: First, 'เลือกประเภทการรับเงิน' (Select Payment Type); second, 'กดปุ่ม ทดสอบเครื่อง EDC' (Press EDC Test Button); and third, a message box indicating 'เครื่อง EDC พร้อมใช้งาน' (EDC device ready). -->

## 5. การค้นหาใบแจ้งการชำระ

การค้นหาใบแจ้งการชำระ สามารถค้นหาได้ตามเงื่อนไข ดังรูป 5-1 รายละเอียดดังนี้

- 5.1. ระบุข้อมูลประเภทรายได้ และต้องระบุข้อมูลที่ต้องการค้นหา อย่างน้อย 1 ใน 3 เงื่อนไข
- 5.2. ระบุ เลขที่บัตรประชาชน/นิติบุคคล ต้องระบุให้ครบ 13 หลัก
- 5.3. ระบุ ชื่อ-นามสกุล เจ้าของใบแจ้งการชำระ ระบุตัวอักษร ที่มีนัยสำคัญในการค้นหา เช่น การระบุชื่อบริษัท หรือระบุนามสกุล เข้าไป โปรแกรมจะค้นหาใบแจ้งการชำระ ที่มีชื่อบริษัท หรือที่มีนามสกุลเดียวกันกับที่ได้ระบุ หากระบุข้อมูลที่ไม่เฉพาะเจาะจงเข้าไป จะส่งผลให้โปรแกรมต้องใช้เวลาในการค้นหามากขึ้น
- 5.4. ระบุ เลขที่ใบแจ้งการชำระ/ใบคำร้องผ่อน ต้องระบุให้ครบ 18 หลัก และต้องตรงกับใบแจ้งการชำระที่ต้องการรับเงิน

รูป 5-1 หน้าจอ การค้นหาใบแจ้งการชำระ

<!-- image: A screenshot of a data entry form with Thai text. The fields are labeled with numbers 1 through 4, indicating the sequence for data input. The fields request, in order, "Type of income", "ID number", "Name Surname", and "Invoice number for payment". -->

- 5.5. กดปุ่ม <ค้นหาใบแจ้งการชำระ> ซึ่งโปรแกรมจะค้นหาใบแจ้งการชำระตามเงื่อนไขที่ระบุ พร้อมตรวจสอบสถานะของใบแจ้งการชำระที่พร้อมรับเงิน และไม่เลยกำหนดชำระ ผลการค้นหามีรายละเอียดดังนี้
    - 5.5.1. กรณีพบข้อมูลใบแจ้งการชำระพร้อมรับเงิน ระบบจะแสดงข้อมูล ดังรูป 5-2
    - 5.5.2. กรณีพบใบแจ้งการชำระที่รับชำระเงินแล้ว โปรแกรมจะแสดงข้อมูล เลขที่ใบแจ้งการชำระ, หน่วยงานรับเงิน, วันที่รับเงิน, เลขที่ใบเสร็จ, จำนวนเงิน ดังรูป 5-3

รูป 5-2 หน้าจอผลการค้นหาใบแจ้งการชำระ

<!-- image: A screenshot of the PTARDT01 software interface, used for receiving income from payment notices, featuring a search panel at the top and a results table showing details of payment records, with annotations pointing to the 'Search Payment Notice' button and highlighting the 'Payment Notice and Receipt' section. -->

<!-- image: A screenshot of an application interface, showing search parameters and a message box that displays payment information for a specific transaction. The message confirms the transaction details, including the payer's name, transaction date, and the amount paid. -->

- 5.5.3. กรณีพบใบแจ้งการชำระที่รับชำระเงินแล้ว แต่อยู่ระหว่างการยืนยันข้อมูลจากธนาคาร เพื่อออกใบเสร็จรับเงิน โปรแกรมจะแสดงข้อมูล เลขที่ใบแจ้งการชำระ, วันที่รับเงิน, จำนวนเงิน ดังรูป 5-4

รูป 5-4 หน้าจอพบใบแจ้งการชำระ รับชำระเงินแล้ว แต่อยู่ระหว่างการยืนยันข้อมูลจากธนาคาร

<!-- image: A screenshot of an application form titled 'PTARDT01' for receiving income from payment notifications. The form includes fields for barcode input, tax type selection (1013), identification number, name, and payment request numbers (5024, 1013, 66, 00000074). A message box is displayed indicating a payment of 15.00 baht has been received and is being verified. An 'OK' button is visible within the message box. -->

- 5.5.4. กรณีพบใบแจ้งการชำระที่ถูกยกเลิกแล้ว โปรแกรมจะแสดงข้อมูล เลขที่ใบแจ้งการชำระที่ถูกยกเลิก ดังรูป 5-5

รูป 5-5 หน้าจอพบใบแจ้งการชำระ ถูกยกเลิก

<!-- image: A screenshot of an application window with a pop-up message in Thai that states: "ใบแจ้งการชำาระ 5049-1018-66/00031700 ถูกยกเลิกแล้ว โปรดตรวจสอบข้อมูลที่ระบบภาษีที่ดินและสิ่งปลูกสร้าง!!!" with the OK button highlighted. -->

- 5.5.5. กรณีพบใบแจ้งการชำระที่เลยกำหนดการรับชำระ โปรแกรมจะแสดงข้อมูล เลขที่ใบแจ้งการชำระ, วันที่ครบกำหนดชำระ ดังรูป 5-6

รูป 5-6 หน้าจอพบใบแจ้งการชำระ เลยกำหนดชำระ

<!-- image: A screenshot of a Thai-language software interface, showing a 'Message' dialog box with a yellow warning icon. The dialog box indicates that payment for invoice 5049-1018-66/00003200 is overdue as of 29/03/2566, and prompts the user to check the land and building tax system data. The 'OK' button is visible at the bottom. -->

- 5.5.6. กรณีไม่พบใบแจ้งการชำระตามที่ได้ระบุเลขที่ใบแจ้งการชำระ โปรแกรมจะแสดงข้อมูล เลขที่ใบแจ้งการชำระที่ไม่พบ ดังรูป 5-7

รูป 5-7 หน้าจอไม่พบใบแจ้งการชำระ ตามที่ได้ระบุเลขที่ใบแจ้งการชำระ

<!-- image: A screenshot showing an error message that reads, "No payment notification data found 5049-1018-66/00003233 in the central payment system, land and building tax system. Please check your search information !!!" -->

- 5.5.7. กรณีไม่พบใบแจ้งการชำระตามที่ได้ระบุเลขที่บัตรประชาชน/เลขที่นิติบุคคล โปรแกรมจะแสดงข้อมูล เลขที่บัตรประชาชน/เลขที่นิติบุคคล ที่ไม่พบ ดังรูป 5-8

รูป 5-8 หน้าจอไม่พบใบแจ้งการชำระ ตามที่ได้ระบุเลขที่บัตรประชาชน/เลขที่นิติบุคคล

<!-- image: A screenshot of a software interface with data entry fields for searching billing information. A message box appears, displaying an error in Thai that translates to 'Billing information for the ID number 1234567890000 in the central revenue system, land and building tax system was not found. Please check your search criteria!!!'. The 'OK' button is visible to close the message box. -->

- 5.5.8. กรณีไม่พบใบแจ้งการชำระตามที่ได้ระบุชื่อ-นามสกุล โปรแกรมจะแสดงข้อมูล ชื่อ-นามสกุล ที่ไม่พบดังรูป 5-9

รูป 5-9 หน้าจอไม่พบใบแจ้งการชำระ ตามที่ได้ระบุชื่อ-นามสกุล

<!-- image: A screenshot of a software interface, showing a message box in Thai that translates to: "No information found for the billing name: Jidapa Yimyem in the central payment system, land and building tax system. Please check your search criteria!!!" with an 'OK' button. -->

- 5.5.9. กรณีพบข้อมูลที่ใบแจ้งชำระมีข้อมูลไม่ครบถ้วน (เฉพาะในการรับชำระภาษีที่ดินและสิ่งปลูกสร้าง) เช่น ที่อยู่, เลขที่หนังสือแจ้งการประเมิน, วันที่หนังสือแจ้งการประเมิน โปรแกรมจะแสดงข้อมูล เลขที่ใบแจ้งการชำระที่พบข้อมูลไม่ครบถ้วน ดังรูป 5-10

รูป 5-10 หน้าจอพบข้อมูลไม่ครบถ้วน มีเฉพาะการรับชำระภาษีที่ดินและสิ่งปลูกสร้าง

<!-- image: A screenshot of an application in Thai language, showing a message window with a warning icon. The message indicates that the system cannot accept the payment because the information is incomplete, and prompts the user to check the address, date/document number, assessment, central payment system, and land and building tax system. The message window has an 'OK' button. -->

## 6. การรับเงิน

การรับเงินทุกประเภทรายได้ สามารถเลือกประเภทรับเงินได้ 5 ประเภท ดังนี้
- 1. เฉพาะเงินสด / ธนาณัติ
- 2. เฉพาะเช็ค / แคชเชียร์เช็ค
- 3. เฉพาะเงินโอน
- 4. เงินสดและเช็ค
- 5. บัตรเครดิต / เดบิต / ATM

## 6.1 การรับเงินด้วย QR Code

- 6.1.1. ระบุเลขที่ใบแจ้งการชำระที่ต้องการรับเงิน จากข้อมูลรายการรับเงิน สามารถระบุได้มากกว่า 1 ใบแจ้งการชำระ ดังรูป 6-1
- 6.1.2. ระบุประเภทการรับเงิน เป็น 'เฉพาะเงินโอน' จากข้อมูลเอกสารการเงิน สามารถระบุได้ 1 ประเภทการรับเงิน ดังรูป 6-1
- 6.1.3. กดปุ่ม 'สร้าง QR Code และพิมพ์ Slip' ดังรูป 6-1

<!-- image: A screenshot of a Thai-language software interface with annotated steps. Step 1 directs the user to select numbers from a listed table, Step 2 instructs to choose the payment method, and Step 3 indicates to select the 'Create QR Code' button. -->

รูป 6-1 หน้าจอการรับเงินรายได้จากใบแจ้งการชำระ

- 6.1.4. เครื่อง EDC จะพิมพ์ THAI QR PAYMENT ตามข้อมูล REF1, REF2, ยอดเงินที่ต้องรับทั้งหมดตามที่ได้ระบุไว้ ดังรูป 6-2

รูป 6-2 THAI QR PAYMENT Slip

<!-- image: A receipt from a Thai QR payment, showing the payment date (12/07/23), time (10:52:43), TID (00036822), Biller ID (376050007511386), Trace No (000217), REF1 (509910186600000018), REF2 (310866000000000000), and the amount (33,882.18 BAHT) highlighted by red boxes. -->

- 6.1.5. ฉีก THAI QR PAYMENT Slip ส่งให้ประชาชน Scan จ่ายเงิน หรือ ให้ประชาชน Scan จ่ายเงินจาก THAI QR PAYMENT Slip ที่เครื่อง EDC
- 6.1.6. โปรแกรมจะแสดงหน้าจอพร้อมรับเงินจากการ Scan จ่ายจากประชาชน ดังรูป 6-3

รูป 6-3 หน้าจอ พร้อมรับเงินจากการ Scan จ่าย จากประชาชน

<!-- image: A screenshot of a data entry form with Thai text labels, including fields for barcode, tax type, ID number, and name. A command prompt window is open in the foreground, displaying the message "please SCAN QR CODE". The form also includes a table with columns for transaction type, document number, bank code, branch code, account number, date, and amount. -->

- 6.1.7. รอกดปุ่มสีแดง หรือ กดปุ่มสีเขียวที่เครื่อง EDC เท่านั้น
- 6.1.8. ให้กดปุ่มสีแดง หากประชาชนไม่ได้ Scan จ่าย หรือแจ้งยกเลิกการ Scan จ่าย ดังรูป 6-4

รูป 6-4 ตำแหน่งกดปุ่มสีแดง ที่เครื่อง EDC

<!-- image: A close-up of a card reader's keypad, emphasizing the red 'X' button (cancel) in the lower-left corner, highlighted by a red square. The label 'กดปุ่มสีแดง' (press the red button) is below the button. -->

- 6.1.9. ให้กดปุ่มสีเขียว หากประชาชน Scan จ่ายเรียบร้อยแล้ว ดังรูป 6-5

รูป 6-5 ตำแหน่งกดปุ่มสีเขียว ที่เครื่อง EDC

<!-- image: A close-up of a PIN entry device keyboard. The green 'Enter' button is highlighted with a red rectangle. Text at the bottom of the image says 'กดปุ่มสีเขียว'. -->

- 6.1.10. โปรแกรมรับเงินจะตรวจสอบรายการที่ประชาชน Scan จ่าย หากตรวจสอบพบรายการที่ Scan จ่าย โปรแกรมรับเงินจะแสดงรายละเอียดให้โดยอัตโนมัติ ดังนี้:
    - 6.1.10.1. แจ้งบันทึกรายการรับเงินสำเร็จ ดังรูป 6-6

รูป 6-6 แจ้งบันทึกรายการรับเงินสำเร็จ

<!-- image: A screenshot of a software interface in Thai, showing payment information with fields for barcode, type of income, ID number, name, bill details, and payment dates. A message box with a yellow exclamation point icon displays the text "บันทึกข้อมูลเสร็จสิ้น", with an "OK" button. The interface displays tables for received money and financial documents, and data entry fields for transaction type, document number, account number, and date. -->

- 6.1.10.2. ออกใบเสร็จรับเงิน ดังรูป 6-7

<!-- image: A Thai tax document with the total amount (16,808.98) highlighted by a red box around a QR code. -->

<!-- image: A tax invoice in Thai script with a QR code and an amount of 17,073.20 baht. -->

รูป 6-7 ออกใบเสร็จรับเงิน

- 6.1.10.3. พิมพ์ Sale Slip รายการที่ถูก Approve ที่เครื่อง EDC ดังรูป 6-8

รูป 6-8 Sale Slip รายการที่ถูก Approve ที่เครื่อง EDC

<!-- image: A receipt in Thai from 'KTB' showing a 'QR CODE PAYMENT', with an amount of '33882.18 THB' and the text 'NO REFUND'. -->

- 6.1.11. ฉีก Sale Slip รายการที่ถูก Approve แนบคู่กับ THAI QR PAYMENT Slip ดังรูป 6-9

รูป 6-9 Sale Slip รายการที่ถูก Approve แนบคู่กับ THAI QR PAYMENT Slip

<!-- image: A receipt showing a Thai QR payment for 33,882.18 BAHT, with reference numbers REF1: 509910186600000018 and REF2: 310866000000000000 highlighted in red. -->

## 6.2 การรับเงินด้วยบัตรเครดิต/เดบิต/ATM

- 6.2.1. จากหน้าจอโปรแกรม ให้เลือกข้อมูลรายการรับเงินในช่อง 'บัตรเครดิต / เดบิต /ATM' โดย:
    - ระบุเลขที่ใบแจ้งการชำระที่ต้องการรับเงิน จากข้อมูลรายการรับเงิน สามารถระบุได้มากกว่า 1 ใบแจ้งการชำระ ดังรูป 6-10
    - ระบุประเภทการรับเงิน เป็น 'บัตรเครดิต / เดบิต /ATM' ดังรูป 6-10
    - ระบุธนาคาร โดยกดปุ่มเพื่อรับชำระเงินผ่านบัตรเครดิต/เดบิต/ATM ดังรูป 6-10
    - กดปุ่ม 'ยืนยันการรูดบัตร' ดังรูป 6-10

รูป 6-10 หน้าจอเลือกข้อมูลรายการรับเงิน ช่อง 'บัตรเครดิต / เดบิต / ATM'

<!-- image: A screenshot of a software interface in Thai, displaying a form for receiving payments, with sections for entering invoice details (1), selecting payment types (2), specifying the bank (3), and a button to confirm the card swipe (4). A row is selected in the invoice details table. -->

- 6.2.2. โปรแกรมจะแสดงหน้าจอพร้อมชำระเงินผ่าน 'บัตรเครดิต/เดบิต/ATM' ดังรูป 6-11

รูป 6-11 หน้าจอพร้อมรับเงินจากบัตร จากประชาชน

<!-- image: A software application window with Thai text fields for data entry, including fields for barcode, identification number, and name, overlaid by a Windows command prompt window displaying the message 'please insert card'. -->

- 6.2.3. เครื่อง EDC จะปรากฏข้อความ ดังรูป 6-12 ให้ผู้ใช้งานทำการรูดบัตร 'บัตรเครดิต/เดบิต/ATM' บนเครื่อง EDC

รูป 6-12 หน้าจอเครื่อง EDC แสดงข้อความ เพื่อสร้าง QR Code

<!-- image: A close-up of a Verifone VX 520c card reader device. The screen displays a message in Thai, presenting options to connect to a computer, insert/swipe/enter card number, or press '*' for QR transactions. The keypad is visible below the screen. -->

- 6.2.4. กรณีรูดด้วยบัตรเดบิตหรือบัตร ATM เครื่อง EDC จะปรากฏหน้าจอให้ใส่รหัสของผู้รับชำระ ดังรูป 6-13 กรณีบัตรเครดิต ให้ทำขั้นตอนดังรูป 6-14

รูป 6-13 หน้าจอเครื่อง EDC แสดงข้อความ ใส่รหัสบัตรเครดิต/เดบิต/ATM

<!-- image: A Verifone VX 520c credit card terminal. The screen reads 'รายการขาย', which means 'sales transactions', and asks for a 'ใส่รหัส', or 'password'. An asterisk password is being entered. -->

- 6.2.5. เมื่อระบุรหัสผ่านเรียบร้อยแล้ว เครื่อง EDC จะปรากฏหน้าจอรายละเอียดข้อมูลบัตรเดบิต/เครดิต และยอดรายการที่ต้องการรับชำระ จากนั้นกดปุ่มสีเขียว ดังรูป 6-14

รูป 6-14 หน้าจอเครื่อง EDC แสดงรายละเอียดข้อมูลบัตรเดบิต/เครดิต

<!-- image: A screenshot of a Verifone VX 520C credit card terminal, highlighting the green 'enter' key, with a screen showing a transaction request for 5,316.00 with card details. -->

- 6.2.6. เมื่อทำการกดปุ่ม Enter ในเครื่อง EDC หรือปุ่มสีเขียวเรียบร้อยแล้ว เครื่อง EDC จะทำการประมวลผลรับข้อมูล ดังรูป 6-15 เมื่อเสร็จสิ้น เครื่องจะประมวลผลแสดงข้อความ 'รายการสำเร็จ' ดังรูป 6-16

รูป 6-15 หน้าจอเครื่อง EDC แสดงรายละเอียดข้อมูลบัตรเดบิต/เครดิต

<!-- image: A Verifone VX 520C payment terminal screen displaying a transaction in Thai, including the card number '4117 08xx xxxx 0200', the amount '5,316.00', and the expiry date '2606'. -->

รูป 6-16 หน้าจอเครื่อง EDC แสดงรายการสำเร็จ

<!-- image: A screenshot of a Verifone VX 520C credit card terminal. The screen displays the text "รายการสําเร็จ" (Transaction successful) and "กำลังยิมพ์.." (Printing...). The terminal's keypad is visible below the screen. -->

- 6.2.7. ตรวจสอบข้อมูลเพื่อยืนยันบัตรอีกครั้ง จากนั้นทำการกดปุ่มยืนยันสีเขียว เพื่อทำการพิมพ์สำเนา Sale Slip ให้ผู้ชำระ ดังรูป 6-17

รูป 6-17 หน้าจอเครื่อง EDC พิมพ์ใบเสร็จสำหรับผู้ชำระ

<!-- image: A Verifone VX 520c credit card terminal. The screen displays Thai text, and the green 'Enter' button in the lower-right corner is highlighted by a red square and an arrow with Thai text instructing the user to press the green button. -->

- 6.2.8. พิมพ์ Sale Slip รายการที่ถูก Approve ที่เครื่อง EDC
    - 6.2.8.1. 'ส่วนที่ 1 เก็บไว้เป็นหลักฐานให้หน่วยงาน ให้ผู้ชำระกรอกลายเซ็นกำกับในส่วน Signature ใน Sale Slip' ดังรูป 6-18
    - 6.2.8.2. 'ส่วนที่ 2 เป็นสำเนา Sale Slip ที่ต้องยื่นให้แก่ผู้ชำระ' ดังรูป 6-18

รูป 6-18 หน้าจอเครื่อง EDC แสดงรายละเอียดข้อมูลบัตรเดบิต/เครดิต

<!-- image: A side-by-side comparison of two KTB (Krungthai Bank) credit card receipts. The left receipt is labeled "ส่วนเก็บไว้เป็นหลักฐานข้อมูลการชำระ" (for data storage) and the right receipt is labeled "ส่วนสำเนาให้ผู้ชำระ" (copy for the payer). The highlighted area on the left receipt includes a signature line and a statement acknowledging satisfactory receipt of goods/services, with a note that indicates the payer's signature is required. -->

- 6.2.9. หลังจากเครื่อง EDC สร้างใบเสร็จรับเงิน/Sale Slip เรียบร้อย ในส่วนโปรแกรมรับเงินรายได้จากใบแจ้งการชำระ โปรแกรมแสดงข้อความ 'บันทึกข้อมูลเสร็จสิ้น' และระบบจะทำการสร้างใบเสร็จในระบบให้อัตโนมัติ ดังรูป 6-19 และ รูป 6-20

รูป 6-19 หน้าจอข้อมูลรายการรับเงิน พิมพ์ QR Code เสร็จสิ้น

<!-- image: A screenshot of an application window, possibly for financial transactions, featuring data tables, input fields, and a popup message box with a yellow exclamation icon, stating "บันทึกข้อมูลเสร็จสิ้น" (Record completed) and an OK button. -->

รูป 6-20 ใบเสร็จในระบบงานการเงินรับ

<!-- image: A Thai-language document with the text "บัตรเครดิต********5,316.00 บาท" highlighted in a red box. -->

## 6.3 การรับเงินผ่าน QR Code แบบไม่เชื่อมโยง

### 6.3.1 ตรวจสอบการรับเงินผ่าน QR Code แบบไม่เชื่อมโยง
- 6.3.1.1. ตรวจสอบการรับเงินผ่าน QR Code แบบไม่เชื่อมโยง ผู้ใช้งานจะต้องทำการตรวจสอบการชำระเงินผ่านเครื่อง EDC
- 6.3.1.2. จากหน้าจอเครื่อง EDC ให้ผู้ใช้งานเลือก ข้อ 1) QR PAYMENT กดหมายเลข 1 ที่เครื่อง EDC ดังรูป 6-21
- 6.3.1.3. เมื่อกดหมายเลข 1 เรียบร้อยแล้ว ให้ผู้ใช้งานเลือก ข้อ 3) ตรวจสอบการชำระเงิน กดหมายเลข 3 ที่เครื่อง EDC จะปรากฏหน้าจอ ดังรูป 6-22
- 6.3.1.4. เมื่อกดหมายเลข 3 เรียบร้อยแล้ว ให้นำเลข Trace No. ใน Sale Slip ไปตรวจสอบโดยใส่หมายเลขสลิป (Trace No) จากนั้นกดปุ่มสีเขียวเพื่อยืนยันการตรวจสอบ จะปรากฏหน้าจอ ดังรูป 6-23
- 6.3.1.5. เมื่อผู้ชำระชำระเรียบร้อย เครื่อง EDC จะปรากฏดังรูป 6-24
- 6.3.1.6. ผู้ใช้งานทำการบันทึกการรับเงินผ่าน QR Code ได้ตามข้อ 6.3.2
- 6.3.1.7. เมื่อผู้ชำระชำระไม่สำเร็จ เครื่อง EDC จะปรากฏดังรูป 6-25
- 6.3.1.8. ผู้ใช้งานแจ้งรายการชำระเงินไม่เสร็จกับผู้ชำระภาษี เพื่อตรวจสอบการโอนเงิน

<!-- image: A screenshot of a Verifone VX 520c payment terminal with the main menu displayed. '1) QR PAYMENT' is highlighted on the screen, and the number '1' button on the keypad is also highlighted. The text in the lower left translates to 'Press button number 1'. -->

รูป 6-21 หน้าจอเริ่มตรวจสอบการชำระเงิน

<!-- image: A Verifone VX 520c credit card terminal, with the screen displaying a menu in Thai. Option 3, "ตรวจสอบการชำระเงิน" (Check Payment), is highlighted. A red box indicates the number '3' key on the keypad, accompanied by a callout in Thai, "กดปุ่มหมายเลข 3" (Press button number 3). -->

รูป 6-22 หน้าจอเริ่มตรวจสอบการชำระเงิน

<!-- image: A picture showing a receipt printer with a sales slip that says "Trace No.: 000293" next to the device's screen that reads "000293" for the user to enter and then press the green button. -->

รูป 6-23 หน้าจอตรวจสอบการชำระเงินโดยหมายเลขสลิป

<!-- image: A Verifone VX 520c payment terminal displaying the Thai phrase "รายการสำเร็จ" on its screen, indicating a successful transaction. The terminal's keypad is visible. -->

รูป 6-24 หน้าจอตรวจสอบการชำระเงิน รายการสำเร็จ

<!-- image: A screenshot of a Verifone VX 520c payment terminal displaying an error message on its screen, 'Error Response Code 90001'. The keypad and card reader slot are also visible. -->

รูป 6-25 หน้าจอตรวจสอบการชำระเงิน รายการไม่สำเร็จ

### 6.3.2 บันทึกการรับเงินผ่าน QR Code แบบไม่เชื่อมโยง
- 6.3.2.1. โปรแกรมหน้าจอการเลือกข้อมูลรายการรับเงิน ช่อง 'เฉพาะเงินโอน' กรณี 'รับผ่าน QR Code แบบไม่เชื่อมโยง'
- 6.3.2.2. ค้นหาใบแจ้งการชำระ สามารถระบุได้มากกว่า 1 ข้อมูลที่ต้องการรับเงิน จากนั้นกดปุ่ม 'ค้นหาใบแจ้งชำระ' ดังรูป 6-26
- 6.3.2.3. เลือก 'ข้อมูลรายการรับเงิน' สามารถระบุได้มากกว่า 1 ใบแจ้งการชำระ ดังรูป 6-26
- 6.3.2.4. ระบุประเภทการรับเงิน เป็น 'เฉพาะเงินโอน' จากข้อมูลเอกสารการเงิน สามารถระบุได้ 1 ประเภทการรับเงิน ดังรูป 6-26
- 6.3.2.5. กดช่อง 'รับผ่าน QR Code แบบไม่เชื่อมโยง' ดังรูป 6-26
- 6.3.2.6. กดปุ่ม บันทึกข้อมูล ระบบจะออกเลขที่เอกสาร ดังรูป 6-27 และพิมพ์ใบเสร็จให้อัตโนมัติ ดังรูป 6-28

รูป 6-26 หน้าจอเลือกข้อมูลรายการรับเงิน ช่อง 'เฉพาะเงินโอน' กรณี 'รับผ่าน QR Code แบบไม่เชื่อมโยง'

<!-- image: A screenshot of a Thai language software interface, detailing steps to process payments: including searching for payment details, selecting payment records, specifying payment types, enabling QR code payments, and saving the information. -->

รูป 6-27 หน้าจอข้อมูลรายการรับเงิน กรณี 'รับผ่าน QR Code แบบไม่เชื่อมโยง' เสร็จสิ้น

<!-- image: A screenshot of a software interface in Thai showing payment information, a data input form with fields like 'Type of Revenue', 'Barcode', and 'Invoice Number', and a table listing payment details. A 'Message' pop-up states "Successfully saved". -->

รูป 6-28 ใบเสร็จในระบบงานการเงินรับ

## รายงานที่เกี่ยวข้องกับเครื่องรูดบัตร EDC ระบบการเงินรับ

รายงานที่เกี่ยวข้องกับการใช้งานร่วมกับเครื่องรูดบัตร EDC ระบบการเงินรับ อยู่ในส่วนเมนูรายงานประจำวัน เลือกเมนูหัวข้อ ประกอบด้วย
- 1. รายงานการรับเงินด้วยบัตรเครดิต/เดบิต/ATM/QR
- 2. รายงานการรับเงินด้วยบัตรเครดิต/เดบิต/ATM/QR ตามประเภทรายได้

เมนูรายงาน เครื่องรูดบัตร EDC

## 1. รายงานการรับเงินด้วยบัตรเครดิต/เดบิต/ATM/QR

<!-- image: A screen capture of a form with fields for 'Date Received', 'Receiving Unit', and a drop-down box defaulted to 'Credit Card/Debit Card/ATM'. All labels are in Thai. -->

### รายละเอียดหน้าจอ
- **1. วันที่รับเงิน:** ระบุวันที่รับเงิน
- **2. หน่วยงานรับเงิน:** ระบบแสดงข้อมูลอัตโนมัติ
- **3. รับเงินโดย:** เลือกประเภทการรับเงิน

**วัตถุประสงค์:** เพื่อเรียกดูรายงานตามประเภทการรับเงิน บัตรเครดิต/เดบิต/ATM/QR

### ขั้นตอนการทำงาน
1. ระบุวันที่รับเงินที่ต้องการเรียกดูรายงานการรับเงินด้วยบัตรเครดิต/เดบิต/ATM/QR จากนั้นเลือกหน่วยงานรับเงิน ระบบจะแสดงข้อมูลอัตโนมัติในหน่วยงานที่ตรวจสอบ ผู้ใช้งานสามารถเรียกดูหน่วยงานรับเงินอื่นได้โดยให้คลิกปุ่ม

<!-- image: A screenshot of the software showing fields for entering the date range of receipts, the receiving unit, and the type of payment received. There is a red box indicating the date fields are the ones to be completed. -->

2. จากนั้นให้เลือกประเภทการรับเงินที่ต้องการ ดังรูป

<!-- image: A screenshot of the report display form with fields for date, unit, and payment method including options 'Credit Card/Debit Card/ATM', 'QR', 'QRM' and 'All'. The instruction '2.1 Choose payment type' is indicated with a red arrow. -->

<!-- image: A view of the report input form for the 'REP_FIN_073_2' report. Date input boxes are visible, as well as organization number and name input boxes. A button is highlighted with a text box saying '2.2 กดปุ่มแสดงรายงาน', which translates to '2.2 Press to show the report'. -->

### ตัวอย่าง รายงานการรับเงินด้วยบัตรเครดิต/เดบิต/ATM/QR

<!-- image: A report detailing financial transactions involving credit cards, debit cards, ATM, and QR code payments, spanning from 01/07/2566 to 18/07/2566. It includes transaction dates, invoice numbers, types of revenue, payment methods, card/reference numbers, and amounts. The report is generated by the Financial Division, Office of Finance, unit 14030000, with a total of 16 transactions and a grand total of 121,969.70. -->

3. เมื่อต้องการออกจากหน้าจอหรือจบการทำงานให้ทำการกดปุ่ม ระบบจะแสดงแจ้งเตือนการออกจากโปรแกรม ถ้าไม่ต้องการออกจากหน้าจอพิมพ์รายงานให้กดยกเลิก แต่ถ้าต้องการออกจากพิมพ์รายงาน ให้กดตกลง ดังรูป

<!-- image: A screenshot of a software interface, showing a data entry form with fields for date ranges and units of currency. A popup dialog is displayed, prompting the user to confirm exiting the program with a red circle emphasizing the exit confirmation button. The prompts are in Thai. -->

## 2. รายงานการรับเงินด้วยบัตรเครดิต/เดบิต/ATM/QR ตามประเภทรายได้

<!-- image: A screenshot of a Thai language form titled "BMRBRP59(REP_FIN_075) : รายงานการรับเงินด้วยบัตรเครดิต/เดบิต/ATM/QR ตามประเภทรายได้", containing fields for date range ("วันที่รับเงิน 01/07/2566 ถึง 01/07/2566"), "หน่วยงานรับเงิน" (receiving unit), "ประเภทรายได้" (type of income) and "รับเงินโดย" (payment by) with the selected value "บัตรเครดิต/บัตรเดบิต/บัตรATM" (credit card/debit card/ATM). -->

### รายละเอียดหน้าจอ
- **1. วันที่รับเงิน:** ระบุวันที่รับเงิน
- **2. หน่วยงานรับเงิน:** ระบบแสดงข้อมูลอัตโนมัติ
- **3. ประเภทรายได้:** เลือกประเภทรายได้ โดยคลิกปุ่ม
- **4. รับเงินโดย:** เลือกประเภทการรับเงิน

**วัตถุประสงค์:** เพื่อเรียกดูรายงานการรับเงินด้วยบัตรเครดิต/เดบิต/QR ตามประเภทรายได้

### ขั้นตอนการทำงาน
1. ระบุวันที่รับเงินที่ต้องการเรียกดูรายงานการรับเงินด้วยบัตรเครดิต/เดบิต/QR ตามประเภทรายได้ ดังรูป

<!-- image: A screenshot of a data entry form titled "BMRBRP59(REP_FIN_075)", featuring fields such as "วันที่รับเงิน" (date of receipt), "หน่วยงานรับเงิน" (receiving agency), "ประเภทรายได้" (type of income), and "รับเงินโดย" (received by), with date fields populated as "01/07/2566", and the text "บัตรเครดิต/บัตรเดบิต/บัตรATM" (credit card/debit card/ATM card) selected from a drop-down menu. A red box points to the date fields indicating “1.ระบุ ช่วงวันที่รับเงิน” (1. Specify the date range). -->

2. เลือกหน่วยงานรับเงิน โดยคลิกปุ่ม ระบบจะแสดงรายชื่อหน่วยงานให้เลือก ดังรูป

<!-- image: A screenshot of an application window in Thai, showing a data entry form and a selection list used to choose a unit of assignment; '14030000 กองการเงิน สำนักการคลัง' is highlighted in the list. The note '2.1 เลือกหน่วยงานนำส่ง' (2.1 Select assigning agency) points to the highlighted entry and the note '2.2 กดปุ่ม ตกลง' (2.2 Click OK) points to the 'ตกลง' ('OK') button below the selection list. -->

3. เลือกประเภทรายได้ โดยคลิกปุ่ม ระบบจะแสดงรายการประเภทรายได้ให้เลือก ดังรูป

<!-- image: A screenshot showing a form with fields for date, department, and tax type in Thai. A popup window titled "เลือกประเภทรายได้" (Select Tax Type) displays a list of tax types and codes. The '1018 ภาษีที่ดินและสิ่งปลูกสร้าง ทดสอบ' (Land and Building Tax Test) entry is highlighted in blue. The screenshot includes labels indicating to select a tax type and press the "ตกลง" (OK) button. -->

4. เลือกประเภทการรับเงิน จากนั้นกดปุ่มเรียกดูรายงาน ดังรูป

<!-- image: A screenshot of a software interface in Thai, showing input fields for "Date of receipt", "Receiving unit", "Income type", and a dropdown for "Received by" with options including Credit card/Debit card/ATM, QR, QRM, and All. A red box highlights the prompt "4.1 Select the type of payment received". -->

<!-- image: A window displaying a form for generating a financial report, with fields for date range ('01/07/2566' to '18/07/2566'), receiving organization ('14030000', 'กองการเงิน สำนักการคลัง'), income type ('1018', 'ภาษีที่ดินและสิ่งปลูกสร้าง ทดสอบ'), and payment method ('ทั้งหมด'). The window is titled 'BMRBRP59(REP_FIN_075) :รายงานการรับเงินด้วยบัตรเครดิต/เดบิต/ATM/QR ตามประเภทรายได้', and a red box highlights the instruction '4.2 กดปุ่มแสดงรายงาน', referring to the button for generating the report. -->

### ตัวอย่าง รายงานการรับเงินด้วยเครื่อง EDC ตามประเภทรายได้

5. เมื่อต้องการออกจากหน้าจอหรือจบการทำงานให้ทำการกดปุ่ม ระบบจะแสดงแจ้งเตือนการออกจากโปรแกรม ถ้าไม่ต้องการออกจากหน้าจอพิมพ์รายงานให้กดยกเลิก แต่ถ้าต้องการออกจากพิมพ์รายงาน ให้กดตกลง ตัวอย่างดังรูป

<!-- image: A screenshot showing a software interface in Thai. There is a red box around an icon at the top of the screen with the text "5.1 กดปุ่ม". A dialog box labeled "ข้อความแจ้งเตือน" (notification message) is open, containing the text "UDF-00002 : คุณต้องการที่จะออกจากโปรแกรมนี้หรือไม่" (UDF-00002: Do you want to exit this program?). Another red box highlights the "ตกลง" (OK) button, labeled "5.2 กดปุ่ม ตกลง" (5.2 Press OK button). -->