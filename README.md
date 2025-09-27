# AWS Cloud-Based Attendance Tracking System

## 📌 Project Overview
This project demonstrates how to build and deploy a **cloud-based attendance tracking system** using **AWS EC2 and AWS RDS (MySQL)**.  
The system allows users to mark attendance through a web form, securely stores data in the cloud, and ensures **scalability, reliability, and cost control**.  

---

## 🔧 Tools & Services
- **AWS EC2** – to run the backend Flask API  
- **AWS RDS (MySQL)** – to store attendance records  
- **Security Groups** – to allow specific traffic (SSH, HTTP, MySQL)  
- **Key Pair (.pem file)** – for secure SSH access to EC2  
- **AWS Console** – to manage cloud resources  
- **Browser** – to test the application  

---

## 🚀 Implementation Steps
1. Created an **EC2 Key Pair** for secure SSH access  
2. Configured **EC2 Security Group** (SSH on port 22, HTTP on port 80)  
3. Configured **RDS Security Group** (MySQL on port 3306)  
4. Launched **RDS MySQL database** and created `attendance_db` with `attendance` table  
5. Launched **Ubuntu EC2 instance** and installed Python & Flask  
6. Developed **Flask backend (app.py)** for attendance marking  
7. Created a **frontend (index.html)** form for users to submit attendance  
8. Deployed frontend with **Apache** and backend with **Flask**  
9. Connected the application to **RDS MySQL**  
10. Tested marking attendance and verified entries in the database  

---

## 📸 Project Output

### 1. Attendance Form  
![Attendance Form](Assets-/Attendance%20Form.png)  

### 2. Flask Backend  
![Flask Backend](Assets-/Flask%20Backend.png)  

### 3. Database Records  
![Database Records](Assets-/Database%20Records.png)  

---

## 🌟 Outcome
✅ A fully functional **cloud-based attendance tracking system** hosted on AWS.  
✅ Users can **submit attendance online**, and data is securely stored in **RDS MySQL**.  
✅ The solution is **scalable, reliable, and cost-effective**.  

---

## 🙌 Acknowledgement
This project was completed as part of my **internship with Pinnacle Labs**.
