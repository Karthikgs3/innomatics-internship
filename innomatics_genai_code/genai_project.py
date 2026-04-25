from transformers import pipeline

# Text Generation Model
generator = pipeline("text-generation", model="gpt2")

# Summarization Model
summarizer = pipeline("summarization")

# Question Answering Model
qa_model = pipeline("question-answering")


def generate_text(prompt):
    result = generator(prompt, max_length=60, num_return_sequences=1)
    return result[0]['generated_text']


def summarize_text(text):
    result = summarizer(text, max_length=50, min_length=20, do_sample=False)
    return result[0]['summary_text']


def answer_question(question, context):
    result = qa_model(question=question, context=context)
    return result['answer']


# ------------------ DEMO ------------------

if __name__ == "__main__":

    print("\n--- TEXT GENERATION ---")
    prompt = "Artificial Intelligence is transforming"
    print(generate_text(prompt))

    print("\n--- SUMMARIZATION ---")
    long_text = """
    Artificial Intelligence is a rapidly growing field in technology.
    It enables machines to learn from data, make decisions, and improve over time.
    Applications include healthcare, finance, automation, and more.
    """
    print(summarize_text(long_text))

    print("\n--- QUESTION ANSWERING ---")
    context = "FastAPI is a modern Python framework used for building APIs quickly."
    question = "What is FastAPI used for?"
    print(answer_question(question, context))