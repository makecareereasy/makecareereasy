### Added files for Emotion analysis. This is different from Sentiment Analysis, which divides into categories(Positive, Negative, or Neutral).
### Emotion Analysis is more specific.
________________________________________________________________________________________________________
# Emotion Detection from text using PyTorch

# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anmol-sinha-coder/Sentiment_Emotion_Analysis/blob/main/Multi_Emotion_Analyzer/Emotion_detection_from_text_using_PyTorch.ipynb)<--Click on the icon to open Google CoLab

## Project Notebook
Open project [notebook](Emotion_detection_from_text_using_PyTorch.ipynb).

## The Project

### What is the project about?
This project is about performing emotion detection from text using PyTorch and Federated Learning.
For this project, we implemented an NLP task of creating a model to detect the emotion from text. We developed this using the PyTorch library where we created our Deep Neural Network using GloVe Word Embeddings, LSTMs and fully connected layers. Additionally we added the Federated Learning framework for decentralized training.

### Dataset

Phase | Instances | File |
--- | --- | --- |
Training | 132 | train.csv |
Testing | 56 | test.csv |

* Each sentence contains maximum 10 words.     
* GloVe Embedding used: `glove.6B.50d.txt`   
The embedding can be downloaded from [here](https://worksheets.codalab.org/rest/bundles/0x97c870dd60eb4f0fa53f257978851c60/contents/blob/glove.6B.50d.txt ).

For example:

| Sentence | Emotion   |
|----------|-----------|
|food is life|  🍽 Foodie|
|I love you mum|  ❤️ Loving|
|Stop saying bullshit|  😞 Annoyed|
|congratulations on your acceptance|  😄 Happy|
|The assignment is too long|    😞 Annoyed|
|I want to go play| ⚽️ Playful|
|she did not answer my text| 😞 Annoyed|
|Your stupidity has no limit| 😞 Annoyed|
|how many points did he score|  ⚽️ Playful|
|my algorithm performs poorly| 😞 Annoyed|
|I got approved|  😄 Happy|


### Emotions

We will create an emotion detection for the following 5 emotions:

| Emotion | Emoji   | Label   |
|------|------|------|
|Loving| ❤️| 0|
|Playful| ⚽️| 1|
|Happy| 😄| 2|
|Annoyed| 😞| 3|
|Foodie| 🍽| 4|

### Model
We will build an LSTM model that takes as input word sequences that will take word ordering into account. We will use 50-dimensional GloVe pre-trained word embeddings to represent words. We will then feed those as an input into an LSTM that will predict the most appropiate emotion for the text.
![Model Architecture](https://drive.google.com/uc?id=1s-KYhU5JWF-jvAlZ2MIKKugxLLDdhpQP "Model Architecture")

### Results
We are able to succesfully create a model that could achieve an accuracy of `84.4%` in our training set and also were able to use our model on user inputted sentences and were able to get expected emotion outputs.

`Test Loss: 1.064..  Test Accuracy: 0.844`

The following results are emotion predictions on user inputted sentences:
```

Input Text: 	I hate you
Emotion: 	😞 Annoyed

Input Text: 	I want a pizza
Emotion: 	🍽 Foodie

Input Text: 	Lets see the match
Emotion: 	😞 Annoyed

Input Text: 	I love you Lisa
Emotion: 	❤️ Loving

Input Text: 	This is the best day of my life
Emotion: 	😄 Happy

```

### Open Issues
We additionally added Federated Learning in our project and our code is  is meant to work out of the box, however at the time of project submission, there is an open issue in PySyft that causes an error with the LSTM implementation in PyTorch while performing Federated Learning. 

The problem is that GRUs and LSTMs from PyTorch use the method `.size()` to get the shape of tensors. It works well in PyTorch code, but it doesn’t in PySyft, because while performing Federated Learning with remote tensors, the `.size()` of a pointer is always `0` and we only can use `.shape` on pointers to get the shape of the tensor.
