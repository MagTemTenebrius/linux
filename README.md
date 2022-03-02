# lunux

## Laboratory Work #2

#### 1. Каков размер MBR из чего он состоит?

MBR логически можно разделить на три области:

- Код начального загрузчика (446 байт)
- Таблица разделов (четыре записи по 16 байт каждая)
- Сигнатура (2 байта)

Общий размер: 512 байт.

#### 2. Сколько разделов поддерживает MBR

Диски MBR поддерживают только четыре записи в таблице разделов. Для более чем четырех секций требуется дополнительная
структура, известная как расширенная секция.

#### 3. Описать процесс загрузки все этапы на bios и uefi

1. Безовая система загрузки, проверки целостности устройства.
2. Ищет и выполняет загрузчик операционной системы.
3. MBR или GPT в свою очередь передают управление загрузкой Grub (и т.п.).
4. Grub подготавливает систему к загрузке ядра операционной системы.
5. Дальше выполняется загрузка ядра Linux.
6. Ядро запускает главный процесс инициализации, который приводит к запуску всех необходимых служб и программ.

#### 4. Описать порядок загрузки ОС на sysVinit и systemd

##### systemd

Основная особенность — интенсивное распараллеливание запуска служб в процессе загрузки системы, что позволяет
существенно ускорить запуск операционной системы.

Общий порядок:

- BIOS
- Загрузка ядра (GRUB)
- Инициализация ядра
- Запуск systemd, родителя всех процессов.

systemd — родитель всех процессов, ответственный за приведение хоста Linux в состояние эффективной работы. Некоторые его
функции, более обширные, чем те, что были представлены в старой программе инициализации, и должны управлять множеством
аспектов запущенного хоста Linux, включая монтирование файловой системы, запуск и управление системными сервисами,
необходимыми для продуктивной работы хоста Linux. Все задачи systemd, которые не относятся к процессу запуска системы,
выходят за рамки обсуждения в этой статье.

systemd монтирует файловые системы, как определено в /etc/fstab, включая любые swap-файлы и разделы. К этому моменту, он
может получить доступ к файлам конфигурации, расположенным в /etc, включая его собственным. Чтобы определить таргет (
target), по которому нужно загрузить хост он использует конфиг.

#### sysVinit

Запускаются определённые службы, которые соответствуют уровню выполнения. Есть определенные директории уровней в которых
есть определенные службы, которые либо убиваются, либо создаются при переходе на этот уровень. Все происходит в
определенной последовательности. Инициализация просит ядро запустить некоторые начальные системные вызовы. После
закрывает свой стандартный вход и выход. После делает себя лидером сеанса. Он читает и обрабатывает inittab. Он
запускает все процессы, у которых есть запись inittab.

#### 5. Показать скриншоты вашего используемого Linux дистрибутива и объяснить на какой системе инициализации он работает

- Исполльзую wsl, на который поставлена Ubuntu 20.04 LTS.
- Подсистема инициализации systemd. С версии 15.04 она установлена по умолчанию

`systemd is under active development in Ubuntu although the rough plan would be to default to systemd during 
development of 15.04. If you want to help it's best to be running 15.04. (14.10 might be doable as well..)
Источник: ubuntu.com`

![img](./img/neofetch.png)