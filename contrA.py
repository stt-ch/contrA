import streamlit as st
import os
import openai

# Set your OpenAI API key as an environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

# Dictionary of Schopenhauer's strategies with their short descriptions
strategies = {
    "The Extension (Straw Man)": "Exaggerate or extend your opponent's argument to make it easier to attack.",
    "Homonymy (Equivocation)": "Use ambiguous terms and shift their meaning during the argument.",
    "Generalize Your Opponent's Specific Statements": "Turn a specific argument into a general one to attack the broader implications.",
    "Conceal Your Conclusion": "Present your argument in a way that the opponent doesn't realize the conclusion you are leading to.",
    "Use Your Opponent’s Beliefs Against Them": "Use your opponent’s own beliefs or principles against them.",
    "Appear to Yield": "Pretend to concede a point but twist it to your advantage.",
    "Question Instead of Stating": "Use questions instead of statements to make it harder for your opponent to counter.",
    "Make Your Opponent Angry": "Get your opponent emotional to make them less logical and easier to defeat.",
    "Use Ridicule": "Mock your opponent’s argument to undermine its credibility.",
    "Present False Choices (False Dilemma)": "Force your opponent into a situation where they must choose between two unfavorable options.",
    "Claim Victory Despite Defeat": "Assert that you’ve won the argument, regardless of the actual outcome.",
    "Personal Attack (Ad Hominem)": "Attack the character or motives of your opponent instead of addressing their argument.",
    "Lead Your Opponent Into a Contradiction": "Guide your opponent into making contradictory statements.",
    "Appeal to Authority": "Cite an authority figure or expert to support your argument, even if irrelevant.",
    "Appeal to the Majority (Ad Populum)": "Argue that because many people believe something, it must be true.",
    "Appeal to Emotions": "Manipulate emotions such as fear, pity, or anger to support your argument.",
    "Ignore Your Opponent’s Evidence": "Simply dismiss or ignore any evidence presented by your opponent.",
    "Use Metaphors or Analogies": "Employ metaphors or analogies to make your argument more persuasive.",
    "Use Their Own Words Against Them": "Twist your opponent’s words to contradict their own argument.",
    "Challenge to Justify": "Demand that your opponent justify their basic premises or beliefs.",
    "Refuse to be Provoked": "Stay calm and composed to prevent your opponent from gaining the upper hand emotionally.",
    "Confuse the Issue": "Introduce irrelevant issues or obscure the topic to sidetrack your opponent.",
    "Take Advantage of Your Opponent’s Gaps in Knowledge": "Exploit any gaps or weaknesses in your opponent’s knowledge.",
    "Change the Subject": "Shift the discussion to a different topic that’s more favorable to your argument.",
    "State a Lie": "Boldly assert something false, relying on the fact that it might not be challenged.",
    "Give Your Opponent the Challenge": "Challenge your opponent to prove something that’s difficult or impossible to prove.",
    "Diversion by Answering Something Else": "Respond to a different question than the one asked to avoid answering directly.",
    "Make Your Opponent Admit Something": "Get your opponent to admit to something that weakens their position.",
    "Put the Opponent on the Defensive": "Force your opponent to defend their position rather than attack yours.",
    "Refute by Preemptive Argument": "Anticipate and refute potential arguments from your opponent before they’re made.",
    "Use Arbitrary Definitions": "Define key terms in a way that is favorable to your argument.",
    "Turn the Tables": "Reverse the situation or argument to put your opponent on the defensive.",
    "Appeal to Inconsistent Statements": "Highlight any inconsistencies in your opponent’s statements to discredit them.",
    "Break Down Their Argument into Smaller Pieces": "Deconstruct your opponent’s argument into smaller parts to attack them individually.",
    "Force a Choice Between Two Alternatives": "Present a situation as a binary choice, even if there are more options available.",
    "Use Generalities and Vague Statements": "Make broad, vague statements that are hard to refute but seem persuasive.",
    "Draw Conclusions from Assumptions": "Base your argument on assumptions rather than facts, drawing conclusions from them.",
    "Silence Your Opponent": "Use techniques that effectively silence or confuse your opponent, leaving them unable to respond."
}

# Streamlit UI
st.title("contrA - Schopenhauer's Argument Counter")

# Opponent's argument input
opponent_argument = st.text_area("Enter the opponent's argument:")

# Your argument input
your_argument = st.text_area("Enter your argument:")

# Strategy selection
selected_strategies = st.multiselect(
    "Select Schopenhauer's strategies to apply:",
    list(strategies.keys())
)

# Display strategy descriptions
if selected_strategies:
    descriptions = "\n\n".join([f"**{strategy}:** {strategies[strategy]}" for strategy in selected_strategies])
    st.markdown(descriptions)

# Counter button
if st.button("Counter"):
    # Combine selected strategies into a prompt
    strategies_prompt = ", ".join(selected_strategies)
    prompt = f"Counter the following argument using these strategies: {strategies_prompt}\n\nOpponent's Argument: {opponent_argument}\n\nYour Argument: {your_argument}"
    
    # Make a request to OpenAI
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )
   
    # Display the counter-argument
    counter_argument = completion.choices[0].message['content']
    st.subheader("Counter-Argument:")
    st.text_area("Generated Counter-Argument:", value=counter_argument, height=200)
