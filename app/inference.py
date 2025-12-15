import json
import torch
from transformers import AutoTokenizer, AutoModelForTokenClassification
from pathlib import Path

# Resolve project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Absolute path to model directory
MODEL_PATH = BASE_DIR / "resume_ner_model"

# Load tokenizer & model
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForTokenClassification.from_pretrained(MODEL_PATH)
model.eval()

# Load label mapping
id2label = model.config.id2label


def extract_entities(text: str):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    with torch.no_grad():
        outputs = model(**inputs)

    predictions = outputs.logits.argmax(dim=-1)[0]
    tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])

    entities = {}
    current_entity = ""
    current_label = None

    for token, pred_id in zip(tokens, predictions):
        label = id2label[pred_id.item()]

        if token in ["[CLS]", "[SEP]"]:
            continue

        if label == "O":
            if current_entity and current_label:
                entities.setdefault(current_label, []).append(current_entity.strip())
                current_entity = ""
                current_label = None
            continue

        tag, entity_type = label.split("-", 1)

        is_subword = token.startswith("##")
        clean_token = token[2:] if is_subword else token

        if tag == "B":
            if current_entity and current_label:
                entities.setdefault(current_label, []).append(current_entity.strip())

            current_entity = clean_token
            current_label = entity_type

        elif tag == "I" and current_label == entity_type:
            if is_subword:
                current_entity += clean_token
            else:
                current_entity += " " + clean_token

        else:
            if current_entity and current_label:
                entities.setdefault(current_label, []).append(current_entity.strip())

            current_entity = clean_token
            current_label = entity_type

    if current_entity and current_label:
        entities.setdefault(current_label, []).append(current_entity.strip())

    EXPECTED_ENTITIES = [
        "ROLE",
        "COMPANY",
        "START_DATE",
        "END_DATE"
    ]

    for ent in EXPECTED_ENTITIES:
        entities.setdefault(ent, [])

    return entities


