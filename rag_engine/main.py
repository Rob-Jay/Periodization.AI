from rag_pipeline import run_rag

if __name__ == "__main__":
    # Sample input (you can replace this with real data or load from a file)
    user_input = {
        "weeks": 10,
        "user_profile": {
            "age": 25,
            "sex": "male",
            "height_cm": 181,
            "weight_kg": 90,
            "experience": "intermediate",
            "goal": "Increase squat strength and improve 5K time",
            "available_days": 5,
            "equipment": ["barbell", "dumbbells", "track access"]
        },
        "recent_training": {
            "posterior_chain_volume": 72,
            "quads_volume": 60,
            "conditioning_sessions": 3,
            "deload_last_week": True
        },
        "request": "Generate a new block focused on squat strength and conditioning."
    }


    output = run_rag(user_input)
    print("\n--- AI-Generated Training Plan ---\n")
    print(output)