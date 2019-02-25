
FROM python:2.7-slim
MAINTAINER lulazaria <azarialulseged96@email.com>
WORKDIR /app
COPY . /app
RUN  apt-get update && apt-get install -y git
RUN  apt-get install  -y zlib1g-dev automake autoconf unzip wget sox libtool subversion python3
RUN  apt-get install -y libatlas3-base
RUN  apt-get install -y build-essential
RUN  apt-get install -y  make 



RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 5000
RUN git clone https://github.com/kaldi-asr/kaldi  
COPY . /kaldi/egs/aspire/s5/
RUN cd kaldi/tools && make 
RUN cd kaldi/src && ./configure --shared && make

RUN cd kaldi/egs/aspire/s5/ && wget http://dl.kaldi-asr.org/models/0001_aspire_chain_model.tar.gz && tar xfv 0001_aspire_chain_model.tar.gz && steps/online/nnet3/prepare_online_decoding.sh --mfcc-config conf/mfcc_hires.conf data/lang_chain exp/nnet3/extractor exp/chain/tdnn_7b exp/tdnn_7b_chain_online && utils/mkgraph.sh --self-loop-scale 1.0 data/lang_pp_test exp/tdnn_7b_chain_online exp/tdnn_7b_chain_online/graph_pp && ./path.sh && ./cmd.sh
RUN cd kaldi/egs/aspire/s5/ && chmod +x lat.sh output.sh test.sh

WORKDIR  /app/kaldi/egs/aspire/s5/
CMD ["python", "server.py"]

