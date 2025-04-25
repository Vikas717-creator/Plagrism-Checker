# 🕵️‍♂️ Plagiarism Checker CLI

A simple yet powerful **Command Line Interface (CLI)** tool to detect textual plagiarism using **TF-IDF (Term Frequency-Inverse Document Frequency)** and **Cosine Similarity**. This tool is perfect for quickly comparing two documents and generating a detailed plagiarism report with highlighted plagiarized content.

---

## 🚀 Features

- 🔍 Detects plagiarism based on semantic similarity
- 📄 Accepts `.txt` files for comparison
- 📊 Shows similarity score between documents
- 📝 Highlights plagiarized phrases using `<<>>` markers
- 📤 Automatically generates a clean and clear **PDF report**
- ⚡ Fast and efficient — ideal for small to medium text files
- 🛠️ Fully command-line driven — no GUI or web server needed

## ⚙️ Installation

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/plagiarism-checker-cli.git
cd plagiarism-checker-cli

## 📥How to Use
**🔧 Command Format**

python main.py documents/original.txt documents/suspect.txt
## 📄 Output Report

The output **PDF file** contains the original and suspect text side by side.  
Text segments with high similarity are highlighted with `<<` and `>>` markers.  
The report helps users quickly locate copied content and assess the severity of plagiarism.

---

## 🧠 How It Works

- **TF-IDF Vectorization**: Converts text into numerical vectors based on term importance.
- **Cosine Similarity**: Compares document vectors to calculate similarity percentage.
- **Text Matching**: Finds overlapping n-grams or phrases and wraps them with `<< >>`.
- **PDF Report Generation**: Uses `fpdf` (or `reportlab`) to generate a clean, professional report.

---

## 📦 Dependencies

The tool uses the following Python packages:

- `scikit-learn`
- `numpy`
- `fpdf` *(or optionally `reportlab`)*

Install them with:

```bash
pip install scikit-learn numpy fpdf


# 🔮 Future Enhancements

- 📁 Support comparison of multiple documents in a batch
- 🎚️ Add configurable similarity threshold (e.g., 70% cutoff)
- 🖼️ Display side-by-side colored comparisons in PDF
- 🖥️ Develop a simple GUI using Tkinter or PyQt
- 🌐 Integrate with web scraping or plagiarism detection APIs
- 🧠 Use advanced NLP models like BERT for semantic similarity
- 📊 Include detailed plagiarism statistics in the report

---

## 👨‍💻 Author

Developed by **Vikas Thakur**

- 📧 Email: vikasthakur5900@gmail.com 
