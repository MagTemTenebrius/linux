# Linux

## Laboratory Work #7

#### 1. Как отобразить 4 последних выполненных команды?

`history 4`

#### 2. Перевести задание в фоновый режим в bash можно командой

`bg`

#### 3. Какая комбинация клавиш переключит вас на 4-ю виртуальную консоль?

`Ctrl`+`Alt`+`F4`

#### 4. Какая переменная среды содержит путь к домашнему каталогу?

`pwd`

#### 5. Установить в bash переменную MYVAR в качестве системной можно командой?

`export MYVAR`

#### 6. Какие комбинации клавиш позволят выделить несколько файлов в Midnight Commander?

`Ctrl + T`

#### 7. Что выведет на экран этот сценарий?

```shell
#!/bin/bash
VAR=`echo 'test'`
VAR2=`echo '$VAR'`
echo $VAR2
```

output: `$VAR`

#### 8. Что выведет на экран это сценарий?

```shell
#!/bin/bash
cd /etc
VAR="$PWD"
if [ -n "$VAR" ]; then
 echo "$VAR"
else
 echo '$VAR'
fi 
```

output: `/etc`

#### 9. Что выведет на экран этот сценарий?

```shell
#!/bin/bash
A=1
B=2
if [ $A -eq $B  ]; then
 echo '$A'
else
 echo "$B"
fi
``` 

output: `2`

#### Задача 1.

Написать скрипт, который получает в качестве аргумента 3 значения, a, b, c, d. A - высота прямоугольника, б - ширина
прямоугольника с 0/1 - пустой или заполненный d - символ из которого следует рисовать.

Ответ:
```shell
#!/bin/bash

if [ "$#" -ne 4 ]
then
    echo "$0 <height> <weight> <is full> <char>"
    exit 1
fi

let Height=$1-1
let Weight=$2-1
for ((i = 0; i < $Height + 1; i++)); do
   for ((j = 0; j < $Weight; j++)); do
   	if [ $i -eq 0 -o $i -eq $Height ] 
   		then
   		echo -n $4
   	else 
   		if [ $j -eq 0 -o $j -eq $Weight ] 
   			then
   			echo -n $4
   		else					
   			if [ $3 -eq 0 ]
   				then
   				echo -n " "
   			else echo -n $4
   			fi
   		fi
   	fi
   done
   echo ''
done
```