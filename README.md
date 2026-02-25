# 📊 Big Data Technology - Praktikum 1

**Setup Environment & Git Workflow (Spark + Cloud)**

## 🎯 Tujuan Praktikum

Praktikum ini bertujuan untuk membangun lingkungan kerja dasar sebagai seorang Data Engineer dengan menggunakan teknologi yang umum digunakan di industri, meliputi:

* Setup environment menggunakan VS Code dan PowerShell
* Instalasi dan penggunaan PySpark
* Koneksi ke MongoDB Atlas (Cloud Database)
* Pembuatan struktur project profesional
* Penggunaan Git dan GitHub untuk version control
* Menjalankan Spark job sederhana

---

## ⚙️ Teknologi yang Digunakan

* **Python 3.10**
* **PySpark**
* **MongoDB Atlas**
* **Git & GitHub**
* **VS Code**
* **PowerShell**

---

## 🧱 Struktur Project

```
bigdata-project/
│
├── data/
├── cloud_storage/
├── scripts/
│   ├── simple_job.py
│   └── test_mongo.py
├── notebooks/
├── reports/
├── README.md
```

---

## 🔄 Workflow Sistem

Alur kerja pada praktikum ini:

```
VS Code → PowerShell → PySpark → MongoDB Atlas → GitHub
```

---

## ☁️ Setup MongoDB Atlas

* Membuat cluster gratis (M0 Free Tier)
* Membuat database user
* Mengatur network access (0.0.0.0/0)
* Mengambil connection string
* Menguji koneksi menggunakan Python

---

## 🔥 Implementasi PySpark

Berikut kode Spark job sederhana yang digunakan:

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("SimpleJob") \
    .getOrCreate()

data = [("A", 10), ("B", 20), ("A", 30)]
columns = ["category", "value"]

df = spark.createDataFrame(data, columns)

df.groupBy("category").sum("value").show()

spark.stop()
```

---

## ▶️ Cara Menjalankan Program

```bash
py -3.10 scripts/simple_job.py
```

---

## 📊 Hasil Output

Output yang dihasilkan dari Spark job:

```
+--------+----------+
|category|sum(value)|
+--------+----------+
|       A|        40|
|       B|        20|
+--------+----------+
```

---

## 📸 Dokumentasi

Berikut dokumentasi yang dilampirkan:

1. Screenshot Spark berjalan
2. Screenshot MongoDB Atlas (Status ACTIVE)
3. Screenshot repository GitHub
4. Screenshot file simple_job.py
5. Screenshot hasil output Spark

---

## 🧠 Insight & Kesimpulan

Pada praktikum ini, mahasiswa tidak hanya belajar menjalankan kode, tetapi juga memahami bagaimana membangun lingkungan kerja Data Engineer yang meliputi:

* Integrasi local development dengan cloud
* Penggunaan distributed computing (Spark)
* Pengelolaan project secara profesional menggunakan Git
* Simulasi arsitektur Big Data sederhana

Praktikum ini menjadi dasar penting sebelum mempelajari topik lanjutan seperti ETL, data pipeline, dan machine learning.

---

## 🚀 Penutup

Dengan selesainya praktikum ini, mahasiswa telah memiliki fondasi awal dalam pengembangan sistem Big Data yang siap digunakan dalam skala industri.

---
