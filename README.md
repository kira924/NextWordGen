# NextWordGen: Next-Word Prediction Model
NextWordGen is my first NLP project that predicts the next word in a sequence using trigrams. 
It leverages Wikipedia data, applies Laplace smoothing, and calculates perplexity. 
Future updates will focus on enhancing prediction accuracy and perplexity evaluation.

## Features
- Next-word prediction: Predicts the next word based on the previous context using trigrams.
- Laplace smoothing: Enhances the prediction by refining probability estimates.
- Perplexity calculation: Evaluates the model’s performance.

## How It Works
1. Trigram model: Analyzes a sequence of three words to predict the next one.
2. Laplace smoothing: Refines predictions for unseen word combinations.
3. Perplexity: Measures the model’s accuracy by calculating the perplexity score.

## Requirements
- Python 3.x
- Libraries: `nltk`, `wikipedia-api`, `tkinter`

## Project Files
- `next_word_gen.py`: Core application for next-word prediction and smoothing.
- Sample data: Wikipedia articles used to build the model.

## Future Enhancements
- Improve perplexity evaluation for better performance.
- Expand the dataset and model for more accurate predictions.
