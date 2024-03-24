#include <iostream>

using namespace std;

int main() {
    char op;
    float num1, num2;

    cout << "Enter operator (+, -, *, /): ";
    cin >> op;

    cout << "Enter two numbers: ";
    cin >> num1 >> num2;

    switch(op) {
        case '+':
            cout << "Result: " << num1 + num2;
            break;
        case '-':
            cout << "Result: " << num1 - num2;
            break;
        case '*':
            cout << "Result: " << num1 * num2;
            break;
        case '/':
            if (num2 == 0) {
                cout << "Error! Division by zero!";
            } else {
                cout << "Result: " << num1 / num2;
            }
            break;
        default:
            cout << "Error! Invalid operator!";
            break;
    }

    return 0;
}
