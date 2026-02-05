# 学生数据存储
students = []
courses = ["数学", "英语", "Python"]

while True:
    print("\n=== 学生成绩管理系统 ===")
    print("1. 添加学生")
    print("2. 录入成绩")
    print("3. 查看成绩")
    print("4. 显示所有")
    print("5. 退出")
    print("=====================")

    choice = input("请选择(1-5): ")

    if choice == "1":
        # 添加学生
        print("\n--- 添加学生 ---")
        student_id = input("学号: ")
        name = input("姓名: ")

        # 检查学号是否重复
        found = False
        forin students:
            if[0] == student_id:
                found = True
                break

        if found:
            print("错误：该学号已存在！")
        else:
            # 使用列表存储：[学号, 姓名, 数学成绩, 英语成绩, Python成绩]
            students.append([student_id, name, 0, 0, 0])
            print(f"学生 {name} 添加成功！")

    elif choice == "2":
        # 录入成绩
        print("\n--- 录入成绩 ---")
        if not students:
            print("还没有学生！请先添加学生。")
            continue

        student_id = input("请输入学号: ")

        # 查找学生
        found_index = -1
        for i, s in enumerate(students):
            if[0] == student_id:
                found_index = i
                break

        if found_index == -1:
            print("找不到该学号的学生！")
        else:
            student = students[found_index]
            print(f"\n正在为 {student[1]} 录入成绩:")

            for j, course in enumerate(courses):
                while True:
                    try:
                        score = float(input(f"{course}成绩: "))
                        if 0 <= score <= 100:
                            student[2 + j] = score
                            break
                        else:
                            print("成绩必须在0-100之间！")
                    except:
                        print("请输入数字！")

            print("成绩录入成功！")

    elif choice == "3":
        # 查看成绩
        print("\n--- 查看成绩 ---")
        if not students:
            print("还没有学生！")
            continue

        student_id = input("请输入学号: ")

        # 查找学生
        found = False
        forin students:
            if[0] == student_id:
                found = True
                print(f"\n学生信息:")
                print(f"学号: {[0]}")
                print(f"姓名: {[1]}")
                print("各科成绩:")

                total = 0
                count = 0
                for j, course in enumerate(courses):
                    score = s[2 + j]
                    if score > 0:
                        print(f"  {course}: {score}")
                        total += score
                        count += 1
                    else:
                        print(f"  {course}: 未录入")

                if count > 0:
                    average = total / count
                    print(f"平均分: {average:.1f}")

                break

        if not found:
            print("找不到该学号的学生！")

    elif choice == "4":
        # 显示所有学生
        print("\n--- 所有学生 ---")
        if not students:
            print("暂无学生")
        else:
            print("学号\t姓名\t数学\t英语\tPython\t平均分")
            print("-" * 40)

            forin students:
                total = 0
                count = 0
                scores_text = []

                for j in range(3):
                    score = s[2 + j]
                    scores_text.append(str(score) if score > 0 else "未录")
                    if score > 0:
                        total += score
                        count += 1

                if count > 0:
                    average = total / count
                    avg_text = f"{average:.1f}"
                else:
                    avg_text = "未录"

                print(f"{[0]}\t{[1]}\t{scores_text[0]}\t{scores_text[1]}\t{scores_text[2]}\t{avg_text}")

    elif choice == "5":
        print("再见！")
        break

    else:
        print("请输入1-5之间的数字！")
