[![Actions Status](https://github.com/Vitaocy/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Vitaocy/python-project-50/actions)
[![pyci](https://github.com/Vitaocy/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/Vitaocy/python-project-50/actions/workflows/pyci.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Vitaocy_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Vitaocy_python-project-50)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=Vitaocy_python-project-50&metric=bugs)](https://sonarcloud.io/summary/new_code?id=Vitaocy_python-project-50)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=Vitaocy_python-project-50&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=Vitaocy_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=Vitaocy_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=Vitaocy_python-project-50)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=Vitaocy_python-project-50&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=Vitaocy_python-project-50)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=Vitaocy_python-project-50&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=Vitaocy_python-project-50)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=Vitaocy_python-project-50&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=Vitaocy_python-project-50)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=Vitaocy_python-project-50&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=Vitaocy_python-project-50)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=Vitaocy_python-project-50&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=Vitaocy_python-project-50)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=Vitaocy_python-project-50&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=Vitaocy_python-project-50)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=Vitaocy_python-project-50&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=Vitaocy_python-project-50)

# Вычислитель отличий (gendiff)

Вычислитель отличий — это инструмент командной строки для поиска различий между двумя файлами.

Поддерживаемые форматы: 
- **JSON** (.json)
- **YAML** (.yaml, .yml)

## Зависимости:
- **Python** = ">=3.13"
- *make* (стандартная утилита Linux / macOS)

## Установка:
```bash
git clone https://github.com/Vitaocy/python-project-50.git
cd python-project-50
make install
make build
make package-install
```

## Примеры команд для разных форматов вывода:
1. Вывод в стиле **stylish** (по-умолчанию)
```bash
gendiff filepath1.json filepath2.json
```
2. Вывод в формате **plain**
```bash
gendiff -f plain filepath1.json filepath2.json
```
3. Вывод в формате **json**
```bash
gendiff -f json filepath1.json filepath2.json
```


## Asciinema с примерами использования:
#### Файлы .JSON (-f stylish):
[![asciicast](https://asciinema.org/a/I6ZjNCjJRFGjbHKW.svg)](https://asciinema.org/a/I6ZjNCjJRFGjbHKW)

#### Файлы .YAML (-f stylish):
[![asciicast](https://asciinema.org/a/xGwiOv1oNltuZxpd.svg)](https://asciinema.org/a/xGwiOv1oNltuZxpd)

#### Файлы .json и .yaml (-f stylish)
[![asciicast](https://asciinema.org/a/CjczjtYSaAlQyOnC.svg)](https://asciinema.org/a/CjczjtYSaAlQyOnC)

#### Файлы с вложенными структурами .json (-f plain)
[![asciicast](https://asciinema.org/a/0fKhJmC9X6gMWzhI.svg)](https://asciinema.org/a/0fKhJmC9X6gMWzhI)

#### Простой .json в машиночитаемом формате (-f json)
[![asciicast](https://asciinema.org/a/rbRoyjnLGNuHX1Zk.svg)](https://asciinema.org/a/rbRoyjnLGNuHX1Zk)
