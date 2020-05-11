# Subjective Answer Evaluator

The conventional way of paper checking is very hecting and mentally tiring. The problem can be resolved if this work is done by a machine which is trained for checking answers based on prior knowledge of evaluating answers. A subjective answer evaluator uses certain parameters/features which can help the machine judge the answer based on previous learning. The answer we wish to establish will be extracted using OCR and evaluated on different parameters.

PARAMETERS FOR EVALUATING ANSWERS
---------------------------------

    Context Similarity – It is important for the machine to understand the context of answer and then check if it similar to the teacher’s answer.
    Grammar Check – The answer should not have grammatical mistakes and the sentences should make sense. The model would rate the answer based on number of grammatical errors.
    Length of the answer – The length of answers is also very important when it comes to evaluating subjective answers. The model would check if the answer is within the permissible word limit.
    Keywords – The model would check the presence of the keywords that should be present in the answer.

Pre requisites
--------------

nltk, rake libraries

Implementation
--------------

The evaluation of the answer will be on a 10-point scale where the answer would be rated 0-10 based on the quality of answer.

    Context similarity – The context similarity between answers is calculated using a Heat map which contains the cosine distance between each word in student’s answer and teacher’s answer.
    Grammar Check – The python library named language_check checks for the grammatical errors in student’s answer and then computes the score.
    Length of the answer – The length of the answer is calculated using the regular expressions library and there is a dictionary which has word limit for answer with respect to maximum marks for the answer.
    Keywords – The rake library in python helps in extracting keywords from the answer according to their importance in the answer, these words are then searched in the student’s answer and if those words which are not found in the student’s answer then the PyDictionary helps in getting the synonyms of the words then these synonyms are then searched in the test. Based on the number of keywords present in students answer the score is computed.
