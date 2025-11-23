def build_prompt(user_data: dict, context_chunks: list[str]) -> str:
    context = "\n".join(context_chunks)

    weeks = user_data.get("weeks", 4)  # default to 4 if not provided

    prompt = f"""
You are a training assistant.

User Profile:
{user_data['user_profile']}

Recent Training:
{user_data['recent_training']}

Goal:
{user_data['request']}

Generate a structured {weeks}-week training block.
Break it down week-by-week and session-by-session.
Use the context below to guide your recommendations.

Context:
---
{context}
---
"""
    return prompt
