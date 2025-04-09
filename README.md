<!-- intro fig eval-pipeline 需要的文件-->

# VCR-Bench: A Comprehensive Evaluation Framework for Video Chain-of-Thought Reasoning

![VideoQA](https://img.shields.io/badge/Task-VideoQA-red) 
![Multi-Modal](https://img.shields.io/badge/Task-Multi--Modal-red) 
![Video-MME](https://img.shields.io/badge/Dataset-V2P--Bench-blue)  
![Gemini](https://img.shields.io/badge/Model-Gemini-green)
![GPT-4o](https://img.shields.io/badge/Model-GPT--4o-green)
![LLaVA-Video](https://img.shields.io/badge/Model-%20LLaVA--Video-green
)


<font size=7><div align='center' >  [[📖 arXiv Paper]()] [[📊 Dataset]()]  [[🏆 Leaderboard(TBD)]()]  </div></font>

---

## 🔥 News
* **`2025.04.11`** 🌟 We have released **VCR-Bench**, a novel benchmark designed to comprehensively evaluate LVLMs' **V**ideo **C**hain-of-Thought **R**easoning capabilities

---

## 👀 Introduce V2P-Bench

<p align="center">
    <img src="./figs/main_v2.pdf" width="100%" height="100%">
</p>

The advancement of Chain-of-Thought (CoT) reasoning has significantly enhanced the capabilities of large language models (LLMs) and large vision-language models (LVLMs). However, a rigorous evaluation framework for video CoT reasoning remains absent. Current video benchmarks fail to adequately assess the reasoning process and expose whether failures stem from deficiencies in perception or reasoning capabilities. Therefore, we introduce \textbf{VCR-Bench}, a novel benchmark designed to comprehensively evaluate LVLMs' \textbf{V}ideo \textbf{C}hain-of-Thought \textbf{R}easoning capabilities. VCR-Bench comprises 859 videos spanning a variety of video content and durations, along with 1,034 high-quality question-answer pairs. Each pair is manually annotated with a stepwise CoT rationale, where every step is tagged to indicate its association with the perception or reasoning capabilities. Furthermore, we design seven distinct task dimensions and propose the CoT score to assess the entire CoT process based on the stepwise tagged CoT rationals. Extensive experiments on VCR-Bench highlight substantial limitations in current LVLMs. Even the top-performing model, o1, only achieves a 62.8\% CoT score and an 56.7\% accuracy, while most models score below 40\%. Experiments show most models score lower on perception than reasoning steps, revealing LVLMs' key bottleneck in visual information processing for complex video reasoning. A robust positive correlation between the CoT score and accuracy confirms the validity of our evaluation framework and underscores the critical role of CoT reasoning in solving complex video reasoning tasks. We hope VCR-Bench to serve as a standardized evaluation framework and expose the actual drawbacks in complex video reasoning. 