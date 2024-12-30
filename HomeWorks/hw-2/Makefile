PIP := venv/bin/pip
PYTHON3 := venv/bin/python3

clear: ## удалить виртуальное окружение
	rm -rf venv

venv: ## создать виртуальное окружение
	python3 -m venv venv

install_requirements: ## yстановить зависимости из requirements.txt
	${PIP} install --upgrade pip
	${PIP} install -r requirements.txt

run:
	${PYTHON3} server.py

add_dependency: ## добавить зависимость в requirements.txt
	@echo "Какой пакет вы хотите установить? (Введите название) "
	@read package; ${PIP} install $$package && ${PIP} freeze > requirements.txt


help: # вывести список доступных команд
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'