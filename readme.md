# TDT13 Exploring Hallucination Rate in LLMs based on Role-Based Prompt Wording 

## Aquiring DefAn. 

The chosen data set is DefAn which has 75k+ prompt/answer responses. As this is quite a large dataset, I will therefore not upload it directly into the repository, but I am leaving the instructions here for how to get the dataset in order to rerun the experiments.  

Furthermore, I only used 10K of the Data from DefAn, which is respectively aquired from set 1, 2 and 3(as far as it went). 

Run in terminal:  

git clone https://github.com/ashikiut/DefAn.git. 


## Installing Dependencies
Make sure all dependencies are downloaded in the project.

## Running project

Batches only accepts jsonl format.  

https://www.pythontutorials.net/blog/python-conversion-from-json-to-jsonl/. 

Start by running the src/json_converter files. 

You now have three jsonl files in processed_defan folder.

## How to set up Batch System Documentation

Documentation retrieved from OpenAi.

After failing with GPT2, a locally ran openai model I got from huggingface, I realized I would need something that was not ran locally. Thus I started looking for online models to run. Here I first checked out Huggingface, as they have over a million different models, but I saw that they did not have any SotA generative models - which makes sense, since SotA has now switched over to use for pay.    

Batch API was ultimately chosen based on the asynchronous batch polling, with a 24 Hour return rate. This marked the paradigmn shift from synchroneous, 1 by 1 prompting to whatever jobs free polling. 


### Set up OpenAI account
So the first thing I would advise a person trying to recreate this to do is to set up an openai account(which is linked to the different models they have). https://openai.com/ and https://platform.openai.com/docs/api-reference/batch/create were used to set up Batching.

In order to duplicate this method, it must be noted that it costs about 13 kroner(or 5 USD) to run these prompts in the OpenAI batch model.

### Set up API Key in account

Create an API key in order to send in the files to OpenAI Batch. Documentation: https://platform.openai.com/docs/guides/batch/batch-api

### Initialize Key

run  

export OPENAI_API_KEY="sk-somethingsomething_yourkey_here"  

in your terminal so the key is linked.

## Send Batches
Send in the prompts from the files in src/batch.

Bevare - it can take up to 24 hours pr batch.

## How to set up Bert
Huggingface documentation: https://huggingface.co/docs/transformers/en/model_doc/bert

## How to set up Bart

Documentation: https://bart-doc.readthedocs.io/en/latest/index.html

Huggingface documentation: https://huggingface.co/docs/transformers/en/model_doc/bart

Digitalocean tutorial: https://www.digitalocean.com/community/tutorials/bart-model-for-text-summarization-part1
