import re

from transformers import AutoTokenizer, AutoModelForCausalLM
import datasets


def extract_regex(text):
    num_list = re.findall(r'\d+', text)
    if num_list is not None:
        return num_list
    else:
        return None


def score_mgsm(pred, answer_number) -> bool:
    if "." in pred:
        pred = pred.rstrip("0").rstrip(".")
    pred = pred.replace(",", "")
    if str(answer_number) == pred:
        return 1
    else:
        return 0


def main():
    df = datasets.load_dataset("juletxara/mgsm")
    df = df["test"]

    model_id = "merge_mgsm_train"
    model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")
    tokenizer = AutoTokenizer.from_pretrained(model_id)

    cnt = 0
    for i in range(len(df)):
        question = df["question"][i]
        prompt = f"次の数学の問題を解いてください。最終的な答えを出す前に、解答の推論過程を記述してください。答えには整数の答え以外何も追加しないでください。\n問題:{question}\n答え:"
        inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
        tokens = model.generate(
            **inputs,
            max_new_tokens=128,
            temperature=0.0,
            top_p=1.0,
            do_sample=False,
        )
        output = tokenizer.decode(tokens[0], skip_special_tokens=True)
        try:
            pred = extract_regex(output)[-1]
            score = score_mgsm(pred, df["answer_number"][i])
        except IndexError:
            score = 0
        cnt += score
    print(cnt/len(df))        
