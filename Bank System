#include <iostream>
#include <string>
using namespace std;

int main() {
    // variables
    int money,card,num,pin,login,logpin,trans,send,monsend,depo;
    string acc, retry;
    
    // header
    cout << "Bank Tampan" << endl;
    cout << "=============" << endl;
    
    // open bank account
    cout << "Do you want to open a new bank account? (y/n) ";
    cin >> acc;
    
    if (acc == "y") {
    cout << "Your card number: 12345678" << endl;
    num = 12345678;
    
    cout << "Please enter a new 4-number PIN: ";
    cin >> pin;
    
    cout << "Thank you for trusting Bank Tampan" << endl;
    cout << endl;
    }
    
    // log in
    while (true) {
        // card number
        cout << "Please insert your card number: ";
        cin >> login;

        // pin
        if (login == num) {
            while (true) {
                cout << "Enter your 4-number PIN: ";
                cin >> logpin;

                // transaction
                if (logpin == pin) {
                    while (true) {
                    cout << "\nWhat transaction do you want to do? " << endl;
                    cout << "1. Deposit" << endl;
                    cout << "2. View Balance" << endl;
                    cout << "3. Transfer" << endl;
                    cin >> trans;
                    cout << endl;
                    
                    // deposit
                    if (trans == 1) {
                        cout << "How much would you like to deposit: ";
                        cin >> depo;
                        money += depo;
                        cout << endl;
                        
                        cout << "Bank Tampan" << endl;
                        cout << "=============" << endl;
                        cout << "Saturday, 14/09/2024" << endl;
                        cout << "Deposit success!" << endl;
                        cout << "Amout of deposit: " << depo << endl;
                        cout << "=============" << endl;
                        cout << "Do you want to do another transaction? (y/n) ";
                        cin >> retry;
                        
                        if (retry == "y")
                            continue;
                        else
                            return 0;
                    }
                    
                    // view balance
                    else if (trans == 2) {
                        cout << "Bank Tampan" << endl;
                        cout << "=============" << endl;
                        cout << "Saturday, 14/09/2024" << endl;
                        cout << "Card Number: " << num << endl;
                        cout << "Balance: " << money << endl;
                        cout << "=============" << endl;
                        cout << "Do you want to do another transaction? (y/n) ";
                        cin >> retry;
                        
                        if (retry == "y")
                            continue;
                        else
                            return 0;
                    }
                    
                    // transfer
                    else if(trans == 3) {
                        cout << "Enter the card the number you want to transfer to: ";
                        cin >> send;
                        cout << "How much money you want to transfer: ";
                        if (monsend < money) {
                            cin >> monsend;
                            money -= monsend;
                            cout << endl;
                            cout << "Bank Tampan" << endl;
                            cout << "=============" << endl;
                            cout << "Saturday, 14/09/2024" << endl;
                            cout << "Transfer success!" << endl;
                            cout << "From card number: " << num << endl;
                            cout << "To card number: " << send << endl;
                            cout << "Amout of transfer: " << monsend << endl;
                            cout << "=============" << endl;
                            cout << "Do you want to do another transaction? (y/n) ";
                            cin >> retry;
                        
                            if (retry == "y")
                                continue;
                            else
                                return 0;
                        }
                        else {
                            cout << "You don't have enough money" << endl;
                            continue;
                        }
                    }
                    }
                }
                else 
                    cout << "PIN is incorrect!" << endl;
            }
        }
        else
            cout << "Card number not registered!" << endl;
    }
}

// Things to improve :
// PIN creation rules checking
// Card number random generator
// More transaction features
// Rules for being incorrect too many times
// Loans
