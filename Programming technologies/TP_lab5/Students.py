from typing import List, Dict, Union


def read_students_file(file_path: str) -> List[Dict[str, Union[str, float, int]]]:
    students: List[Dict[Union[str, float, int]]] = []
    with open(file_path, "r") as file:
        for line in file:
            data: List[str] = line.strip().split()
            students.append({
                "фамилия": data[0],
                "год рождения": int(data[1]),
                "номер группы": data[2],
                "средняя оценка": float(data[3]),
                "год поступления": int(data[4])
            })
    return students


def print_same_surnames(students: List[Dict[str, Union[str, float, int]]]) -> None:
    surnames: Dict = {}
    for student in students:
        surname = student["фамилия"]
        if surname in surnames:
            surnames[surname].append(student)
        else:
            surnames[surname] = [student]

    for surname, students_list in surnames.items():
        if len(students_list) > 1:
            print(f"Студенты с фамилией {surname}:")
            for student in students_list:
                print(student)


def print_straight_a_students(students: List[Dict[str, Union[str, float, int]]]) -> None:
    for student in students:
        if student["средняя оценка"] == 5.0:
            print(student)


def print_students_by_group(students: List[Dict[str, Union[str, float, int]]]) -> None:
    groups: Dict = {}
    for student in students:
        group = student["номер группы"]
        if group in groups:
            groups[group].append(student)
        else:
            groups[group] = [student]

    for group, students_list in groups.items():
        print(f"Группа {group}:")
        for student in students_list:
            print(student)


def max_students_group(students: List[Dict[str, Union[str, float, int]]]) -> Dict:
    groups_count: Dict = {}
    for student in students:
        group = student["номер группы"]
        if group in groups_count:
            groups_count[group] += 1
        else:
            groups_count[group] = 1
    max_group: Dict = max(groups_count, key=groups_count.get)
    return max_group


def max_straight_a_group(students: List[Dict[str, Union[str, float, int]]]) -> Union[str, float, int]:
    straight_a_count: Dict = {}
    for student in students:
        if student["средняя оценка"] == 5.0:
            group: Union[str, float, int] = student["номер группы"]
            if group in straight_a_count:
                straight_a_count[group] += 1
            else:
                straight_a_count[group] = 1
    if straight_a_count:
        max_group: Union[str, float, int] = max(straight_a_count, key=straight_a_count.get)
        return max_group
    else:
        return "Нет отличников"


def create_group_files(students: List[Dict[str, Union[str, float, int]]]) -> None:
    groups: Dict = {}
    for student in students:
        group: Union[str, float, int] = student["номер группы"]
        if group in groups:
            groups[group].append(student)
        else:
            groups[group] = [student]

    for group, students_list in groups.items():
        with open(f"Group_{group}_students.txt", "w") as file:
            for student in students_list:
                file.write(
                    f"{student['фамилия']}, {student['год рождения']}, {student['номер группы']}, "
                    f"{student['средняя оценка']}, {student['год поступления']}\n")


if __name__ == "__main__":
    students_data = read_students_file("Students.txt")

    print_same_surnames(students_data)
    print("\nКруглые отличники:")
    print_straight_a_students(students_data)
    print("\nСтуденты по группам:")
    print_students_by_group(students_data)
    print("\nНомер группы с максимальным количеством студентов:", max_students_group(students_data))
    print("Номер группы с максимальным количеством отличников:", max_straight_a_group(students_data))
