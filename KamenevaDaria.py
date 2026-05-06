import random

total_attempts = 0  # commit 1
difficulty = "medium"  # commit 6: easy/medium/hard

def generate_example():
    global difficulty # commit 6
    if difficulty == "easy": # commit 6
        max_num = 10 # commit 6
    elif difficulty == "hard": # commit 6
        max_num = 50 # commit 6
    else: # commit 6
        max_num = 20 # commit 6
    a = random.randint(5, max_num)  # commit 6, commit 10
    b = random.randint(0, max_num)  # commit 6, commit 10
    op = random.choice(['+', '-', '*'])
    
    if op == '+':
        result = a + b
        example = f"{a} + {b}"
    else:
        if op == '-':
            a, b = max(a, b), min(a, b)
            result = a - b
            example = f"{a} - {b}"
        else:
            result = a * b
            example = f"{a} × {b}"
    return example, result

def math_quiz():
    score = 0
    total = 5
    
    print("МАТЕМАТИЧЕСКИЙ ТРЕНАЖЕР (самый лучший🤩)")  # commit 5, commit 9
    print(f"Реши {total} примеров")
    
    for i in range(total):
        example, correct = generate_example()
        print(f"\nПример №{i+1}: {example} = ?")

        global total_attempts
        total_attempts += 1  # commit 2
        
        try:
            answer = int(input("Твой ответ: "))
            if answer == correct:
                print("Правильно!")
                score += 1
            else:
                print(f"Неверно! Правильный ответ: {correct}")
        except ValueError:
            print("Ошибка! Принимаются только числа")
            break
    
    print(f"Итог: {score}/{total}")
    if score == total:
        print("Отлично! Ты гений!")
    else: 
        if score >= total/2:
            print("Неплохо, но можно лучше")
        else:
            print("Нужно подтянуть математику")

def show_stats():
    global total_attempts
    print(f"\nПопыток за всё время: {total_attempts} ⏱️")  # commit 3, commit 8

while True:
    print("\n1. Начать тренировку")
    print("2. Показать статистику")  # commit 4
    print("3. Выбрать сложность")  # commit 7
    print("0. Выйти")
    
    choice = input("Выбери: ")
    if choice == "0":
        print("Успехов в учебе!")
        break
    elif choice == "1":
        math_quiz()
    elif choice == "2":
        show_stats()  # commit 4
    elif choice == "3":
        set_difficulty()  # commit 7
    else:
        print("Некорректный ввод!")