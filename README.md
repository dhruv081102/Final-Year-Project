# Final-Year-Project

### Summary of the Report: Machine Translation from English to Regional Languages using Transformer Model

#### Authors and Affiliations:
- Vijay Sandha, Esha Telkar, Dhruv Mehta, Deepmala Singh
- Mentor:- Monika Ingale, Vinutha T. P.
- Department of Electronics and Telecommunication Engineering, Shah and Anchor Kutchhi Engineering College, Mumbai.


### Abstract:
The paper explores Machine Translation (MT) from English to regional languages, highlighting the role of Transformer models. It evaluates the efficiency of these models for translating English to Hindi and Marathi, comparing them with established platforms like Google Translator and Bing Translator. The paper underscores the future potential of MT in promoting cross-cultural communication and highlights the importance of transfer learning in enhancing Neural Machine Translation (NMT) systems.

### Keywords:
- Machine Translation (MT)
- Natural Language Processing (NLP)
- Machine Learning
- English to Hindi translation
- English to Marathi translation

### Introduction:
MT for English to regional languages is crucial for global communication and cultural exchange. It aims to break language barriers and promote inclusivity. MT facilitates access to English-dominated digital content, supporting linguistic inclusivity and aiding businesses in global markets through effective localization.

### Related Work:
MT has evolved from rule-based and statistical methods to neural and hybrid techniques.

1. *Statistical Machine Translation (SMT):* Uses statistical models to learn correlations between languages but struggles with linguistic nuances.
2. *Rules-Based Machine Translation (RBMT):* Relies on language rules and dictionaries but is labor-intensive and hard to scale.
3. *Neural Machine Translation (NMT):* Uses deep learning techniques and transformer models for better context understanding, outperforming SMT and RBMT.
4. *Hybrid Machine Translation:* Combines different methods to leverage their strengths and mitigate weaknesses.

### Methodology:
MT involves several key stages:

1. *Pre-processing:* Cleaning and transforming the input data (e.g., tokenization, padding, lowercasing, punctuation removal, stop word removal, stemming, lemmatization, contraction removal).
2. *Feature Extraction:* Techniques like Word2Vec create dense vector representations of words.
3. *Model Selection:* Transformer models are preferred for their ability to handle long-range dependencies and parallel processing.
4. *Model Training:* Involves optimizing neural networks with parameters like batch size and learning rate.
5. *Model Evaluation:* Uses metrics like BLEU score, accuracy, precision, recall, and F1 score to assess performance.
6. *Model Testing:* Evaluates the trained model on unseen data to assess its generalization ability.
7. *Post-processing:* Improves the output's grammatical accuracy and fluency (e.g., handling punctuation, reordering).

### Results and Statistical Analysis:
The proposed MT system was evaluated against Google Translator and Bing Translator using BLEU scores:

- *English to Hindi Translation:* Achieved a BLEU score of 0.8824.
- *English to Marathi Translation:* Achieved a BLEU score of 0.7591.

The results demonstrate the system's effectiveness and reliability.

### Tables of Comparison:
#### English to Hindi Translation Examples:
1. *Input Sentence:* "Wow, that sunset is beautiful!"
   - *Google:* "वाह, वह सूर्यास्त सुंदर है!"
   - *Bing:* "वाह, कि सूर्यास्त सुंदर है!"
   - *Proposed:* "वाह, वह सूर्यास्त सुन्दर है!"

#### English to Marathi Translation Examples:
1. *Input Sentence:* "Wow, that sunset is beautiful!"
   - *Google:* "वा, तो सूर्यास्त सुंदर आहे!"
   - *Bing:* "वा, की सूर्यास्त सुंदर आहे!"
   - *Proposed:* "वा, तो सूर्यास्त सुंदर आहे!"

### Conclusion:
The proposed MT system using transformer models demonstrates significant improvements in translation accuracy and efficiency for English to Hindi and English to Marathi translations. This approach has the potential to enhance cross-cultural communication and promote linguistic inclusivity in digital environments.

---

### Key Points:
- *Objective:* Improve MT for English to regional languages (Hindi and Marathi) using transformer models.
- *Methodology:* Detailed pre-processing, feature extraction, model selection, training, evaluation, testing, and post-processing steps.
- *Results:* High BLEU scores indicating effective translation performance.
- *Conclusion:* Transformer models significantly improve translation quality, aiding in global communication and cultural exchange.
