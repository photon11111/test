#Тестовое на должность стажера-программиста игровой логики

##Задача 1:

**Формулировка**:

На языке Python написать алгоритм (функцию) определения четности целого числа, который будет аналогичен нижеприведенному по функциональности, но отличен по своей сути. Объяснить плюсы и минусы обеих реализаций. 

Пример: 

def isEven(value):

      return value % 2 == 0

**Решение**:

- Рассмотрение базовой реализации:
    - Плюсы:
        - данный код легко читается и понимается
        - универсальность для всех типов чисел
    - Минусы:
        - операция деления является более затратной, чем побитовая операция в альтернативном методе

- Рассмотрение альтернативной реализации:
    -Плюсы:
        - побитовая операция работает напрямую с представлением числа в памяти, что делает определение остатка более быстрым, чем при подходе, основанном на делении
    -Минусы:
        - необходимо совершать дополнительные операции для того, чтобы подход корректно работал на float'ах и отрицательных числах
        - для этого метода приходится импортировать дополнительные зависимости, в то время как базовая реализация работает на средствах стандартной библиотеки
        - более сложный код, по сравнению с базовой реализацией

В итоге, базовая реализация является более предпочтительной. Альтернативную версию лучше использовать только для случая, когда, во-первых, она будет выполняться только для int'ов, что позволит убрать операции взятия абсолютного значения и каста к целочисленному типу, а во-вторых, большая эффективность побитовой операции критична (при вычислении на очень большом объеме данных, например).

##Задача 2:

**Формулировка**:

На языке Python написать минимум по 2 класса реализовывающих циклический буфер FIFO. Объяснить плюсы и минусы каждой реализации.

**Решение**:

Описания классов очередей:

- **Queue1**: циклическая очередь на односвязном списке

    - оценка сложности **enqueue**:
        - Временная сложность: O(1)
        - Пространственная сложность: O(1)
    - оценка сложности **dequeue**:
        - Временная сложность: O(1)
        - Пространственная сложность: O(1)
    - оценка сложности **peek**:
        - Временная сложность: O(1)
        - Пространственная сложность: O(1)

Это достаточно эффективная реализация очереди, которая выполняет за O(1) основные операции, однако, из-за постоянно создающихся элементов списка, нагрузка на сборщик мусора будет высокой.

- **Queue2**: циклическая очередь на двусвязном списке (deque)

    - оценка сложности **enqueue**:
        - Временная сложность: O(1)
        - Пространственная сложность: O(1)
    - оценка сложности **dequeue**:
        - Временная сложность: O(1)
        - Пространственная сложность: O(1)
    - оценка сложности **peek**:
        - Временная сложность: O(1)
        - Пространственная сложность: O(1)

Основная идея такая же, как у предыдущего класса, но используется готовая реализация структуры данных deque из библиотеки colections, что делает код лаконичнее и понятнее.

- **Queue3**: циклическая очередь на списке

    - оценка сложности **enqueue**:
        - Временная сложность (амортизационная): O(1)
        - Пространственная сложность (амортизационная): O(1)
    - оценка сложности **dequeue**:
        - Временная сложность: O(N)
        - Пространственная сложность: O(N)
    - оценка сложности **peek**:
        - Временная сложность: O(1)
        - Пространственная сложность: O(1)

Плюс этой реализации в ее простоте. Однако она является самой неэффективной из представленных из-за удаления элемента из начала списка.

- **Queue4**: циклическая очередь на двух списках, доработанная версия Queue3

    - оценка сложности **enqueue**:
        - Временная сложность (амортизационная): O(1)
        - Пространственная сложность (амортизационная): O(1)
    - оценка сложности **dequeue**:
        - Временная сложность (амортизационная): O(1)
        - Пространственная сложность (амортизационная): O(1)
    - оценка сложности **peek**:
        - Временная сложность: O(1)
        - Пространственная сложность: O(1)

Улучшенная версия предыдущего подхода. Все еще сохраняет простоту, но работает эффективнее. Однако эта реализация менее эффективна, чем другие подходы.

- **Queue5**: циклическая очередь на массиве

    - оценка сложности **enqueue**:
        - Временная сложность: O(1)
        - Пространственная сложность: O(1)
    - оценка сложности **dequeue**:
        - Временная сложность: O(1)
        - Пространственная сложность: O(1)
    - оценка сложности **peek**:
        - Временная сложность: O(1)
        - Пространственная сложность: O(1)

Данная реализация является самой эффективной из представленных за счет того, что здесь есть фиксированное выделение памяти. Но при ее разработке проще всего допустить неочевидную ошибку, которая будет долго отлаживаться.

##Задача 3: 

**Формулировка**:

На языке Python предложить алгоритм, который быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел. Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным). Объяснить, почему вы считаете, что функция соответствует заданным критериям.

**Решение**:

Для решения данной задачи подходит алгоритм Timsort, реализованный в стандратной библиотеке. Он удовлетворяет указанным критериям по следующим причинам:

1. Этот алгоритм был создан для сортиовки реальных данных, и потому он оптимизирован для случаев частично или полностью отсротированных входных данных.

2. Данный алгоритм имеет лучшие, чем у других алгоритмов, асимптотические оценки временной сложности:
    - $O(N)$ для лучшего случая
    - $O(N log N)$ для худшего случая
    - $O(N log N)$ в среднем

3. Исходный код данного метода написан на C, что делает его более быстрым, чем любая реализация на Python, и оптимизирует затраченные процессорные тики.