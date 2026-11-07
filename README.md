NOVA AI – Chatbot Accuracy Testing System

🚀 Project Overview

NOVA AI Chatbot Accuracy Testing System is a Python-based application designed to evaluate and analyze the similarity between an expected answer and an AI-generated answer.

The system helps users understand how closely an AI-generated response matches the expected response by calculating different text evaluation metrics such as Precision, Recall, and F1 Score.

It also generates a detailed testing report containing matched words, missing words, extra words, similarity percentage, and the final evaluation verdict.

🎯 Project Objectives

- Evaluate AI-generated chatbot responses.
- Compare expected answers with AI-generated answers.
- Measure text similarity using evaluation metrics.
- Identify matched, missing, and extra words.
- Generate detailed accuracy analysis reports.
- Provide an easy-to-use interface for testing.

✨ Key Features

1. Chatbot Response Testing

- Test AI-generated answers against expected answers.
- Enter expected and generated responses for comparison.
- Analyze response matching.

2. Text Similarity Analysis

- Calculate text similarity using F1 Score.
- Evaluate how closely two responses match.
- Display similarity percentage.

3. Performance Evaluation Metrics

The system calculates:

- Precision: Measures how many matched words are relevant to the generated answer.
- Recall: Measures how many expected words were successfully matched.
- F1 Score: Calculates the balance between Precision and Recall.

4. Word-Level Analysis

- Identify matched words.
- Detect missing words.
- Identify extra words in AI-generated responses.
- Display matched word count.

5. Automatic Testing Verdict

The system provides an evaluation verdict based on text similarity, such as:

- High Text Similarity
- Moderate Text Similarity
- Low Text Similarity

6. Testing Report Generation

- Generate detailed accuracy analysis reports.
- Save testing results in a text file.
- Store evaluation metrics.
- Review previous testing reports.

7. User-Friendly Interface

- Simple and easy-to-use interface.
- Input fields for expected and generated answers.
- Display testing results clearly.
- Easy testing workflow.

🛠️ Technologies Used

- Python
- Python Libraries (as listed in requirements.txt)
- Text Processing
- Precision and Recall
- F1 Score
- Git and GitHub
- Visual Studio Code

⚙️ How the Project Works

The system follows these steps:

1. User enters the expected answer.
2. User enters the AI-generated answer.
3. The system processes both text responses.
4. It compares the words in both responses.
5. Precision, Recall, and F1 Score are calculated.
6. Matched, missing, and extra words are identified.
7. A final text similarity verdict is displayed.
8. A detailed testing report can be generated and saved.

📊 Evaluation Metrics

Metric| Description
Precision| Measures matched words against generated answer words
Recall| Measures matched words against expected answer words
F1 Score| Harmonic mean of Precision and Recall
Text Similarity| Displays the F1-based similarity percentage
Matched Words| Words found in both responses
Missing Words| Expected words not found in generated response
Extra Words| Generated words not found in expected response

🧪 Testing and Results

The project has been tested using multiple input examples.

Testing includes:

- Comparing correct and incorrect responses.
- Checking text similarity.
- Verifying Precision and Recall calculations.
- Checking F1 Score.
- Identifying matched and missing words.
- Generating and saving testing reports.

Sample Testing Result

Expected Answer:
The Earth revolves around the Sun.

AI Generated Answer:
The Earth is flat.

Analysis Results:

- Text Similarity (F1): 40.00%
- Precision: 50.00%
- Recall: 33.33%
- F1 Score: 40.00%
- Matched Word Count: 2
- Verdict: LOW TEXT SIMILARITY

This example demonstrates how the system identifies differences between expected and generated responses.

💻 Installation and Setup

Step 1: Clone the Repository

git clone https://github.com/pavanpatel5612-cpu/NOVA-AI-Chatbot-Accuracy-Testing-System.git

Step 2: Open the Project Folder

cd NOVA-AI-Chatbot-Accuracy-Testing-System

Step 3: Install Required Libraries

pip install -r requirements.txt

Step 4: Run the Application

python main.py

📁 Project Structure

NOVA-AI-Chatbot-Accuracy-Testing-System/
│
├── main.py
│
├── requirements.txt
│
├── README.md
│
├── NOVA_AI_Report.txt
│
└── Testing Reports

⚠️ Limitations

- The current evaluation is based on token-level text similarity.
- Similarity scores do not guarantee factual correctness.
- Semantically equivalent sentences may receive different similarity scores.
- The system does not independently verify the factual accuracy of AI-generated answers.

Important: A high text similarity score does not necessarily mean that an answer is factually correct.

🔮 Future Improvements

- Semantic similarity analysis.
- Advanced NLP-based evaluation.
- Automated chatbot testing.
- Support for multiple test cases.
- Graphical testing analytics.
- Export reports in PDF and Excel formats.

👨‍💻 Developer

Project Name: NOVA AI – Chatbot Accuracy Testing System

Developer: Pavan Patel

Programming Language: Python

Project Type: AI Chatbot Testing and Accuracy Evaluation

📌 Conclusion

NOVA AI Chatbot Accuracy Testing System provides a simple way to compare expected answers with AI-generated responses.

It helps analyze response similarity through Precision, Recall, F1 Score, and word-level comparison.

This project demonstrates practical implementation of Python programming, text processing, performance evaluation metrics, and testing report generation.

---

⭐ If you find this project useful, consider giving it a star on GitHub!


