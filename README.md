# bayesian-finance-notes

These are my personal notes as I work through **Bayesian Data Analysis (3rd Edition)** by Andrew Gelman, John Carlin, Hal Stern, David Dunson, Aki Vehtari, and Donald Rubin — commonly referred to as BDA3.

I'm making this because I want to understand more about Bayesian models and how do they apply in the field of finance to predict risk and investment outcomes. I want to replace the static, spreadsheet-based assumptions that break every traditional valuation model — fixed revenue growth rates, constant margins, rigid WACC inputs — with probabilistic, dynamically updated distributions that actually reflect how uncertain the future is.

This repo is not a summary of the textbook. It's my working translation of it — written the way I think, with analogies that make sense to me, equations broken down line by line when they show up, and a direct connection to financial modeling at every step.

---

## Why Bayesian?

A standard DCF model asks: *what is the revenue growth rate?* It picks a number — say 8% — and treats it as fact. When the next earnings report comes in at 3%, the model doesn't update. It just sits there, wrong.

A Bayesian model asks a different question: *what is the probability distribution over possible revenue growth rates, given everything I know?* Every new earnings release updates that distribution. The model is never "wrong" — it's just more or less certain.

That distinction — from a point estimate to a living distribution — is the entire reason I'm reading this book.

---

## Structure

Each chapter gets its own folder. Inside each folder:

- A `README.md` with the chapter overview and a map of all sections
- One markdown file per section, written in plain language with equations broken down inline
- A `financial-utility-summary.md` at the end of each chapter mapping every concept to a specific use case in financial modeling
- A `code/` folder with standalone `.py` model files and `.ipynb` Jupyter notebooks

---
<!-- 
## Chapters

| Chapter | Title | Status |
|---------|-------|--------|
| [Chapter 1](./chapter-01-probability-and-inference/README.md) | Probability and Inference | ✅ Complete |
| [Chapter 2](./chapter-02-single-parameter-models/README.md) | Single-Parameter Models | 🔄 In Progress |
| [Chapter 3](./chapter-03-multiparameter-models/README.md) | Introduction to Multiparameter Models | ⏳ Upcoming | -->

---

## Resources

- [Notation Reference](./resources/notation-reference.md) — every Greek letter and symbol used across all chapters, defined in plain English

---

## Stack

- **PyMC** — probabilistic programming in Python
- **Jupyter Notebooks** — walkthrough code with inline explanations
- **LaTeX in Markdown** — equations render on GitHub with proper Greek letters

---

*Reading BDA3 sequentially. Notes added chapter by chapter as I go.*
