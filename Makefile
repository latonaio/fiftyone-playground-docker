.DEFAULT_GOAL := help
.SHELL := bash


.PHONY: docker-build
docker-build: ## Docker イメージのビルド
	docker compose build

.PHONY: launch
launch: ## ビルド済み Docker イメージからコンテナの作成と実行
	docker compose up -d

.PHONY: stop
stop: ## Docker コンテナの終了 (データは維持されます)
	docker compose stop fiftyone-playground

.PHONY: start
start: ## Docker コンテナの再開
	docker compose start fiftyone-playground

.PHONY: remove
remove: ## Docker コンテナの削除 (データがすべて削除されます)
	docker compose down || true
	docker compose rm || true

.PHONY: shell
shell: ## 実行中の Docker コンテナ内でシェルを実行 (トラブルシューティング用)
	docker compose exec fiftyone-playground /bin/bash

.PHONY: ssh
ssh: ## 実行中の Docker コンテナに SSH ログインする
	ssh -o "StrictHostKeyChecking=no" -o "UserKnownHostsFile=/dev/null" root@127.0.0.1 -p32222


# Self-Documented Makefile
# https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
