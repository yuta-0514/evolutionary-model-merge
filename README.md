# Evolutionary Model Merge
[Evolutionary Optimization of Model Merging Recipes](https://sakana.ai/evolutionary-model-merge-jp/)

## Install Libraries
```
git clone https://github.com/arcee-ai/mergekit.git
cd mergekit
pip install -e .[evolve]
```

## Dataset
[MGSM](https://huggingface.co/datasets/juletxara/mgsm)

## Model Merge
```
mergekit-evolve ./evol_merge_config.yml \
		--storage-path evol_merge_storage \
		--task-search-path eval_tasks \
		--in-memory \
		--no-merge-cuda --wandb
```

## Save Best Parameter
```
mergekit-yaml evol_merge_storage/best_config.yaml merge
```

## Evaluate
```
Python eval_mgsm.py
```

| Model | Type | Size | MGSM-JA |
| -- | -- | -- | -- |
| Shisa Gamma 7B v1 | JA general | 7B |  |
| WizardMath 7B v1.1 | EN math | 7B |  |
| Abel 7B 002 | EN math | 7B |  |
| EvoLLM-JP |  |  |  |
| Merged Model | 1+2+3 | 7B |  |

## Citation
- https://sakana.ai/evolutionary-model-merge-jp/
- https://acro-engineer.hatenablog.com/entry/2024/05/07/124507
- https://note.com/npaka/n/n42129c043026
- https://github.com/openai/simple-evals/tree/main

### TODO
- Train(8件)
	best_score 0.75
	evaluations 108
	population/mgsm_train_acc_max 0.5
	population/mgsm_train_acc_mean 0.5
	population/mgsm_train_acc_min 0.5
	population/score_mean 0.5
	population/score_std 0.0
- Train+Testの一部を使用、Trainの8件のみanswerを入れる
- 生成文に英語が残る場合 → MTBenchをタスクに導入
- MGSMスコアを算出
 - augmxnt/shisa-gamma-7b-v1
 - WizardLMTeam/WizardMath-7B-V1.1
 - GAIR/Abel-7B-002