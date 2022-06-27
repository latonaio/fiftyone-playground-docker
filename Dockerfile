FROM ubuntu:20.04

# 基本設定とパッケージのインストール
#
# SSH の鍵をイメージに含めるのはセキュリティ的に良くないので、ここでは削除し、
# 初回起動時 docker-entrypoint.sh 内で生成させる
RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \
	&& apt-get update \
	&& (DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade -y) \
	&& apt-get install -y neovim openssh-server python3-venv sudo libcurl4 \
	&& rm -rf /etc/ssh/ssh_host_*_key* \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*

# OpenSSH 設定を変更
RUN sed -i -e 's/^#Port 22$/Port 32222/;s/^#PermitRootLogin.*$/PermitRootLogin yes/' /etc/ssh/sshd_config

# ユーザーの作成
# RUN groupadd -g XXXXXXXX \
# 	&& useradd -g XXXX -u XXXX --create-home latona --shell /bin/bash -G sudo \
# 	&& (echo 'XXXXXXXXXXXXX' | chpasswd)
RUN echo 'root:XXXXXXXX' | chpasswd

# OpenSSH の自動起動スクリプト
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod 755 /docker-entrypoint.sh


# Python 環境の準備
# WORKDIR /home/latona/app
WORKDIR /root/app

RUN python3 -m venv venv \
	&& . venv/bin/activate \
	&& pip install wheel \
	&& pip install fiftyone \
	&& rm -rf /root/.cache/pip

# RUN chown -R XXXXXX:XXXXX /home/XXXXX

# ls に色を付けるなど、カスタマイズを適用
RUN cp /etc/skel/.* /root || true

# 起動時に自動で venv をアクティベートする
RUN (echo "source ~/.profile"; echo "source ~/app/venv/bin/activate") >> ~/.bash_profile


ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/usr/bin/sleep", "infinity"]
