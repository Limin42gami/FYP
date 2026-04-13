import os
from google import genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def initialize_client():
    """Initialize the Gemini client with API key"""
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable is not set. Please set it in .env file.")

    return genai.Client(api_key=api_key)

import random

def generate_joke(topic):
    """
    Generate a joke based on the user's topic using Google Gemini API

    Args:
        topic (str): The user's topic for joke generation

    Returns:
        str: Generated joke response
    """
    try:
        client = initialize_client()

        # Dynamic joke structures to ensure variety
        joke_structures = [
            "QUESTION_ANSWER",      # Why did X...? Because Y.
            "OBSERVATIONAL",        # You know what's funny about X?
            "PUN_BASED",           # Wordplay and double meanings
            "SITUATIONAL",         # Imagine if X happened...
            "COMPARISON",          # X is like Y, but...
            "PERSONIFICATION",     # If X could talk...
            "HYPERBOLE",           # X is so [adjective] that...
            "UNDERSTATEMENT",      # X is slightly [adjective]...
            "RULE_OF_THREE",       # X, Y, and Z walk into a bar...
            "TWIST_EXPECTATIONS"   # Everyone thinks X, but actually Y.
        ]

        selected_structure = random.choice(joke_structures)

        # Advanced system instruction with variety enforcement
        system_instruction = f"""
        You are a versatile comedy genius who can create ANY type of humor flawlessly.
        You have mastered every comedy format and can switch between them effortlessly.
        NEVER use the same joke structure twice in a row - always vary your approach!

        TODAY'S FORMAT: {selected_structure}

        COMEDY MASTERY RULES:
        1. AVOID REPETITIVE PATTERNS - Never start multiple jokes with "I", "My", "Why did", etc.
        2. STRUCTURAL VARIETY - Mix Q&A, observations, puns, stories, one-liners
        3. PERSPECTIVE SHIFTING - Use different voices: narrator, character, expert, etc.
        4. TIMING VARIATION - Some quick punchlines, others with more setup
        5. THEMATIC DIVERSITY - Connect topics to unexpected domains

        JOKE STRUCTURES YOU MUST MASTER:

        🔹 QUESTION_ANSWER: "Why/What/How/When did [topic]...?" + clever answer
        🔹 OBSERVATIONAL: "You know what I don't get about [topic]?" + insight
        🔹 PUN_BASED: Play on words related to {topic}
        🔹 SITUATIONAL: "Imagine a [topic] at a dinner party..." + scenario
        🔹 COMPARISON: "[Topic] is like [unexpected thing] because..."
        🔹 PERSONIFICATION: "If [topic] could talk, it would say..."
        🔹 HYPERBOLE: "[Topic] is so [adjective] that..."
        🔹 UNDERSTATEMENT: "[Topic] is a bit [mild adjective]..."
        🔹 RULE_OF_THREE: "[Topic A], [Topic B], and [Topic] walk into..."
        🔹 TWIST_EXPECTATIONS: "Everyone thinks [topic] is X, but actually..."

        DIVERSITY MANDATES:
        ✅ Vary sentence lengths (1-4 sentences max)
        ✅ Switch between first-person and third-person perspectives
        ✅ Use different openings: Questions, statements, scenarios, dialogues
        ✅ Mix direct and indirect humor styles
        ✅ Alternate between punchline endings and amusing observations
        ✅ Include personal story formats occasionally for relatable humor

        PATTERNS TO USE IN MODERATION:
        ⚠️ "I finally/tried/asked/bought..." - Great for relatable stories, but don't overuse
        ⚠️ "My [family member/friend/pet]..." - Personal anecdotes can be hilarious when used sparingly
        ⚠️ "You won't believe..." - Good for setup, but mix with other approaches

        AVOID EXCESSIVE REPETITION:
        ❌ Using the exact same starter pattern 3+ times in a row
        ❌ Always defaulting to the same joke structure regardless of topic
        ❌ Never switching between different comedy styles

        CONTENT STANDARDS:
        - Keep universally appropriate and clever
        - Maximum 3 sentences unless absolutely necessary
        - Every word must serve the humor
        - No meta-commentary or joke explanations

        CHALLENGE: Create a {selected_structure} joke about {topic} that feels completely fresh and original!
        """

        # Dynamic prompt based on selected structure
        structure_prompts = {
            "QUESTION_ANSWER": f"Create a clever question-and-answer joke about {topic}. Start with Why/What/How/When and deliver a surprising punchline.",
            "OBSERVATIONAL": f"Create an observational comedy joke about {topic}. Start like you're noticing something funny about it.",
            "PUN_BASED": f"Create a brilliant pun or wordplay joke about {topic}. Focus on clever language twists.",
            "SITUATIONAL": f"Create a situational comedy joke about {topic}. Put it in an unexpected scenario.",
            "COMPARISON": f"Create a comparison joke about {topic}. Compare it to something completely different.",
            "PERSONIFICATION": f"Create a personification joke about {topic}. Imagine if it could talk or have feelings.",
            "HYPERBOLE": f"Create a hyperbole joke about {topic}. Exaggerate something about it to absurd levels.",
            "UNDERSTATEMENT": f"Create an understatement joke about {topic}. Downplay something obvious about it.",
            "RULE_OF_THREE": f"Create a rule-of-three joke about {topic}. Use the classic three-item comedy structure.",
            "TWIST_EXPECTATIONS": f"Create a joke about {topic} that twists common expectations."
        }

        enhanced_prompt = f"""
        FORMAT: {selected_structure}

        {structure_prompts[selected_structure]}

        CRITICAL: Make this completely different from typical joke patterns. Be original, surprising, and genuinely clever.

        Topic: {topic}
        """

        response = client.models.generate_content(
            model='gemini-flash-lite-latest',
            contents=enhanced_prompt,
            config={'system_instruction': system_instruction}
        )

        # Clean up the response
        joke = response.text.strip()

        # Remove any unwanted prefixes
        if joke.startswith("Here's") or joke.startswith("Here is"):
            joke = joke.split('\n', 1)[-1].strip()

        return joke

    except Exception as e:
        # Varied fallback jokes to avoid repetition
        fallback_jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "I told my computer I needed a break, and it said 'no problem, I'll go to sleep.'",
            "Why did the scarecrow win an award? He was outstanding in his field!",
            "I'm reading a book about anti-gravity. It's impossible to put down!",
            "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
            "Why don't eggs tell jokes? They'd crack each other up!"
        ]
        return random.choice(fallback_jokes)
