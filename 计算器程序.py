def binary_calculator(num1, num2, operation):
    if operation == '+':
        return bin(int(num1, 2) + int(num2, 2))[2:]
    elif operation == '-':
        return bin(int(num1, 2) - int(num2, 2))[2:]
    elif operation == '*':
        return bin(int(num1, 2) * int(num2, 2))[2:]
    elif operation == '/':
        if num2 == '0':
            return "错误：除数不能为0"
        return bin(int(num1, 2) // int(num2, 2))[2:]
    else:
        return "无效的操作"


def octal_calculator(num1, num2, operation):
    if operation == '+':
        return oct(int(num1, 8) + int(num2, 8))[2:]
    elif operation == '-':
        return oct(int(num1, 8) - int(num2, 8))[2:]
    elif operation == '*':
        return oct(int(num1, 8) * int(num2, 8))[2:]
    elif operation == '/':
        if num2 == '0':
            return "错误：除数不能为0"
        return oct(int(num1, 8) // int(num2, 8))[2:]
    else:
        return "无效的操作"


def hexadecimal_calculator(num1, num2, operation):
    if operation == '+':
        return hex(int(num1, 16) + int(num2, 16))[2:]
    elif operation == '-':
        return hex(int(num1, 16) - int(num2, 16))[2:]
    elif operation == '*':
        return hex(int(num1, 16) * int(num2, 16))[2:]
    elif operation == '/':
        if num2 == '0':
            return "错误：除数不能为0"
        return hex(int(num1, 16) // int(num2, 16))[2:]
    else:
        return "无效的操作"


def main():
    while True:
        print("""  
        1. 二进制计算器  
        2. 八进制计算器  
        3. 十六进制计算器  
        4. 退出  
        """)
        choice = input("请选择计算器类型 (1/2/3/4): ")

        if choice == '1':
            num1 = input("请输入第一个二进制数: ")
            num2 = input("请输入第二个二进制数: ")
            operation = input("请输入运算符 (+, -, *, /): ")
            result = binary_calculator(num1, num2, operation)
            print(f"结果: {result}")

        elif choice == '2':
            num1 = input("请输入第一个八进制数: ")
            num2 = input("请输入第二个八进制数: ")
            operation = input("请输入运算符 (+, -, *, /): ")
            result = octal_calculator(num1, num2, operation)
            print(f"结果: {result}")

        elif choice == '3':
            num1 = input("请输入第一个十六进制数: ")
            num2 = input("请输入第二个十六进制数: ")
            operation = input("请输入运算符 (+, -, *, /): ")
            result = hexadecimal_calculator(num1, num2, operation)
            print(f"结果: {result}")

        elif choice == '4':
            print("退出计算器...")
            break

        else:
            print("无效的选择，请重新输入。")


if __name__ == "__main__":
    main()
