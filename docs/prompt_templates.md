# 🧠 Prompt Templates for Periodization.AI

This file defines prompt formats used in RAG workflows for personalized training generation, evaluation, and insight delivery.

---

## 🏋️‍♂️ Training Block Generator Prompt

> Use case: Generate a personalized 4-week mesocycle plan

```json
{
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
    "deload_last_week": true
  },
  "request": "Generate a new 4-week block focused on squat strength and conditioning."
}
