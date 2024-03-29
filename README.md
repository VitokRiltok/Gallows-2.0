# Техническое задание (ТЗ) для игры "Виселица"

## Функциональность проекта

Игра "Виселица" - это консольная игра, предназначенная для развлечения пользователей. Главной целью игры является угадывание слова, буква за буквой, прежде чем виселица будет нарисована полностью. Игра должна предоставлять следующую функциональность:

1. Начало новой игры с выбором случайного слова из заданного списка.
2. Отображение текущего состояния слова с угаданными и неугаданными буквами.
3. Отображение виселицы и висящего человечка в зависимости от количества ошибочных попыток.
4. Возможность ввода букв пользователем.
5. Проверка введенной буквы и обновление состояния слова и виселицы.
6. Подсчет и отображение количества попыток и использованных букв.
7. Определение исхода игры (победа или поражение) и вывод соответствующего сообщения.

## Формат входных данных

Игра "Виселица" не требует внешних входных данных. Все необходимые данные генерируются и обрабатываются внутри приложения. Однако, при необходимости, можно предусмотреть внешний список слов для выбора.

## Интерфейс приложения

Приложение работает в интерактивном режиме в текстовой консоли. Элементы интерфейса включают в себя следующие:

1. Приветственное сообщение, объясняющее правила игры и приглашение начать новую игру.
2. Отображение текущего состояния слова (с буквами и пропусками для неугаданных букв).
3. Отображение виселицы и висящего человечка на основе количества ошибочных попыток.
4. Поле для ввода буквы пользователем.
5. Сообщения о результате каждой попытки, включая успешные и неуспешные попытки.
6. Сообщения о победе или поражении после завершения игры.

## Аргументы командной строки (опционально)

Приложение может принимать следующие аргументы командной строки:

- `-w` или `--wordlist`: Путь к файлу со списком слов для выбора в игре. Если не указан, используется встроенный список слов.
- `-m` или `--max_attempts`: Максимальное количество попыток (ошибок), прежде чем игра будет завершена. По умолчанию: 6.

Пример использования:

`python hangman.py -w wordlist.txt -m 8`

## Использование внешних данных (опционально)

Если необходимо использовать внешние данные (например, конфигурационный файл), необходимо предоставить формат файла и описание протокола взаимодействия. В данной игре такая необходимость отсутствует, но можно реализовать функциональность загрузки списка слов из файла, где каждое слово находится на отдельной строке.

Формат файла `wordlist.txt`:
никитос
карыч
крем
тауматафакатангихангакоауауотаматеатурипукакапикимаунгахоронукупокаифенуакитанатаху
солнце
