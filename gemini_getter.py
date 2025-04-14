from google import genai

class geminiGetter:
    key = '<<YOUR API KEY HERE>>'
    prompt = """Your task is to create flashcards from quizbowl questions I will provide. For each question, you need to identify individual clues and create a separate flashcard for each clue.

    Here are the important rules:

    1.  **Copy Text Directly:** When creating a flashcard, copy entire portions of text directly from the original quizbowl question for the "question" side of the flashcard.
    2.  **One Clue Per Flashcard:** Each flashcard should focus on only one specific piece of information (one clue) from the original question.
    3.  **Map Clues to Specific Answers:** Make sure the clue on the flashcard points to the *most specific* correct answer. For example, if a clue is about the tempest but the answer to the question is shakespeare, the answer to the flashcard should be the tempest
    4.  **Strict Output Format:** You MUST return every flashcard in the following exact format, with no other text or explanations:
        question1~answer1$question2~answer2$`
        
        Make sure there is a tilde (`~`) separating the question and answer for each flashcard, and a dollar sign (`$`) separating each individual flashcard.
        
    For example, if I give you the question: "This author of *The Catcher in the Rye* fought in World War II and later became reclusive in New Hampshire," you should create two flashcards like this:

    "This author of *The Catcher in the Rye*"~J.D. Salinger$"fought in World War II and later became reclusive in New Hampshire"~J.D. Salinger$
    
    Question for you : 
    """
    def __init__(self):
        self.god_of_your_world = genai.Client(api_key = self.key)

    def make_card(self, formatted_question):
        response = self.god_of_your_world.models.generate_content(model="gemini-2.0-flash", contents = self.prompt + formatted_question)#new model, 1.5flash old model.
        return response.text
