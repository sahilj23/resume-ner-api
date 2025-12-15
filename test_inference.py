from app.inference import extract_entities

sample_text = """
Sahil Jain worked as a Data Analyst at Top Trove Foundation from April 2025 to June 2025.
"""

entities = extract_entities(sample_text)

print(entities)
