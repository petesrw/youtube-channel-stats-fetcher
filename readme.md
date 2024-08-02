# ตัวดึงข้อมูลสถิติของช่อง YouTube

โปรเจกต์นี้เป็นสคริปต์ Python ที่ใช้ YouTube Data API เพื่อดึงข้อมูลและแสดงจำนวนผู้เข้าชมและผู้ติดตามของช่อง YouTube ที่ระบุ สคริปต์นี้จะดึงข้อมูลอย่างต่อเนื่องทุก 9 วินาที เพื่อให้แน่ใจว่าจะไม่เกินโควตาการใช้งาน API รายวัน

## คุณสมบัติ

- **อัปเดตแบบเรียลไทม์**: ดึงข้อมูลจำนวนผู้เข้าชมและผู้ติดตามล่าสุดจากช่อง YouTube
- **จัดการโควตาอย่างมีประสิทธิภาพ**: สคริปต์ถูกออกแบบมาเพื่อให้อยู่ในขอบเขตโควตารายวันของ YouTube Data API โดยทำการร้องขอข้อมูลทุก 9 วินาที
- **ตั้งค่าง่าย**: สามารถตั้งค่าและใช้งานได้ง่ายด้วยการตั้งค่าเพียงเล็กน้อย

## ข้อกำหนดเบื้องต้น

ก่อนที่จะรันสคริปต์ ตรวจสอบให้แน่ใจว่าคุณมีสิ่งต่อไปนี้:

1. **Python 3.6+**: สคริปต์นี้ต้องการ Python เวอร์ชัน 3.6 ขึ้นไป
2. **บัญชี Google Cloud Platform**: คุณจะต้องตั้งค่าโปรเจกต์ใน Google Cloud Console เพื่อเปิดใช้งาน YouTube Data API
3. **เปิดใช้งาน YouTube Data API v3**: เปิดใช้งาน YouTube Data API v3 ในโปรเจกต์ Google Cloud ของคุณ
4. **OAuth 2.0 Credentials**: ดาวน์โหลดไฟล์ JSON ที่เป็น OAuth 2.0 client credentials

## การติดตั้ง

1. **โคลน Repository**

   โคลน repository นี้ไปยังเครื่องของคุณ:

   ```bash
   git clone https://github.com/your-username/youtube-channel-stats-fetcher.git
   cd youtube-channel-stats-fetcher

2.	**ตั้งค่า Virtual Environment**
แนะนำให้ใช้ virtual environment เพื่อจัดการ dependencies:

```python3 -m venv myenv
    source myenv/bin/activate  # บน Windows ใช้ `myenv\Scripts\activate`

3.  **ติดตั้งแพ็กเกจที่จำเป็น**
ติดตั้งแพ็กเกจ Python ที่จำเป็นโดยใช้ pip:
```pip install google-auth google-auth-oauthlib google-api-python-client


4.	วางไฟล์ client_secret.json
ดาวน์โหลดไฟล์ client_secret.json จาก Google Cloud Console และวางไว้ในไดเรกทอรีของโปรเจกต์

การตั้งค่า

	1.	ตั้งค่า Google Cloud Console
	•	ไปที่ Google Cloud Console
	•	สร้างโปรเจกต์ใหม่
	•	ไปที่ APIs & Services > Credentials
	•	คลิกที่ Create credentials แล้วเลือก OAuth client ID
	•	ตั้งค่าหน้าจอการยินยอม (Consent Screen) หากถูกขอให้ทำ
	•	เลือก Desktop app หรือ Web application เป็นประเภทของแอปพลิเคชัน
	•	ดาวน์โหลดไฟล์ JSON credentials แล้วเปลี่ยนชื่อเป็น client_secret.json
	2.	อนุญาต Redirect URI
	•	ตรวจสอบให้แน่ใจว่าคุณได้เพิ่ม redirect URI: http://localhost:8000/ ใน Google Cloud Console ภายใต้ Authorized redirect URIs

วิธีการใช้งาน

1.	แก้ไขสคริปต์
เปิดไฟล์ main.py และแทนที่ channel_id ด้วย YouTube channel ID ที่คุณต้องการตรวจสอบ:

channel_id = 'UC_x5XG1OV2P6uZZ5FSM9Ttw'  # แทนที่ด้วย Channel ID ของคุณ
2.	รันสคริปต์
ใช้ Python ในการรันสคริปต์:
```python main.py
	•	สคริปต์จะเปิดหน้าต่างเบราว์เซอร์เพื่อให้คุณยืนยันการเข้าถึง YouTube Data API
	•	เมื่อได้รับการยืนยันแล้ว สคริปต์จะเริ่มดึงข้อมูลและแสดงจำนวนวิวและจำนวนผู้ติดตามของช่องทุกๆ 10 วินาที

ใบอนุญาต

โปรเจกต์นี้ได้รับอนุญาตภายใต้ MIT License - ดูไฟล์ LICENSE สำหรับรายละเอียด

การร่วมมือ

ยินดีต้อนรับการร่วมมือ! กรุณา fork repository และส่ง pull request พร้อมการปรับปรุงของคุณ