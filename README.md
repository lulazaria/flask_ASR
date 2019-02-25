# Flask backed Web Interface for pre-trained ASR model with kaldi
This is a simple web interface with a Flask backend for a pre-trained ASR model using Kaldi speech recognition toolkit.


## Pip
### Install Requirements
```bash
sudo pip install -r requirments.txt
```

### Clone kaldi and get the pre-trained model
~~~
git clone https://github.com/kaldi-asr/kaldi
cd kaldi/egs/aspire/s5
wget http://dl.kaldi-asr.org/models/0001_aspire_chain_model.tar.gz
tar xfv 0001_aspire_chain_model.tar.gz
~~~
clone this repository and copy contents to <kaldi-folder>/egs/aspire/s5

### Usage


Start the server 
```python 
python server.py
```
Go to your web browser and start a client with http://localhost:5000
## Docker

Build the image with
~~~
docker build --tag=flask_asr .
~~~
Run with 
~~~
docker run flask_asr
~~~


 
