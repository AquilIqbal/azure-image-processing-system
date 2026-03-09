## 1st Functionality Work Flow : 

### User
### ↓
### Upload File (UI)
### ↓
### Flask Backend (Python)
### ↓
### Image Processing (Pillow)
### ↓
### Azure SDK
### ↓
### Azure Blob Storage (Cloud)
###  ↓
### Blob URL returned
###  ↓
### Gallery Page shows image


<!-- | Azure Service      | Role              |
     | ------------------ | ----------------- |
     | Azure Blob Storage | Store files       |
     | Azure App Service  | Deploy web app    |
     | Azure SQL Database | Store metadata    |
     | Azure Key Vault    | Secure secrets    |
     | Azure Monitor      | Track performance | -->



# Cloud Azure Image Processing System

## 1st Functionality Work Flow

```
User
↓
Upload File (UI)
↓
Flask Backend (Python)
↓
Image Processing (Pillow)
↓
Azure SDK
↓
Azure Blob Storage (Cloud)
↓
Blob URL returned
↓
Metadata stored in Azure SQL Database
↓
Gallery Page displays processed files
```

---

# Overview

This project is a cloud-based image processing system where users can upload images or documents, process them, and store them in the cloud.

The application uses Flask for backend processing, Azure Blob Storage for file storage, and Azure SQL Database for storing metadata.

Users can view uploaded files through a gallery page, download them, or delete them from the system.

---

# Features Implemented

## File Upload

Users can upload images or documents through the web interface.

### Supported Image Types

```
jpg
jpeg
png
gif
bmp
tiff
webp
```

### Supported Document Types

```
pdf
docx
txt
```

---

## Image Processing

Images can be processed before being stored in the cloud.

Supported operations include:

* Resize image (512×512, 1024×1024, 2048×2048, or custom size)
* Apply compression
* Convert image format (JPG, PNG, WEBP, etc.)

Image processing is handled using the Python Pillow library.

---

## Azure Blob Storage

Processed files are stored in Azure Blob Storage.

When a file is uploaded:

1. The backend processes the image.
2. The processed file is uploaded to Azure Blob Storage.
3. Azure returns a Blob URL for the stored file.

Example storage structure:

```
images/
   processed/
   documents/
```

---

## Azure SQL Database

Azure SQL Database stores metadata about uploaded files.

Instead of storing the file itself, the database stores information such as:

* Original filename
* Blob URL
* File format
* File size
* Image processing operations
* Upload timestamp

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

## Gallery System

The gallery page retrieves metadata from Azure SQL Database and displays uploaded files.

Users can:

* View uploaded images
* Download files
* Delete files

The gallery also displays information about the processing applied to each file.

---

# Azure Services Used

| Azure Service      | Purpose                            |
| ------------------ | ---------------------------------- |
| Azure Blob Storage | Store uploaded and processed files |
| Azure SQL Database | Store metadata of uploaded files   |

---

# Technologies Used

| Technology             | Role                |
| ---------------------- | ------------------- |
| Python                 | Backend programming |
| Flask                  | Web framework       |
| Pillow                 | Image processing    |
| Azure Blob Storage     | Cloud file storage  |
| Azure SQL Database     | Metadata storage    |
| SQLAlchemy             | Database ORM        |
| HTML / CSS / Bootstrap | Frontend interface  |

