# 🏢 Human Resource Management System (HRMS)

<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=28&duration=4000&pause=1000&color=2E8B57&center=true&vCenter=true&width=600&lines=Human+Resource+Management+%F0%9F%92%BC;Django+Powered+Solution+%F0%9F%9A%80;Employee+Management+Made+Easy+%E2%9C%A8" alt="Typing SVG" />
</div>

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"/>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"/>
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white"/>
</div>

<div align="center">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Version-1.0.0-orange?style=for-the-badge"/>
</div>

---

## 📋 Table of Contents

- [📖 Overview](#-overview)
- [✨ Features](#-features)
- [🚀 Tech Stack](#-tech-stack)
- [📁 Project Structure](#-project-structure)
- [⚙️ Installation](#️-installation)
- [🎯 Usage](#-usage)
- [📱 Screenshots](#-screenshots)
- [🔐 User Roles](#-user-roles)
- [🛠️ API Endpoints](#️-api-endpoints)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👩‍💻 Author](#-author)

---

## 📖 Overview

The **Human Resource Management System (HRMS)** is a comprehensive web application built with Django that streamlines HR operations and employee management. This system provides a centralized platform for managing employee data, attendance, payroll, leave management, and performance tracking.

### 🎯 Purpose
- Automate HR processes and reduce manual workload
- Centralize employee information and company data
- Improve efficiency in attendance and leave management
- Provide insights through reporting and analytics

---

## ✨ Features

### 👥 **Employee Management**
- ➕ Add, update, and delete employee records
- 📊 Comprehensive employee profiles with personal and professional details
- 🔍 Advanced search and filtering capabilities
- 📁 Document management and file uploads

### 🕒 **Attendance System**
- ⏰ Real-time clock in/out functionality
- 📅 Monthly attendance reports
- 📊 Attendance analytics and statistics
- 🚫 Late arrival and early departure tracking

### 🏖️ **Leave Management**
- 📝 Leave application submission
- ✅ Multi-level approval workflow
- 📊 Leave balance tracking
- 📈 Leave history and reports

### 💰 **Payroll Management**
- 💵 Salary calculation and processing
- 🧾 Payslip generation
- 📊 Salary reports and analytics
- 💳 Tax and deduction management

### 🎯 **Performance Tracking**
- ⭐ Employee performance evaluations
- 🎖️ Goal setting and tracking
- 📈 Performance analytics
- 🏆 Recognition and rewards system

### 📊 **Reporting & Analytics**
- 📈 Comprehensive HR dashboards
- 📋 Customizable reports
- 📊 Data visualization with charts and graphs
- 📤 Export functionality (PDF, Excel)

### 🔐 **Security Features**
- 👤 Role-based access control
- 🔒 Secure authentication system
- 📝 Activity logging and audit trails
- 🛡️ Data encryption and protection

---

## 🚀 Tech Stack

<div align="center">

### **Backend**
<img src="https://img.shields.io/badge/Python_3.9+-3776AB?style=flat-square&logo=python&logoColor=white" height="30"/>
<img src="https://img.shields.io/badge/Django_4.2+-092E20?style=flat-square&logo=django&logoColor=white" height="30"/>
<img src="https://img.shields.io/badge/Django_REST-ff1709?style=flat-square&logo=django&logoColor=white" height="30"/>

### **Frontend**
<img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white" height="30"/>
<img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white" height="30"/>
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black" height="30"/>
<img src="https://img.shields.io/badge/Bootstrap_5-7952B3?style=flat-square&logo=bootstrap&logoColor=white" height="30"/>

### **Database**
<img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white" height="30"/>
<img src="https://img.shields.io/badge/PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white" height="30"/>

### **Tools & Libraries**
<img src="https://img.shields.io/badge/Chart.js-FF6384?style=flat-square&logo=chartdotjs&logoColor=white" height="30"/>
<img src="https://img.shields.io/badge/jQuery-0769AD?style=flat-square&logo=jquery&logoColor=white" height="30"/>
<img src="https://img.shields.io/badge/Font_Awesome-339AF0?style=flat-square&logo=fontawesome&logoColor=white" height="30"/>

</div>

---

## 📁 Project Structure

```
hrms/
├── 📂 hrms_project/
│   ├── 📂 hrms_project/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── 📂 employees/
│   │   ├── 📂 migrations/
│   │   ├── 📂 templates/
│   │   ├── 📂 static/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── forms.py
│   │   └── urls.py
│   ├── 📂 attendance/
│   │   ├── 📂 migrations/
│   │   ├── 📂 templates/
│   │   ├── models.py
│   │   ├── views.py
│   │   └── urls.py
│   ├── 📂 leave_management/
│   │   ├── 📂 migrations/
│   │   ├── 📂 templates/
│   │   ├── models.py
│   │   └── views.py
│   ├── 📂 payroll/
│   │   ├── 📂 migrations/
│   │   ├── 📂 templates/
│   │   ├── models.py
│   │   └── views.py
│   ├── 📂 static/
│   │   ├── 📂 css/
│   │   ├── 📂 js/
│   │   └── 📂 images/
│   ├── 📂 templates/
│   │   ├── 📂 base/
│   │   └── 📂 registration/
│   ├── manage.py
│   └── requirements.txt
├── 📄 README.md
└── 📄 LICENSE
```

---

## ⚙️ Installation

### 🔧 Prerequisites
- Python 3.9 or higher
- pip (Python package installer)
- Git

### 📥 Step-by-step Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Poorni-2002/hrms.git
   cd hrms
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Open your browser and navigate to `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

---

## 🎯 Usage

### 🔑 **Default Login Credentials**
```
Admin User:
Username: admin
Password: admin123

HR Manager:
Username: hr_manager
Password: hr123

Employee:
Username: employee
Password: emp123
```

### 🚀 **Getting Started**
1. Log in with admin credentials
2. Set up company information
3. Add departments and positions
4. Create employee accounts
5. Configure leave policies
6. Start using the system!

---

## 📱 Screenshots

<div align="center">

### 🏠 Dashboard
![Dashboard](https://via.placeholder.com/800x400/2E8B57/FFFFFF?text=Dashboard+Screenshot)

### 👥 Employee Management
![Employee Management](https://via.placeholder.com/800x400/4682B4/FFFFFF?text=Employee+Management)

### 🕒 Attendance System
![Attendance](https://via.placeholder.com/800x400/DC143C/FFFFFF?text=Attendance+System)

### 📊 Reports & Analytics
![Reports](https://via.placeholder.com/800x400/FF8C00/FFFFFF?text=Reports+%26+Analytics)

</div>

---

## 🔐 User Roles

| Role | Permissions | Access Level |
|------|-------------|--------------|
| **Super Admin** | Full system access | 🔴 Complete Control |
| **HR Manager** | Employee management, reports | 🟡 High Access |
| **Department Manager** | Team management | 🟠 Medium Access |
| **Employee** | Personal data, leave requests | 🟢 Basic Access |

---

## 🛠️ API Endpoints

### 👥 **Employee Management**
```
GET    /api/employees/          # List all employees
POST   /api/employees/          # Create new employee
GET    /api/employees/{id}/     # Get employee details
PUT    /api/employees/{id}/     # Update employee
DELETE /api/employees/{id}/     # Delete employee
```

### 🕒 **Attendance**
```
POST   /api/attendance/checkin/   # Clock in
POST   /api/attendance/checkout/  # Clock out
GET    /api/attendance/report/    # Attendance reports
```

### 🏖️ **Leave Management**
```
GET    /api/leaves/              # List leave requests
POST   /api/leaves/              # Apply for leave
PUT    /api/leaves/{id}/approve/ # Approve leave
PUT    /api/leaves/{id}/reject/  # Reject leave
```

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some amazing feature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

### 📝 **Contribution Guidelines**
- Follow PEP 8 style guidelines
- Write meaningful commit messages
- Add tests for new features
- Update documentation as needed

---

## 🐛 Issues & Support

Found a bug or need help? 

- 🐞 [Report Issues](https://github.com/Poorni-2002/hrms/issues)
- 💬 [Discussions](https://github.com/Poorni-2002/hrms/discussions)
- 📧 Email: poorni.dev@gmail.com

---

## 📈 Future Enhancements

- [ ] 📱 Mobile application
- [ ] 🔔 Real-time notifications
- [ ] 📊 Advanced analytics dashboard
- [ ] 🤖 AI-powered insights
- [ ] 📧 Email integration
- [ ] 🔗 Third-party API integrations

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Poorni

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software...
```

---

## 👩‍💻 Author

<div align="center">
  <img src="https://github.com/Poorni-2002.png" width="100" style="border-radius: 50%;"/>
  
  **Poorni**
  
  [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Poorni-2002)
  [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/yourprofile)
  [![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:poorni.dev@gmail.com)
  
  *"Building solutions that make HR management effortless and efficient"*
  
</div>

---

## 🙏 Acknowledgments

- Django community for the amazing framework
- Bootstrap team for the UI components
- Chart.js for beautiful data visualization
- All contributors and supporters

---

<div align="center">
  <img src="https://komarev.com/ghpvc/?username=Poorni-2002&label=Project%20Views&color=2E8B57&style=for-the-badge" alt="Project Views" />
  
  ⭐ **If this project helped you, please give it a star!** ⭐
  
  <img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="1000">
</div>
