import pandas as pd
import random 

file = pd.read_csv('questions.csv')

database = file.to_dict()

# list of objects
test_name = list(set(database['use'].values()))
subject_name = list(set(database['subject'].values()))

def questions_selection(test, subjects, nb_questions):

    """
    returns questions according to type of test (unique value expected), subjects (multiple selection allowed) 
    and finally number of questions wanted (among 5, 10 or 20)
    
    test: str
    subjects: list of str
    nb_questions : int

    """

    if len(subjects) > 1:
        df = file[(file.use==test)&(file.subject.isin(subjects))]
        questions = list(dict(df.question).values())
        selection_questions = random.choices(questions, k = nb_questions )
        return selection_questions

    else:
        df = file[(file.use==test)&(file.subject==subjects[0])]
        questions = list(dict(df.question).values())
        selection_questions = random.choices(questions, k = nb_questions )
        return selection_questions
    
  
  
        

