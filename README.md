# Cloud Azure Image Processing System

## Overview

Cloud Azure Image Processing System is a cloud-based web application that allows users to upload, process, and manage images or documents.

The system performs image processing operations such as resizing, compression, and format conversion before storing files in cloud storage.

The application uses a Flask backend, Azure Blob Storage for file storage, and Azure SQL Database for metadata storage.

Users can view their uploaded files through a gallery interface, download them, or delete them from the system.

---

# System Workflow

```
User
↓
Upload File (Web UI)
↓
Flask Backend (Python)
↓
Image Processing (Pillow)
↓
Azure SDK
↓
Azure Blob Storage
↓
Blob URL returned
↓
Metadata stored in Azure SQL Database
↓
Gallery Page displays files
```

---

# Features

## File Upload

Users can upload images or documents through the web interface.

### Supported Image Formats

```
jpg
jpeg
png
gif
bmp
tiff
webp
```

### Supported Document Formats

```
pdf
docx
txt
```

---

# Image Processing

Images can be processed before being stored in the cloud.

Supported operations include:

• Resize image
• Apply compression
• Convert image format

### Resize Options

```
512 x 512
1024 x 1024
2048 x 2048
Custom size
```

Image processing is performed using the Pillow Python library.

---

# Cloud Storage (Azure Blob Storage)

Processed files are stored in Azure Blob Storage.

When a file is uploaded:

1. The backend processes the image
2. The processed file is uploaded to Azure Blob Storage
3. Azure returns a Blob URL
4. The URL is stored in the database

Example storage structure:

```
images/
   processed/

documents/
```

---

# Metadata Storage (Azure SQL Database)

Azure SQL Database stores metadata related to uploaded files.

The system stores information such as:

• Original filename
• Blob URL
• File format
• File size
• Processing operations applied
• Upload timestamp

Example database fields:

```
id
original_filename
blob_name
blob_url
container_name
file_format
file_size_bytes
original_size_kb
processed_size_kb
resize_applied
compress_applied
width
height
uploaded_at
```

---

# Gallery System

The gallery page retrieves metadata from Azure SQL Database and displays uploaded files.

Users can:

• View uploaded images
• Download files
• Delete files

Processing information is also displayed for each file.

---

# Azure Services Used

| Azure Service      | Purpose                             |
| ------------------ | ----------------------------------- |
| Azure Blob Storage | Store uploaded and processed files  |
| Azure SQL Database | Store metadata of uploaded files    |
| Azure App Service  | Deploy and host the web application |

---

# Technologies Used

| Technology         | Role                |
| ------------------ | ------------------- |
| Python             | Backend programming |
| Flask              | Web framework       |
| Pillow             | Image processing    |
| Azure Blob Storage | Cloud file storage  |
| Azure SQL Database | Metadata storage    |
| SQLAlchemy         | Database ORM        |
| HTML / CSS         | Frontend interface  |
| Bootstrap          | UI styling          |

---

# Project Structure

```
cloud_Azure
│
├── static
│   └── style.css
│
├── templates
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── images.html
│   ├── documents.html
│   ├── gallery.html
│   ├── history.html
│   └── analytics.html
│
├── app.py
├── database.py
├── azure_blob_helper.py
├── requirements.txt
├── startup.txt
└── README.md
```

---

# Deployment

The application can be deployed using Azure App Service with GitHub integration.

Deployment steps:

1. Push code to GitHub repository
2. Create Azure Web App
3. Connect GitHub repository to Azure
4. Configure environment variables
5. Azure automatically builds and deploys the application


---

# Future Improvements

Possible enhancements include:

• User file sharing
• Image watermarking
• AI-based image classification
• Storage usage analytics
• File version history
