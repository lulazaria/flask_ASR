# Flask backed Web Interface for pre-trained ASR model with kaldi
This is a simple web interface with a Flask backend for a pre-trained ASR model.
## Install Requirements

### Pip

```bash
sudo pip install -r requirments.txt
```

## Clone kaldi and get the pre-trained model
~~~
git clone https://github.com/kaldi-asr/kaldi

cd kaldi/egs/aspire/s5
wget http://dl.kaldi-asr.org/models/0001_aspire_chain_model.tar.gz
tar xfv 0001_aspire_chain_model.tar.gz
git clone flask_ASR
~~~
## Usage

Start the server 
```python 
python server.py
```
Go to your web browser start a client with localhost:5000


 
