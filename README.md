# deep_eval

## 簡介

此程式使用 [deepeval](https://github.com/confident-ai/deepeval) 套件於評估大型語言模型（LLM）資料集上的表現，並計算模型的得分。程式支透過繼承 DeepEvalBaseLLM， 並呼叫litellm API 與指定的模型互動完成評估。

## 範例用法
```bash
python3 main.py --model ollama/llama3.1:8b --response_file data/res_llama3.1:8b.csv --score_file MMLU_llama3.1:8b.csv
```

## 可用參數說明：
| 參數名稱           | 必填   | 預設值                      | 功能說明                                                                 |
|--------------------|--------|----------------------------|------------------------------------------------------------------------|
| `--model`          | 否     | `ollama/llama3.2`          | 指定 LLM 模型名稱，用於 `litellm` API                                    |
| `--response_file`  | 否     | 無                         | 模型回應的保存路徑（若需要保存回應）                                      |
| `--score_file`     | 是     | 無                         | 評估結果（得分）的保存路徑                                              |
