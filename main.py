import os
import difflib
from fpdf import FPDF
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load text files from 'documents' folder
def load_documents(folder_path):
    files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    documents = [open(os.path.join(folder_path, f), encoding='utf-8').read() for f in files]
    return files, documents

# Convert text to TF-IDF vectors
def vectorize_text(documents):
    vectorizer = TfidfVectorizer()
    return vectorizer.fit_transform(documents).toarray()

# Compute similarity scores
def check_plagiarism(files, vectors, documents):
    results = []
    highlighted_texts = []
    
    for i in range(len(files)):
        for j in range(i + 1, len(files)):
            similarity_score = cosine_similarity([vectors[i]], [vectors[j]])[0][0]
            results.append((files[i], files[j], similarity_score))
            
            # Highlight matching text
            highlighted = highlight_matches(documents[i], documents[j])
            highlighted_texts.append((files[i], files[j], highlighted))
    
    return results, highlighted_texts

# Enclose plagiarized text in <<>> markers
def highlight_matches(text1, text2):
    matcher = difflib.SequenceMatcher(None, text1, text2)
    highlighted_text = []
    
    for opcode, a1, a2, b1, b2 in matcher.get_opcodes():
        segment = text1[a1:a2].strip()
        if opcode == 'equal':  # Matching text
            highlighted_text.append(("M", f"<<{segment}>>"))  # Enclose in <<>>
        else:
            highlighted_text.append(("N", segment))  # Normal text
    
    return highlighted_text

# Save results as PDF with proper formatting
def save_results_to_pdf(results, highlighted_texts, filename="plagiarism_report.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Title
    pdf.cell(200, 10, "Plagiarism Report", ln=True, align="C")
    pdf.ln(10)

    # Add similarity scores
    pdf.set_font("Arial", size=10)
    pdf.cell(0, 10, "Document Similarity Scores:", ln=True)
    pdf.ln(5)

    for file1, file2, score in results:
        pdf.cell(0, 10, f"{file1} <-> {file2}: {score:.2f}", ln=True)
    pdf.ln(10)

    # Add highlighted text matches
    pdf.set_font("Arial", "B", size=12)
    pdf.cell(0, 10, "Highlighted Matching Text:", ln=True)
    pdf.ln(5)

    for file1, file2, highlighted in highlighted_texts:
        pdf.set_font("Arial", "B", size=10)
        pdf.cell(0, 10, f"{file1} <-> {file2}:", ln=True)
        pdf.ln(3)

        # Format plagiarism text with <<>> markers
        pdf.set_font("Arial", size=10)
        paragraph = ""

        for style, text in highlighted:
            paragraph += text + " "  # Ensure full words are enclosed properly

        pdf.multi_cell(0, 6, paragraph.strip(), align="J")  # Justified text
        pdf.ln(5)

    pdf.output(filename)
    print(f"✅ Plagiarism report saved as '{filename}'")

# Main function
def main():
    folder_path = "documents"  # Path where text files are stored
    if not os.path.exists(folder_path):
        print(f"❌ Error: Folder '{folder_path}' not found.")
        return
    
    files, documents = load_documents(folder_path)
    if len(files) < 2:
        print("❌ Not enough documents for plagiarism check.")
        return
    
    vectors = vectorize_text(documents)
    results, highlighted_texts = check_plagiarism(files, vectors, documents)

    print("\n🔍 Plagiarism Results:")
    for file1, file2, score in results:
        print(f"{file1} <-> {file2}: {score:.2f}")

    # Save report as PDF only
    save_results_to_pdf(results, highlighted_texts)

if __name__ == "__main__":
    main()
